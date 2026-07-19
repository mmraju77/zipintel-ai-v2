import re

with open('src/components/InfrastructureInsights.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    "const zip = (zipCode || '530001').trim();",
    "const zip = zipCode ? zipCode.trim() : 'REGIONAL';"
)

with open('src/components/InfrastructureInsights.tsx', 'w') as f:
    f.write(content)
