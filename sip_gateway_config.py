#!/usr/bin/env python3
"""
SIP Gateway Auto-Configuration Script

This script automates the login and configuration of a SIP gateway device.
It uses Selenium to interact with the web interface and prompts the user
for configuration parameters interactively.
"""

import time
import json
from typing import Dict, List, Any, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import urllib3

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SIPGatewayConfigurator:
    """Automates SIP Gateway configuration through web interface."""
    
    def __init__(self, base_url: str, username: str, password: str):
        """
        Initialize the SIP Gateway configurator.
        
        Args:
            base_url: Base URL of the SIP gateway (e.g., https://192.168.1.122:31567)
            username: Admin username
            password: Admin password
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.driver = None
        self.config_data = {}
        
    def setup_driver(self):
        """Set up Chrome WebDriver with appropriate options."""
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # Uncomment the following line to run in headless mode
        # chrome_options.add_argument('--headless')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_page_load_timeout(30)
        
    def login(self) -> bool:
        """
        Log in to the SIP gateway.
        
        Returns:
            True if login successful, False otherwise
        """
        try:
            print(f"[*] Navigating to login page: {self.base_url}/cgi-bin/login")
            self.driver.get(f"{self.base_url}/cgi-bin/login")
            
            # Wait for login form to load
            wait = WebDriverWait(self.driver, 10)
            
            # Find and fill username field
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.clear()
            username_field.send_keys(self.username)
            print(f"[+] Entered username: {self.username}")
            
            # Find and fill password field
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.clear()
            password_field.send_keys(self.password)
            print(f"[+] Entered password")
            
            # Submit the form
            login_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'], button[type='submit']")
            login_button.click()
            print("[+] Clicked login button")
            
            # Wait for redirect or success indication
            time.sleep(2)
            
            # Check if login was successful (URL should change or no error message)
            current_url = self.driver.current_url
            if "login" not in current_url or self.is_logged_in():
                print("[+] Login successful!")
                return True
            else:
                print("[-] Login may have failed")
                return False
                
        except Exception as e:
            print(f"[-] Login error: {str(e)}")
            return False
    
    def is_logged_in(self) -> bool:
        """Check if currently logged in."""
        try:
            # Try to detect if we're on a protected page
            return "login" not in self.driver.current_url.lower()
        except:
            return False
    
    def probe_page(self, url: str) -> Dict[str, Any]:
        """
        Probe a configuration page and extract form fields.
        
        Args:
            url: URL to probe
            
        Returns:
            Dictionary containing page information and form fields
        """
        print(f"\n[*] Probing page: {url}")
        try:
            self.driver.get(url)
            time.sleep(1)
            
            page_info = {
                'url': url,
                'title': self.driver.title,
                'fields': []
            }
            
            # Find all input fields
            inputs = self.driver.find_elements(By.TAG_NAME, "input")
            selects = self.driver.find_elements(By.TAG_NAME, "select")
            textareas = self.driver.find_elements(By.TAG_NAME, "textarea")
            
            # Process input fields
            for inp in inputs:
                field_type = inp.get_attribute("type")
                field_name = inp.get_attribute("name")
                field_id = inp.get_attribute("id")
                field_value = inp.get_attribute("value")
                
                # Skip submit buttons and hidden fields we don't want to configure
                if field_type in ["submit", "button", "hidden"]:
                    continue
                
                # Get label if available
                label = self._get_field_label(inp, field_id, field_name)
                
                field_info = {
                    'type': 'input',
                    'input_type': field_type,
                    'name': field_name,
                    'id': field_id,
                    'label': label,
                    'current_value': field_value,
                    'element': inp
                }
                page_info['fields'].append(field_info)
                print(f"  - Found input: {label or field_name} (type: {field_type})")
            
            # Process select fields
            for sel in selects:
                field_name = sel.get_attribute("name")
                field_id = sel.get_attribute("id")
                label = self._get_field_label(sel, field_id, field_name)
                
                # Get all options
                select_obj = Select(sel)
                options = [opt.text for opt in select_obj.options]
                current_value = select_obj.first_selected_option.text
                
                field_info = {
                    'type': 'select',
                    'name': field_name,
                    'id': field_id,
                    'label': label,
                    'options': options,
                    'current_value': current_value,
                    'element': sel
                }
                page_info['fields'].append(field_info)
                print(f"  - Found select: {label or field_name} (options: {', '.join(options)})")
            
            # Process textarea fields
            for ta in textareas:
                field_name = ta.get_attribute("name")
                field_id = ta.get_attribute("id")
                field_value = ta.get_attribute("value") or ta.text
                label = self._get_field_label(ta, field_id, field_name)
                
                field_info = {
                    'type': 'textarea',
                    'name': field_name,
                    'id': field_id,
                    'label': label,
                    'current_value': field_value,
                    'element': ta
                }
                page_info['fields'].append(field_info)
                print(f"  - Found textarea: {label or field_name}")
            
            return page_info
            
        except Exception as e:
            print(f"[-] Error probing page {url}: {str(e)}")
            return {'url': url, 'error': str(e), 'fields': []}
    
    def _get_field_label(self, element, field_id: str, field_name: str) -> str:
        """Try to find the label for a form field."""
        try:
            # Try to find label by 'for' attribute
            if field_id:
                labels = self.driver.find_elements(By.CSS_SELECTOR, f"label[for='{field_id}']")
                if labels:
                    return labels[0].text.strip()
            
            # Try to find parent td and previous td (common in table layouts)
            parent = element.find_element(By.XPATH, "..")
            if parent.tag_name == "td":
                try:
                    prev_td = parent.find_element(By.XPATH, "preceding-sibling::td[1]")
                    label_text = prev_td.text.strip()
                    if label_text:
                        return label_text
                except:
                    pass
            
            # Try to find nearby text
            try:
                parent_text = parent.text.strip()
                if parent_text and len(parent_text) < 100:
                    return parent_text
            except:
                pass
                
            return field_name or "Unknown"
            
        except:
            return field_name or "Unknown"
    
    def get_configuration_examples(self) -> Dict[str, str]:
        """Return example values for common SIP configuration fields."""
        return {
            # Network settings
            'ip': '192.168.1.100',
            'netmask': '255.255.255.0',
            'gateway': '192.168.1.1',
            'dns1': '8.8.8.8',
            'dns2': '8.8.4.4',
            'hostname': 'sipgateway',
            
            # SIP Server settings
            'sip_server': 'sip.example.com',
            'sip_port': '5060',
            'sip_domain': 'example.com',
            'register_server': 'sip.example.com',
            'proxy_server': 'sip.example.com',
            'outbound_proxy': 'sip.example.com',
            
            # SIP Account settings
            'username': 'user1000',
            'auth_username': 'user1000',
            'display_name': 'User 1000',
            'password': 'your_sip_password',
            'extension': '1000',
            
            # Codec settings
            'codec': 'ulaw,alaw,g729',
            
            # Port settings
            'sip_local_port': '5060',
            'rtp_start_port': '10000',
            'rtp_end_port': '20000',
            
            # Other common fields
            'enabled': 'yes',
            'register': 'yes',
            'dtmf': 'rfc2833',
        }
    
    def collect_user_input(self, pages_info: List[Dict[str, Any]]) -> Dict[str, str]:
        """
        Interactively collect configuration values from the user.
        
        Args:
            pages_info: List of page information dictionaries
            
        Returns:
            Dictionary mapping field names to user-provided values
        """
        print("\n" + "="*70)
        print("SIP GATEWAY CONFIGURATION")
        print("="*70)
        print("\nThe following configuration parameters were found.")
        print("Please enter values for each field, or press Enter to skip.")
        print("\nExamples are provided in parentheses for guidance.\n")
        
        examples = self.get_configuration_examples()
        user_config = {}
        
        for page_info in pages_info:
            if not page_info.get('fields'):
                continue
                
            print(f"\n--- Configuration from: {page_info['url']} ---")
            
            for field in page_info['fields']:
                field_name = field.get('name')
                if not field_name:
                    continue
                
                field_label = field.get('label', field_name)
                field_type = field.get('type')
                current_value = field.get('current_value', '')
                
                # Create prompt
                prompt_parts = [f"{field_label}"]
                
                # Add field type info
                if field_type == 'select':
                    options = field.get('options', [])
                    prompt_parts.append(f"[Options: {', '.join(options)}]")
                elif field.get('input_type') == 'checkbox':
                    prompt_parts.append("[yes/no]")
                elif field.get('input_type') == 'password':
                    prompt_parts.append("[password]")
                
                # Add current value if exists
                if current_value:
                    prompt_parts.append(f"[Current: {current_value}]")
                
                # Add example if available
                example_found = False
                for key, example_val in examples.items():
                    if key.lower() in field_name.lower() or key.lower() in field_label.lower():
                        prompt_parts.append(f"(e.g., {example_val})")
                        example_found = True
                        break
                
                if not example_found and field_type == 'input':
                    input_type = field.get('input_type', 'text')
                    if input_type == 'text':
                        prompt_parts.append("(e.g., value)")
                    elif input_type == 'number':
                        prompt_parts.append("(e.g., 5060)")
                
                prompt = " ".join(prompt_parts) + ": "
                
                try:
                    user_input = input(prompt).strip()
                    if user_input:
                        user_config[field_name] = user_input
                        print(f"  ✓ Set {field_name} = {user_input}")
                    else:
                        print(f"  ○ Skipped {field_name}")
                except (KeyboardInterrupt, EOFError):
                    print("\n\n[!] Configuration interrupted by user")
                    return user_config
        
        print("\n" + "="*70)
        print(f"Configuration complete! Collected {len(user_config)} parameters.")
        print("="*70 + "\n")
        
        return user_config
    
    def apply_configuration(self, page_info: Dict[str, Any], user_config: Dict[str, str]) -> bool:
        """
        Apply configuration values to a page.
        
        Args:
            page_info: Page information dictionary
            user_config: User-provided configuration values
            
        Returns:
            True if configuration applied successfully
        """
        try:
            print(f"\n[*] Applying configuration to: {page_info['url']}")
            self.driver.get(page_info['url'])
            time.sleep(1)
            
            applied_count = 0
            
            for field in page_info['fields']:
                field_name = field.get('name')
                if not field_name or field_name not in user_config:
                    continue
                
                value = user_config[field_name]
                field_type = field.get('type')
                
                try:
                    if field_type == 'input':
                        input_type = field.get('input_type')
                        element = self.driver.find_element(By.NAME, field_name)
                        
                        if input_type == 'checkbox':
                            # Handle checkbox
                            should_check = value.lower() in ['yes', 'true', '1', 'on', 'checked']
                            if should_check != element.is_selected():
                                element.click()
                        elif input_type == 'radio':
                            # Handle radio button
                            element.click()
                        else:
                            # Handle text, password, number, etc.
                            element.clear()
                            element.send_keys(value)
                        
                        print(f"  ✓ Set {field_name} = {value}")
                        applied_count += 1
                        
                    elif field_type == 'select':
                        element = self.driver.find_element(By.NAME, field_name)
                        select_obj = Select(element)
                        
                        # Try to select by visible text first, then by value
                        try:
                            select_obj.select_by_visible_text(value)
                        except:
                            select_obj.select_by_value(value)
                        
                        print(f"  ✓ Set {field_name} = {value}")
                        applied_count += 1
                        
                    elif field_type == 'textarea':
                        element = self.driver.find_element(By.NAME, field_name)
                        element.clear()
                        element.send_keys(value)
                        print(f"  ✓ Set {field_name} = {value}")
                        applied_count += 1
                        
                except Exception as e:
                    print(f"  ✗ Failed to set {field_name}: {str(e)}")
            
            # Try to find and click submit button
            try:
                submit_buttons = self.driver.find_elements(By.CSS_SELECTOR, 
                    "input[type='submit'], button[type='submit'], input[value*='Save'], input[value*='Apply'], button[value*='Save'], button[value*='Apply']")
                
                if submit_buttons:
                    submit_buttons[0].click()
                    print(f"  ✓ Submitted form")
                    time.sleep(2)
                else:
                    print(f"  ⚠ No submit button found, changes not saved")
                    
            except Exception as e:
                print(f"  ⚠ Could not submit form: {str(e)}")
            
            print(f"[+] Applied {applied_count} configuration(s)")
            return applied_count > 0
            
        except Exception as e:
            print(f"[-] Error applying configuration: {str(e)}")
            return False
    
    def run_configuration_workflow(self):
        """Run the complete configuration workflow."""
        try:
            # Setup driver
            print("[*] Setting up Chrome WebDriver...")
            self.setup_driver()
            
            # Login
            if not self.login():
                print("[-] Failed to login. Exiting.")
                return False
            
            # Configuration pages to probe
            config_pages = [
                f"{self.base_url}/cgi-bin/config2",
                f"{self.base_url}/cgi-bin/config",
                f"{self.base_url}/cgi-bin/config_a1",
                f"{self.base_url}/cgi-bin/config_a2",
                f"{self.base_url}/cgi-bin/config_dns",
            ]
            
            # Probe all configuration pages
            pages_info = []
            for page_url in config_pages:
                page_info = self.probe_page(page_url)
                if page_info.get('fields'):
                    pages_info.append(page_info)
            
            if not pages_info:
                print("\n[-] No configuration fields found on any page.")
                return False
            
            # Collect user input
            user_config = self.collect_user_input(pages_info)
            
            if not user_config:
                print("\n[!] No configuration values provided. Exiting.")
                return False
            
            # Apply configuration to each page
            print("\n[*] Applying configuration to gateway...")
            for page_info in pages_info:
                self.apply_configuration(page_info, user_config)
            
            print("\n[+] Configuration complete!")
            print("\n" + "="*70)
            print("SUMMARY")
            print("="*70)
            print(f"Total parameters configured: {len(user_config)}")
            print("\nYour SIP gateway should now be configured.")
            print("You can use any SIP client to register with the following info:")
            print(f"  - SIP Server: {user_config.get('sip_server', 'N/A')}")
            print(f"  - Username: {user_config.get('username', 'N/A')}")
            print(f"  - Extension: {user_config.get('extension', 'N/A')}")
            print("="*70 + "\n")
            
            return True
            
        except Exception as e:
            print(f"\n[-] Fatal error: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
            
        finally:
            # Keep browser open for a moment so user can see the result
            input("\nPress Enter to close the browser and exit...")
            if self.driver:
                self.driver.quit()
                print("[*] Browser closed.")


def main():
    """Main entry point."""
    print("\n" + "="*70)
    print("SIP GATEWAY AUTO-CONFIGURATION TOOL")
    print("="*70)
    print("\nThis tool will help you configure your SIP gateway automatically.")
    print("It will probe the configuration pages and ask you for the required")
    print("parameters with examples to guide you.\n")
    
    # Default configuration
    base_url = "https://192.168.1.122:31567"
    username = "admin"
    password = "Abcd--1234"
    
    print(f"Gateway URL: {base_url}")
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}\n")
    
    # Ask if user wants to change defaults
    change = input("Use these settings? (y/n) [y]: ").strip().lower()
    if change == 'n':
        base_url = input(f"Enter gateway URL [{base_url}]: ").strip() or base_url
        username = input(f"Enter username [{username}]: ").strip() or username
        password = input(f"Enter password: ").strip() or password
    
    # Create configurator and run
    configurator = SIPGatewayConfigurator(base_url, username, password)
    success = configurator.run_configuration_workflow()
    
    if success:
        print("\n[+] All done! Your SIP gateway is configured.")
        return 0
    else:
        print("\n[-] Configuration incomplete or failed.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
