import os
import re

def process_file(filepath):
    if not filepath.endswith('.tsx') and not filepath.endswith('.ts'):
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content
    
    # 1. Global Contrast
    replacements_contrast = {
        r'text-slate-400': 'text-slate-100',
        r'text-slate-500': 'text-slate-200',
        r'text-slate-600': 'text-slate-200',
        r'text-gray-400': 'text-slate-100',
        r'text-gray-500': 'text-slate-200',
        r'text-gray-600': 'text-slate-200',
    }
    for old, new in replacements_contrast.items():
        new_content = re.sub(old, new, new_content)

    # 2. Typography Sizing
    # Be careful not to replace text-sm inside text-sm: hover:text-sm etc. We can do simple word replacements.
    # text-xs -> text-sm
    new_content = re.sub(r'\btext-xs\b', 'text-sm', new_content)
    # Actually wait, if we do text-sm -> text-base, we'll overwrite the ones we just made text-sm.
    # Let's do it in two passes safely or use a regex callback.
    
    # For padding: p-3, p-4, p-5 -> p-6 in card classes.
    # Let's just do a basic replace for specific cards.
    # We will do this manually for important components.
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

for root, dirs, files in os.walk('src'):
    for file in files:
        process_file(os.path.join(root, file))

