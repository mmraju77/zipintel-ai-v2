with open('src/components/GlobalSearch.tsx', 'r') as f:
    content = f.read()

# We can remove the searchParams useEffect and put it after handleSearch
target = """  const [searchParams] = useSearchParams();

  useEffect(() => {
    const q = searchParams.get('q');
    if (q) {
      handleSearch(q);
    }
  }, [searchParams]);"""

content = content.replace(target, "  const [searchParams] = useSearchParams();")

target2 = "  const handleSelect = useCallback((result: SearchResult) => {"
new_effect = """
  useEffect(() => {
    const q = searchParams.get('q');
    if (q) {
      handleSearch(q);
    }
  }, [searchParams, handleSearch]);

  const handleSelect = useCallback((result: SearchResult) => {"""

content = content.replace(target2, new_effect)

with open('src/components/GlobalSearch.tsx', 'w') as f:
    f.write(content)
