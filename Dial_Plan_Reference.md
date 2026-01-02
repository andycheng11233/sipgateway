# HT813 Dial Plan Reference Guide

## Understanding Dial Plans

A dial plan defines which number patterns the HT813 will accept and how to process them. This guide explains the syntax and provides examples for common scenarios.

---

## Table of Contents

1. [Basic Syntax](#basic-syntax)
2. [Pattern Matching](#pattern-matching)
3. [Common Examples](#common-examples)
4. [Country-Specific Plans](#country-specific-dial-plans)
5. [Advanced Routing](#advanced-routing)
6. [Testing Your Dial Plan](#testing-your-dial-plan)

---

## Basic Syntax

### Dial Plan Format
```
{ pattern1 | pattern2 | pattern3 }
```

Patterns are enclosed in `{ }` and separated by `|` (pipe character).

### Basic Wildcards

| Symbol | Meaning | Example |
|--------|---------|---------|
| `x` | Any digit 0-9 | `x` matches 0,1,2...9 |
| `.` | One or more digits | `xx.` matches 11, 123, 12345, etc. |
| `+` | One or more of previous | `x+` matches any number of digits |
| `*` | Zero or more of previous | `x*` matches 0 or more digits |
| `[]` | Range or set | `[2-9]` matches 2,3,4,5,6,7,8,9 |
| `\` | Escape character | `\+` matches literal + sign |

### Special Characters

| Character | Purpose |
|-----------|---------|
| `<>` | Strip digits | `<1>xxxxxxxxxx` strips leading 1 |
| `( )` | Grouping | Group patterns together |
| `{ }` | Enclose entire dial plan | Required wrapper |
| `\|` | OR separator | Separate multiple patterns |

---

## Pattern Matching

### Exact Length Patterns

Match specific number of digits:

```
# Match exactly 7 digits (local calls)
{ xxxxxxx }

# Match exactly 10 digits
{ xxxxxxxxxx }

# Match exactly 11 digits (1 + 10)
{ xxxxxxxxxxx }
```

### Variable Length Patterns

Match flexible lengths:

```
# Match 1 or more digits (any length)
{ x+ }

# Match 2 or more digits
{ xx+ }

# Match 1 or more, using dot notation
{ x. }
```

### Range Patterns

Match specific digit ranges:

```
# Match digits 2-9 only (no 0 or 1)
{ [2-9] }

# Match 10-digit number starting with 2-9
{ [2-9]xxxxxxxxx }

# Match area codes 200-999
{ [2-9][0-9][0-9]xxxxxxx }
```

### Prefix Patterns

Match numbers starting with specific digits:

```
# Match numbers starting with 011 (US international)
{ 011xx. }

# Match numbers starting with 1800 (toll-free)
{ 1800xxxxxxx }

# Match 911 emergency
{ 911 }
```

---

## Common Examples

### Universal (Most Permissive)

Accepts any dialing pattern:
```
{ x+ | \+x+ | *x+ | *xx*x+ }
```

**Accepts:**
- Any number of digits: `123`, `5551234`, `18005551234`
- International format: `+1234567890`
- Star codes: `*72`, `*67`, `*69`
- Feature codes: `*21*1234567890`

**Use when:** You want maximum flexibility

---

### USA Dial Plans

#### USA - Full Featured
```
{ [2-9]11 | 1[2-9]xxxxxxxxx | [2-9]xxxxxxxxx | 011xx. | \+x+ | *x+ }
```

**Accepts:**
- Emergency: `911`, `311`, `511`, `811`
- Long distance: `1-xxx-xxx-xxxx`
- Local 10-digit: `xxx-xxx-xxxx`
- International: `011-...`
- International format: `+...`
- Star codes: `*72`, `*67`, etc.

**Rejects:**
- Invalid numbers starting with 0 or 1
- Incomplete numbers

#### USA - Basic
```
{ 911 | [2-9]xxxxxxxxx | 1[2-9]xxxxxxxxx }
```

**Accepts:**
- Emergency: `911`
- 10-digit: `2025551234`
- 11-digit: `12025551234`

**Use when:** You only need basic calling

#### USA - With 7-Digit Local
```
{ 911 | [2-9]xxxxxx | [2-9]xxxxxxxxx | 1[2-9]xxxxxxxxx }
```

**Accepts:**
- Emergency: `911`
- 7-digit local: `5551234`
- 10-digit: `2025551234`
- 11-digit: `12025551234`

**Use when:** Your area allows 7-digit local calls

---

### International Dial Plans

#### European Standard
```
{ 00xx. | [1-9]x+ | 112 | 110 }
```

**Accepts:**
- International: `00-...`
- National: Any number starting 1-9
- Emergency: `112` (Europe), `110` (Germany)

#### UK
```
{ 999 | 112 | 0[1-9]x+ | 00xx. }
```

**Accepts:**
- Emergency: `999`, `112`
- National: `0xxxx...`
- International: `00...`

#### Australia
```
{ 000 | 13xxxx | 1[38]xx | 0[2-9]xxxxxxxx | 0011xx. }
```

**Accepts:**
- Emergency: `000`
- Special services: `13xxxx`, `1300`, `1800`
- National: `0x-xxxx-xxxx`
- International: `0011...`

#### Canada (Same as USA)
```
{ [2-9]11 | 1[2-9]xxxxxxxxx | [2-9]xxxxxxxxx | 011xx. }
```

---

### Star Codes and Features

#### Common Star Codes
```
{ *xx | *67 | *69 | *70 | *72 | *73 }
```

**Common codes:**
- `*67` - Block caller ID
- `*69` - Call return (last caller)
- `*70` - Disable call waiting
- `*72` - Call forwarding activate
- `*73` - Call forwarding deactivate

#### Feature Codes with Numbers
```
{ *xx*x+ }
```

**Accepts:**
- `*21*5551234` - Call forwarding to number
- `*72*5551234` - Forward to number
- etc.

---

### International Calling

#### US International with +
```
{ \+x+ | 011xx. }
```

**Accepts:**
- `+12025551234` (international format)
- `01144...` (traditional US international)

#### Multiple International Prefixes
```
{ \+x+ | 011xx. | 00xx. }
```

**Accepts:**
- `+...` (international format)
- `011...` (US/Canada)
- `00...` (Europe)

---

## Advanced Routing

### Selective Routing by Prefix

Route local calls through PSTN, others through SIP:

```
# Use 'L' prefix to force PSTN routing
{ Lxxxxxxx | x+ }
```

**Usage:**
- Dial `L5551234` - Routes through FXO (PSTN)
- Dial `5551234` - Routes through SIP
- Dial `18005551234` - Routes through SIP

### Multiple Route Prefixes

```
# L = PSTN, S = SIP, I = International
{ Lxxxxxxx | S[2-9]xxxxxxxxx | I011xx. | x+ }
```

**Usage:**
- `L5551234` - Force PSTN
- `S2025551234` - Force SIP
- `I01144...` - Force international route
- Regular number - Default route

### Termination Character

Use `#` to dial immediately without timeout:

```
{ x+# }
```

**Usage:**
- User dials `5551234#`
- Calls immediately (no waiting for timeout)
- Useful for variable-length numbers

### Strip Digits

Remove digits before sending:

```
# Strip leading 1 from 11-digit numbers
{ <1>1[2-9]xxxxxxxxx }
```

**Result:**
- User dials: `12025551234`
- Sent to provider: `2025551234`

**Use when:** Provider doesn't accept leading 1

### Replace Digits

Replace prefix with different digits:

```
# Replace 9 with nothing (common for PBX)
{ <9>xx. }

# Replace 0 with 9 to get outside line
{ <0:9>xxxxxxxxxx }
```

---

## Country-Specific Dial Plans

### USA/Canada - Comprehensive
```
{
  [2-9]11 |                    # Emergency and services
  1[2-9]xxxxxxxxx |            # Long distance
  [2-9]xxxxxxxxx |             # 10-digit local
  011xx. |                     # International
  \+x+ |                       # International format
  1800xxxxxxx |                # Toll-free
  1888xxxxxxx |                # Toll-free
  1877xxxxxxx |                # Toll-free
  1866xxxxxxx |                # Toll-free
  *xx |                        # Star codes
  *xx*x+                       # Feature codes
}
```

### UK - Comprehensive
```
{
  999 |                        # Emergency
  112 |                        # Emergency (EU)
  0[1-9]x+ |                   # National numbers
  00xx. |                      # International
  \+x+ |                       # International format
  118xxx |                     # Directory services
  *xx                          # Star codes
}
```

### Germany - Comprehensive
```
{
  110 |                        # Police
  112 |                        # Emergency
  0[1-9]x+ |                   # National
  00xx. |                      # International
  \+x+ |                       # International format
  *xx                          # Feature codes
}
```

### Australia - Comprehensive
```
{
  000 |                        # Emergency
  112 |                        # Emergency (mobile)
  106 |                        # Text emergency
  13[123456]xxx |              # Local rate
  1[38]00xxx |                 # Toll-free
  0[2-9]xxxxxxxx |             # National
  0011xx. |                    # International
  \+x+ |                       # International format
  *xx                          # Feature codes
}
```

---

## Special Use Cases

### Allow Only Specific Numbers (Whitelist)

```
{ 911 | 5551234 | 5555678 | 18005551234 }
```

Only allows:
- Emergency: `911`
- Three specific numbers

**Use when:** Restricting to authorized numbers only

### Block Premium Rate Numbers (USA)

```
{ [2-9]11 | 1[2-9]xxxxxxxxx | [2-9]xxxxxxxxx }
# Specifically blocks 1-900 numbers by not including them
```

**Use when:** Preventing expensive calls

### Hotel/PBX Pattern

```
{
  <9>911 |                     # Strip 9, emergency
  <9>[2-9]xxxxxxxxx |          # Strip 9, local
  <9>1[2-9]xxxxxxxxx           # Strip 9, long distance
}
```

**Use when:** Must dial 9 for outside line

### Extension Dialing

```
{
  1xx |                        # 3-digit extensions (100-199)
  2xxx |                       # 4-digit extensions (2000-2999)
  [2-9]xxxxxxxxx               # External numbers
}
```

**Use when:** Integrated with PBX

---

## Testing Your Dial Plan

### Step 1: Test with Permissive Plan

Start with most permissive plan:
```
{ x+ }
```

Test that basic calling works.

### Step 2: Add Patterns Gradually

Add one pattern at a time:
```
{ 911 | x+ }              # Add emergency
{ 911 | \+x+ | x+ }       # Add international format
```

Test after each addition.

### Step 3: Remove Permissive Fallback

Once specific patterns work, remove `x+`:
```
{ 911 | [2-9]xxxxxxxxx | 1[2-9]xxxxxxxxx }
```

### Testing Checklist

Test these number types:
- [ ] Emergency numbers (911, 112, etc.)
- [ ] Local 7-digit (if applicable)
- [ ] Local 10-digit
- [ ] Long distance (1-xxx-xxx-xxxx)
- [ ] International (011... or 00...)
- [ ] International format (+...)
- [ ] Toll-free (1-800, 1-888, etc.)
- [ ] Star codes (*72, *67, etc.)
- [ ] Any custom patterns

---

## Common Mistakes

### Mistake 1: Missing Escape for +

**Wrong:**
```
{ +x+ }  # Won't work!
```

**Right:**
```
{ \+x+ }  # Escape the + sign
```

### Mistake 2: Forgetting Braces

**Wrong:**
```
x+ | \+x+  # Missing outer braces
```

**Right:**
```
{ x+ | \+x+ }
```

### Mistake 3: Too Restrictive

**Problem:**
```
{ xxxxxxx }  # Only exactly 7 digits
```

Can't dial 10 or 11 digit numbers!

**Better:**
```
{ xxxxxxx | xxxxxxxxxx | xxxxxxxxxxx }
# Or: { x+ }
```

### Mistake 4: Pattern Order Issues

When using strip/replace, order matters:

**Wrong:**
```
{ x+ | <1>1[2-9]xxxxxxxxx }  # x+ matches first!
```

**Right:**
```
{ <1>1[2-9]xxxxxxxxx | x+ }  # Specific pattern first
```

---

## Dial Plan Debugging

### Problem: Numbers Not Accepted

1. Temporarily use permissive plan: `{ x+ }`
2. If works, your plan is too restrictive
3. Add patterns one at a time to identify issue

### Problem: Wrong Route Taken

1. Check pattern order (most specific first)
2. Verify prefix patterns are correct
3. Test with dial plan tester if available

### Problem: Long Delay Before Dialing

1. Use interdigit timeout adjustment
2. Or add `#` termination to dial plan: `{ x+# }`
3. Reduce timeout values in settings

---

## Quick Reference

### Most Common Dial Plans

**USA - Flexible:**
```
{ x+ | \+x+ | *x+ }
```

**USA - Restricted:**
```
{ [2-9]11 | 1[2-9]xxxxxxxxx | [2-9]xxxxxxxxx | 011xx. }
```

**International:**
```
{ x+ | \+x+ | 00xx. | 011xx. }
```

**Maximum Flexibility:**
```
{ x+ }
```

---

## Need Help?

To get help with a custom dial plan, provide:

1. **Country/Region** - Affects numbering plan
2. **Types of calls** - Local, long distance, international
3. **Special requirements** - Extensions, routing, restrictions
4. **Example numbers** - What you need to dial

Example: *"I'm in the USA and need to dial 7-digit local (555-1234), 10-digit local (202-555-1234), long distance (1-202-555-1234), and international (011-44-...). I also want star codes like *67 and *69 to work."*

I'll create a custom dial plan for your needs!

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-02
