import os
import re

replacements = {
    r'text-slate-400': 'text-slate-100',
    r'text-slate-500': 'text-slate-200',
    r'text-slate-600': 'text-slate-200',
    r'text-gray-400': 'text-slate-100',
    r'text-gray-500': 'text-slate-200',
    r'text-emerald-600': 'text-emerald-300',
    r'text-emerald-500': 'text-emerald-300',
    r'text-emerald-400': 'text-emerald-300',
    r'text-blue-600': 'text-blue-300',
    r'text-blue-500': 'text-blue-300',
    r'text-blue-400': 'text-blue-300',
    r'text-indigo-500': 'text-indigo-300',
    r'text-indigo-400': 'text-indigo-300',
    r'placeholder-slate-500': 'placeholder-slate-300',
    r'placeholder:text-slate-600': 'placeholder:text-slate-300',
    r'text-\[7px\]': 'text-xs',
    r'text-\[10px\]': 'text-xs',
}

def process_file(filepath):
    if not filepath.endswith('.tsx') and not filepath.endswith('.ts'):
        return
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in replacements.items():
        new_content = re.sub(pattern, replacement, new_content)
        
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

for root, dirs, files in os.walk('src'):
    for file in files:
        process_file(os.path.join(root, file))

