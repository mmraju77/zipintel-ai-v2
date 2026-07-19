import re

with open('src/components/MonetizationNodes.tsx', 'r') as f:
    content = f.read()

content = content.replace('text-white', 'text-yellow-400')

with open('src/components/MonetizationNodes.tsx', 'w') as f:
    f.write(content)
