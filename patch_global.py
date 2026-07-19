import re

with open('src/components/GlobalSearch.tsx', 'r') as f:
    content = f.read()

content = content.replace("import { useNavigate } from 'react-router-dom';", "import { useNavigate, useSearchParams } from 'react-router-dom';")

new_effect = """  const [searchParams] = useSearchParams();

  useEffect(() => {
    const q = searchParams.get('q');
    if (q) {
      handleSearch(q);
    }
  }, [searchParams]);

  useEffect(() => {"""

content = content.replace("  useEffect(() => {", new_effect, 1)

with open('src/components/GlobalSearch.tsx', 'w') as f:
    f.write(content)
