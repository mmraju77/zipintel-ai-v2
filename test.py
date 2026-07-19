import re
replacements = {
    r'text-\[10px\]': 'text-xs',
    r'text-xs': 'text-sm'
}
regex_parts = [r'text-\[10px\]', r'text-xs\b']
pattern = re.compile(r'(?<!-)\b(' + '|'.join(regex_parts) + r')')

def repl(match):
    val = match.group(0)
    for k, v in replacements.items():
        if re.match(r'^' + k + r'(\b|$)', val):
            return v
    return val

content = '"text-[10px]"'
def string_repl(match):
    full_str = match.group(0)
    return pattern.sub(repl, full_str)

new_content = re.sub(r'"[^"]*"', string_repl, content)
new_content = re.sub(r'`[^`]*`', string_repl, new_content)
new_content = re.sub(r"'[^']*'", string_repl, new_content)

print(new_content)
