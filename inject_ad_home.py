import re

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

# Add import
if 'AdPlaceholder' not in content:
    content = content.replace("import { MonetizationNodes } from '../components/MonetizationNodes';", "import { MonetizationNodes } from '../components/MonetizationNodes';\nimport { AdPlaceholder } from '../components/AdPlaceholder';")

# Add placeholder before Intelligence Bento
ad_block = """      <div className="w-full py-4">
        <AdPlaceholder format="banner" />
      </div>
      
      {/* Intelligence Bento */}"""

content = content.replace('{/* Intelligence Bento */}', ad_block)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)

