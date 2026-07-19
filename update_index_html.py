import re

with open('index.html', 'r') as f:
    content = f.read()

old_link = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet" />'
new_link = """<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" as="style" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" media="print" onload="this.media='all'" />
    <noscript>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" />
    </noscript>"""

if old_link in content:
    content = content.replace(old_link, new_link)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Updated index.html")
else:
    print("Could not find the link to replace.")
