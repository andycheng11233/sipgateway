#!/bin/bash
# Quick Start Script for SIP Gateway Configuration

echo "=========================================="
echo "SIP Gateway Configuration - Quick Start"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher."
    exit 1
fi

echo "✓ Python 3 found"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Check if Chrome is installed
if ! command -v google-chrome &> /dev/null && ! command -v chromium-browser &> /dev/null; then
    echo ""
    echo "⚠ Warning: Chrome/Chromium browser not detected."
    echo "Please ensure Google Chrome is installed for Selenium to work."
    echo ""
fi

echo ""
echo "=========================================="
echo "Setup complete! Starting configuration..."
echo "=========================================="
echo ""

# Run the configuration script
python3 sip_gateway_config.py

# Deactivate virtual environment
deactivate
