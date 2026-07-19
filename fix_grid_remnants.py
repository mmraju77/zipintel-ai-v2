import re

with open('src/pages/CountryPage.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    '<div className="w-full max-w-[1920px] mx-auto grid md:grid-cols-3 gap-6">\n        \n        {/* Card 1 & 2: Local Node Metadata (SEO Rich Text Content) */}\n        <div className="md:col-span-2 space-y-6">',
    '<div className="w-full max-w-[1920px] mx-auto">\n        \n        {/* Card 1 & 2: Local Node Metadata (SEO Rich Text Content) */}\n        <div className="w-full space-y-6">'
)

content = content.replace(
    '<div className="w-full max-w-[1920px] mx-auto grid md:grid-cols-3 gap-6 mt-6">\n        <div className="md:col-span-3">',
    '<div className="w-full max-w-[1920px] mx-auto mt-6">\n        <div className="w-full">'
)

with open('src/pages/CountryPage.tsx', 'w') as f:
    f.write(content)

