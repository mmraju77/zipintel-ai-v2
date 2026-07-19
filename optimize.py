import re
import glob

def remove_unused(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    if "api/index.ts" in file_path:
        content = re.sub(r'\(req: Request', r'(_req: Request', content)
        content = re.sub(r'\(req, res\)', r'(_req, res)', content)

    if "server.ts" in file_path:
        content = re.sub(r'\(req, res\)', r'(_req, res)', content)

    if "AILocalGuide.tsx" in file_path:
        content = re.sub(r',\s*Radio', '', content)
        content = re.sub(r'const { countryId } = ', r'const {  } = ', content)
        content = re.sub(r'const { t } = useI18n\(\);', '', content)

    if "AffiliateWidgets.tsx" in file_path:
        content = re.sub(r',\s*Globe', '', content)
        content = re.sub(r',\s*Sparkles', '', content)

    if "GeoRadar.tsx" in file_path:
        content = re.sub(r"import \{ Target \} from 'lucide-react';\n", '', content)
        content = re.sub(r"const \{ t \} = useI18n\(\);\n", '', content)

    if "GlobalSearch.tsx" in file_path:
        content = re.sub(r"import \{ POSTAL_DATA \} from '\.\./data/postalData';\n", '', content)
        content = re.sub(r"\{ POSTAL_DATA \}", "{ }", content)

    if "InfrastructureInsights.tsx" in file_path:
        content = re.sub(r"import \{ useParams \} from 'react-router-dom';\n", '', content)

    if "Layout.tsx" in file_path:
        content = re.sub(r',\s*Database', '', content)

    if "PDFReport.tsx" in file_path:
        content = re.sub(r',\s*Printer', '', content)
        content = re.sub(r'const \{ .*? \} = \w+; // unused', '', content)

    if "SEOAutomation.tsx" in file_path:
        pass # Handle later

    if "AIToolsPage.tsx" in file_path:
        content = re.sub(r',\s*AnimatePresence', '', content)
        content = re.sub(r',\s*ArrowLeft', '', content)
        content = re.sub(r',\s*Cpu', '', content)
        content = re.sub(r',\s*Shield', '', content)
        content = re.sub(r"import \{ Link \} from 'react-router-dom';\n", '', content)

    if "AboutUs.tsx" in file_path:
        content = re.sub(r',\s*ExternalLink', '', content)

    if "CountryPage.tsx" in file_path:
        pass # Handle later

    if "Home.tsx" in file_path:
        content = re.sub(r'Globe,\s*Shield,\s*Cpu,\s*', '', content)
        content = re.sub(r'Target,\s*', '', content)
        content = re.sub(r'Loader2,\s*', '', content)
        content = re.sub(r"import \{ POSTAL_DATA \} from '\.\./data/postalData';\n", '', content)
        content = re.sub(r"const \[searchResults, setSearchResults\] = useState<SearchResult\[\]>\(\[\]\);\n", '', content)
        content = re.sub(r"const \[isSearching, setIsSearching\] = useState\(false\);\n", '', content)
        content = re.sub(r"const \[searchError, setSearchError\] = useState<string \| null>\(null\);\n", '', content)

    if "vite.config.ts" in file_path:
        content = re.sub(r'\(\{\s*mode,\s*command,\s*env\s*\}\)', r'({ mode, command })', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {file_path}")

files = glob.glob('src/**/*.tsx', recursive=True) + glob.glob('api/*.ts') + glob.glob('*.ts')
for f in files:
    remove_unused(f)
print("Optimization pass 1 done.")
