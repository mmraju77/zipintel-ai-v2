import re

def update_headings(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find h1, h2, h3 tags and replace text-white with text-yellow-400
    # Also find text-3xl, text-4xl, text-5xl and replace text-white with text-yellow-400
    
    # 1. Replace text-white with text-yellow-400 inside heading tags
    # It's easier to just use regex for text-white -> text-yellow-400 where <h1, <h2 are present.
    # We will do a generic approach: find className="..." and if it contains text-3xl, 4xl, 5xl, or it's inside <h1 / <h2, change text-white to text-yellow-400
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if '<h1' in line or '<h2' in line or 'text-3xl' in line or 'text-4xl' in line or 'text-5xl' in line:
            lines[i] = line.replace('text-white', 'text-yellow-400')
    
    # Also, some other metrics are large. Let's just do text-yellow-400 for primary metrics.
    # In Home.tsx, there's "14ms". Let's check for it.
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))

for file in ['src/pages/Home.tsx', 'src/pages/CountryPage.tsx', 'src/pages/Dashboard.tsx', 'src/pages/AboutUs.tsx', 'src/pages/AIToolsPage.tsx', 'src/components/InfrastructureInsights.tsx', 'src/components/UtilityHub.tsx']:
    import os
    if os.path.exists(file):
        update_headings(file)

