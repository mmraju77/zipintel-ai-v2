import re
import glob

replacements = {
    r'text-\[8px\]': 'text-[10px]',
    r'text-\[9px\]': 'text-[11px]',
    r'text-\[10px\]': 'text-xs',
    r'text-\[11px\]': 'text-sm',
    r'text-xs': 'text-sm',
    r'text-sm': 'text-base',
    r'text-base': 'text-lg',
    r'text-lg': 'text-xl',
    r'text-xl': 'text-2xl',
    r'text-2xl': 'text-3xl',
    r'text-3xl': 'text-4xl',
    r'text-4xl': 'text-5xl',
    r'text-5xl': 'text-6xl',
    r'text-6xl': 'text-7xl',
    r'text-7xl': 'text-8xl'
}

# Be careful not to replace text-4xl to text-5xl inside text-5xl etc.
# Using a compiled regex with word boundaries
# The keys with brackets need no \b at the end if they don't form word boundary, but they do form one usually.
# Let's just create a mega regex
regex_parts = []
for k in replacements.keys():
    if '[' in k:
        regex_parts.append(k)
    else:
        regex_parts.append(k + r'\b')

pattern = re.compile(r'(' + '|'.join(regex_parts) + r')')

def repl(match):
    val = match.group(0)
    # find the matching key
    for k, v in replacements.items():
        if re.match(k + r'(\b|$)', val):
            return v
    return val

tsx_files = glob.glob('src/pages/*.tsx') + glob.glob('src/components/*.tsx')

for file_path in tsx_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only want to replace inside className strings
    def string_repl(match):
        full_str = match.group(0)
        # perform replacement on the string contents
        return pattern.sub(repl, full_str)
        
    new_content = re.sub(r'"[^"]*"', string_repl, content)
    new_content = re.sub(r'`[^`]*`', string_repl, new_content)
    new_content = re.sub(r"'[^']*'", string_repl, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Upgraded {file_path}")

print("Done upgrading typography.")
