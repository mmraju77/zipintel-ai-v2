import re

def fix(file, bg_str, title, desc):
    with open(file, 'r') as f:
        content = f.read()

    # If <SEO doesn't exist, insert it
    if '<SEO' not in content:
        target = f'<div className="min-h-screen {bg_str}">'
        replacement = f'<>\n      <SEO title="{title}" description="{desc}" />\n      <div className="min-h-screen {bg_str}">'
        content = content.replace(target, replacement)
        
        # replace the last </div>
        idx = content.rfind("    </div>\n  );\n}")
        if idx != -1:
            content = content[:idx] + "    </div>\n    </>\n  );\n}"
    
    with open(file, 'w') as f:
        f.write(content)

fix('src/pages/AboutUs.tsx', 'bg-[#0B0F19] text-slate-300 py-12 px-6 font-sans', 'About Us - ZipIntel AI', 'Learn more about the ZipIntel AI project and our mission.')
fix('src/pages/Dashboard.tsx', 'bg-[#0B0F19] text-slate-300 p-6 font-sans', 'Dashboard - ZipIntel AI', 'Your personal dashboard for managing insights.')

def remove_unused(file, unused):
    with open(file, 'r') as f:
        content = f.read()
    
    for u in unused:
        content = re.sub(r'import\s+{\s*' + u + r'\s*}\s+from\s+[\'"]react-helmet-async[\'"];\n', '', content)
    
    with open(file, 'w') as f:
        f.write(content)

remove_unused('src/pages/Home.tsx', ['Helmet'])
remove_unused('src/pages/AIToolsPage.tsx', ['Helmet'])

