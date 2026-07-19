import re

with open('src/pages/CountryPage.tsx', 'r') as f:
    content = f.read()

if 'AdPlaceholder' not in content:
    content = content.replace("import { CommunityLayer } from '../components/CommunityLayer';", "import { CommunityLayer } from '../components/CommunityLayer';\nimport { AdPlaceholder } from '../components/AdPlaceholder';")

ad_block = """      <div className="w-full max-w-[1920px] mx-auto mt-6">
        <AdPlaceholder format="banner" />
      </div>
      
      <div className="w-full max-w-[1920px] mx-auto mt-2">
        <CommunityLayer />"""

content = content.replace("""      <div className="w-full max-w-[1920px] mx-auto mt-2">
        <CommunityLayer />""", ad_block)

with open('src/pages/CountryPage.tsx', 'w') as f:
    f.write(content)
