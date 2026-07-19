import os
import re

def process_file(filepath):
    if not filepath.endswith('.tsx') and not filepath.endswith('.ts'):
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content
    
    # Let's upgrade font sizes in specific contexts for better readability
    
    # 1. Update TrustFooter
    if 'TrustFooter' in filepath:
        new_content = new_content.replace('text-sm', 'text-base')
        new_content = new_content.replace('text-xs', 'text-sm')
        new_content = new_content.replace('max-w-sm', 'max-w-xl')

    # 2. Update InfrastructureInsights cards
    if 'InfrastructureInsights' in filepath:
        # Increase text size inside these cards
        new_content = new_content.replace('text-xs font-black', 'text-sm font-black')
        new_content = new_content.replace('text-xs font-bold', 'text-sm font-bold')
        new_content = new_content.replace('text-[10px]', 'text-xs')
        # Padding increase
        new_content = new_content.replace('p-6 rounded-3xl', 'p-8 rounded-3xl')

    # 3. Update CommunityLayer posts
    if 'CommunityLayer' in filepath:
        new_content = new_content.replace('text-sm text-slate-100', 'text-base text-slate-100')
        new_content = new_content.replace('text-xs text-slate-200', 'text-sm text-slate-100')
        new_content = new_content.replace('text-xs text-slate-100', 'text-sm text-slate-100')
        new_content = new_content.replace('p-4', 'p-6')
        
    # 4. Update MonetizationNodes
    if 'MonetizationNodes' in filepath:
        new_content = new_content.replace('text-sm', 'text-base')
        new_content = new_content.replace('text-xs', 'text-sm')
        new_content = new_content.replace('p-4', 'p-6')
        new_content = new_content.replace('p-5', 'p-6')

    # 5. Update DirectoryView (global directories)
    if 'DirectoryView' in filepath:
        new_content = new_content.replace('text-sm', 'text-base')
        new_content = new_content.replace('text-xs', 'text-sm')
        new_content = new_content.replace('p-5', 'p-6 md:p-8')
        
    # 6. Update CountryPage
    if 'CountryPage' in filepath:
        new_content = new_content.replace('text-sm', 'text-base')
        new_content = new_content.replace('p-6 bg-slate-900', 'p-8 bg-slate-900')

    # 7. Update Home
    if 'Home' in filepath:
        new_content = new_content.replace('text-sm text-slate-100', 'text-base text-slate-100')
        new_content = new_content.replace('text-xs', 'text-sm')

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

for root, dirs, files in os.walk('src'):
    for file in files:
        process_file(os.path.join(root, file))

