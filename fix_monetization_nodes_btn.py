import re

with open('src/components/MonetizationNodes.tsx', 'r') as f:
    content = f.read()

# Fix buttons back to text-white or keep text-yellow-400? Button text can be white for better contrast or something dark.
content = content.replace('hover:bg-blue-500 text-yellow-400', 'hover:bg-blue-500 text-white')
content = content.replace('hover:bg-emerald-500 text-yellow-400', 'hover:bg-emerald-500 text-white')

with open('src/components/MonetizationNodes.tsx', 'w') as f:
    f.write(content)
