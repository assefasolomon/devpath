#!/usr/bin/env python3
"""
Safely convert Unicode subscripts/superscripts to HTML <sub>/<sup>
ONLY inside visible text, never inside HTML tags or scripts.
"""

import re
import sys
from pathlib import Path

# Unicode subscripts → HTML
SUB_MAP = {
    '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
    '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
    'ₐ': 'a', 'ₑ': 'e', 'ₕ': 'h', 'ᵢ': 'i', 'ⱼ': 'j',
    'ₖ': 'k', 'ₗ': 'l', 'ₘ': 'm', 'ₙ': 'n', 'ₒ': 'o',
    'ₚ': 'p', 'ᵣ': 'r', 'ₛ': 's', 'ₜ': 't', 'ᵤ': 'u',
    'ᵥ': 'v', 'ₓ': 'x',
    '₊': '+', '₋': '-', '₌': '=', '₍': '(', '₎': ')',
}

# Unicode superscripts → HTML
SUP_MAP = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
    'ⁿ': 'n', 'ⁱ': 'i',
    '⁺': '+', '⁻': '-', '⁼': '=', '⁽': '(', '⁾': ')',
}

SUB_CHARS = ''.join(SUB_MAP.keys())
SUP_CHARS = ''.join(SUP_MAP.keys())

def convert_text(text):
    """Convert subscripts and superscripts in a chunk of plain text."""
    # Replace a run of consecutive subscript chars with <sub>...</sub>
    def sub_repl(m):
        inner = ''.join(SUB_MAP[c] for c in m.group(0))
        return f'<sub>{inner}</sub>'

    def sup_repl(m):
        inner = ''.join(SUP_MAP[c] for c in m.group(0))
        return f'<sup>{inner}</sup>'

    text = re.sub(f'[{re.escape(SUB_CHARS)}]+', sub_repl, text)
    text = re.sub(f'[{re.escape(SUP_CHARS)}]+', sup_repl, text)
    return text

def process_html(html):
    """
    Process only TEXT content between tags.
    Skip <script>, <style>, and anything inside <...>.
    """
    result = []
    i = 0
    in_script = False
    in_style = False
    n = len(html)

    while i < n:
        # Check for tag start
        if html[i] == '<':
            # Find end of tag
            end = html.find('>', i)
            if end == -1:
                result.append(html[i:])
                break
            tag = html[i:end+1]
            tag_lower = tag.lower()

            # Track script/style blocks
            if tag_lower.startswith('<script'):
                in_script = True
            elif tag_lower.startswith('</script'):
                in_script = False
            elif tag_lower.startswith('<style'):
                in_style = True
            elif tag_lower.startswith('</style'):
                in_style = False

            # Emit tag as-is (never convert inside tags)
            result.append(tag)
            i = end + 1
            continue

        # Find next tag start
        next_tag = html.find('<', i)
        if next_tag == -1:
            next_tag = n

        # Text chunk between tags
        text = html[i:next_tag]

        # Only convert if we're not inside script/style
        if not in_script and not in_style:
            text = convert_text(text)

        result.append(text)
        i = next_tag

    return ''.join(result)


def process_file(path):
    try:
        original = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f'  SKIP (not UTF-8): {path}')
        return False

    # Quick check: does the file contain any target chars?
    has_sub = any(c in original for c in SUB_CHARS)
    has_sup = any(c in original for c in SUP_CHARS)
    if not has_sub and not has_sup:
        return False

    # Backup once
    backup = path.with_suffix(path.suffix + '.bak')
    if not backup.exists():
        backup.write_text(original, encoding='utf-8')

    converted = process_html(original)

    if converted != original:
        path.write_text(converted, encoding='utf-8')
        return True
    return False


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    targets = list(root.rglob('*/lessons/*.html'))

    print(f'Found {len(targets)} lesson files')
    converted_count = 0

    for path in targets:
        if process_file(path):
            print(f'  ✓ Fixed: {path}')
            converted_count += 1

    print(f'\n✅ Done. {converted_count} files converted.')


if __name__ == '__main__':
    main()
