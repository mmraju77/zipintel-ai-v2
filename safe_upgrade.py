import re
import glob

replacements = {
    r'text-\[8px\]': 'text-[10px]',
    r'text-\[9px\]': 'text-[10px]',
    r'text-\[10px\]': 'text-xs',
    r'text-\[11px\]': 'text-xs',
    r'text-xs': 'text-sm',
    r'text-sm': 'text-base',
    # For now, let's also increase base to lg, and lg to xl, but carefully
    r'text-base': 'text-lg',
    r'text-lg': 'text-xl',
}

regex_parts = []
for k in replacements.keys():
    if '[' in k:
        regex_parts.append(k)
    else:
        regex_parts.append(k + r'\b')

pattern = re.compile(r'(?<!-)\b(' + '|'.join(regex_parts) + r')')

def repl(match):
    val = match.group(0)
    for k, v in replacements.items():
        if re.match(r'^' + k + r'(\b|$)', val):
            return v
    return val

tsx_files = glob.glob('src/pages/*.tsx') + glob.glob('src/components/*.tsx')

for file_path in tsx_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def string_repl(match):
        full_str = match.group(0)
        return pattern.sub(repl, full_str)
        
    new_content = re.sub(r'"[^"]*"', string_repl, content)
    new_content = re.sub(r'`[^`]*`', string_repl, new_content)
    new_content = re.sub(r"'[^']*'", string_repl, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Upgraded {file_path}")

print("Done upgrading small typography.")
