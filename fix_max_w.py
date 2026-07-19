import re

with open('src/pages/CountryPage.tsx', 'r') as f:
    content = f.read()

content = content.replace('max-w-5xl mx-auto', 'w-full max-w-[1920px] mx-auto')

# Also the layout might have padding in main? Let's check Layout.tsx
with open('src/components/Layout.tsx', 'r') as f:
    layout_content = f.read()

# Just in case, let's see if Layout.tsx restricts width
with open('src/pages/CountryPage.tsx', 'w') as f:
    f.write(content)

