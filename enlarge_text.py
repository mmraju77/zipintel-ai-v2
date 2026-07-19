import re

with open('src/components/InfrastructureInsights.tsx', 'r') as f:
    content = f.read()

# Replace text-xs with text-sm
content = content.replace('text-xs font-black', 'text-sm font-black')
content = content.replace('text-xs font-bold', 'text-sm font-bold')

# Replace text-xl with text-2xl
content = content.replace('text-xl font-black', 'text-2xl font-black')

# For the tiny text text-[7px], maybe make it text-[10px] or text-xs
content = content.replace('text-[7px]', 'text-[10px]')

with open('src/components/InfrastructureInsights.tsx', 'w') as f:
    f.write(content)

