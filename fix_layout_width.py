with open('src/components/Layout.tsx', 'r') as f:
    content = f.read()

content = content.replace('className="max-w-7xl mx-auto p-4 md:p-8"', 'className="w-full max-w-[1920px] mx-auto p-4 md:px-8"')

with open('src/components/Layout.tsx', 'w') as f:
    f.write(content)

