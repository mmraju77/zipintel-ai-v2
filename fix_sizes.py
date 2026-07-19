import os
import re
import glob

js_files = glob.glob('dist/assets/*.js')
with open(js_files[0], 'r', encoding='utf-8') as f:
    js_content = f.read()

size_classes = [
    r'text-\[8px\]', r'text-\[9px\]', r'text-\[10px\]', r'text-\[11px\]',
    r'text-xs', r'text-sm', r'text-base', r'text-lg', r'text-xl',
    r'text-2xl', r'text-3xl', r'text-4xl', r'text-5xl', r'text-6xl',
    r'text-7xl', r'text-8xl', r'text-9xl'
]

# We don't really need to match the whole string exact spacing because Vite removes some spaces.
# It's better to just extract the original class by doing a git diff if possible, but we don't have git.

# Alternative approach: we know what classes were replaced.
# We can just look for the class list in the JS file using a simplified regex.
def get_original_class(corrupted_str):
    if 'text-6xl' not in corrupted_str:
        return corrupted_str
        
    parts = corrupted_str.split('text-6xl')
    escaped_parts = [re.escape(p) for p in parts]
    regex_pattern = r'(text-(?:\[\d+px\]|xs|sm|base|lg|xl|\dxl))'.join(escaped_parts)
    
    # allow flexible whitespace
    regex_pattern = regex_pattern.replace(r'\ ', r'\s+')
    
    matches = re.findall(regex_pattern, js_content)
    if matches:
        # matches will be the captured group, which is the original text size class!
        # If there are multiple text-6xl in the string, matches will be a tuple.
        if isinstance(matches[0], tuple):
            orig_classes = matches[0]
            res = corrupted_str
            for orig in orig_classes:
                res = res.replace('text-6xl', orig, 1)
            return res
        else:
            return corrupted_str.replace('text-6xl', matches[0], 1)
            
    return corrupted_str

tsx_files = glob.glob('src/pages/*.tsx') + glob.glob('src/components/*.tsx')

for file_path in tsx_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def replace_func(match):
        full_str = match.group(1)
        orig = get_original_class(full_str)
        return f'"{orig}"'
        
    def replace_func_backtick(match):
        full_str = match.group(1)
        orig = get_original_class(full_str)
        return f'`{orig}`'

    new_content = re.sub(r'"([^"]*text-6xl[^"]*)"', replace_func, content)
    new_content = re.sub(r'`([^`]*text-6xl[^`]*)`', replace_func_backtick, new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")

print("Done restoring from dist.")
