import re
import glob
import itertools

js_files = glob.glob('dist/assets/*.js')
with open(js_files[0], 'r', encoding='utf-8') as f:
    js_content = f.read()

size_classes = [
    r'text-\[8px\]', r'text-\[9px\]', r'text-\[10px\]', r'text-\[11px\]',
    r'text-xs', r'text-sm', r'text-base', r'text-lg', r'text-xl',
    r'text-2xl', r'text-3xl', r'text-4xl', r'text-5xl', r'text-6xl',
    r'text-7xl', r'text-8xl', r'text-9xl'
]

size_regex_str = r'text-(?:\[\d+px\]|xs|sm|base|lg|xl|\dxl)'

def get_original_class(corrupted_str):
    # Remove all size classes from the corrupted string to form a template
    template_parts = re.split(size_regex_str, corrupted_str)
    
    if len(template_parts) == 1:
        return corrupted_str # no size classes
        
    escaped_parts = [re.escape(p) for p in template_parts]
    # Rebuild regex that matches the template with ANY size classes in the holes
    regex_pattern = f'({size_regex_str})'.join(escaped_parts)
    
    # allow flexible whitespace
    regex_pattern = regex_pattern.replace(r'\ ', r'\s+')
    
    matches = re.findall(regex_pattern, js_content)
    if matches:
        if isinstance(matches[0], tuple):
            orig_classes = matches[0]
            res = corrupted_str
            for orig in orig_classes:
                res = re.sub(size_regex_str, orig, res, count=1)
            return res
        else:
            return re.sub(size_regex_str, matches[0], corrupted_str, count=1)
            
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

    new_content = re.sub(r'"([^"]*text-[^"]*)"', replace_func, content)
    new_content = re.sub(r'`([^`]*text-[^`]*)`', replace_func_backtick, new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")

print("Done restoring from dist.")
