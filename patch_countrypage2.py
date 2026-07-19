import re

with open('src/pages/CountryPage.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'districtId={currentZip}',
    'districtId={currentZip || \'\'}'
)

with open('src/pages/CountryPage.tsx', 'w') as f:
    f.write(content)
