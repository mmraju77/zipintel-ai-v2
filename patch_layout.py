import re

with open('src/components/Layout.tsx', 'r') as f:
    content = f.read()

content = content.replace("import { Link, useLocation } from 'react-router-dom';", "import { Link, useLocation, useNavigate } from 'react-router-dom';")

new_state = """  const [isSidebarOpen, setIsSidebarOpen] = React.useState(true);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = React.useState(false);
  const [topSearch, setTopSearch] = React.useState('');
  const location = useLocation();
  const navigate = useNavigate();

  const handleTopSearch = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && topSearch.trim()) {
      const trimmed = topSearch.trim();
      if (/^\\d{5,6}$/.test(trimmed)) {
        const code = trimmed.length === 6 ? 'in' : 'us';
        const region = trimmed.length === 6 ? 'panderu' : 'california';
        navigate(`/zip/${code}/${region}/${trimmed}`);
      } else {
        navigate(`/?q=${encodeURIComponent(trimmed)}`);
      }
      setTopSearch('');
    }
  };
"""

content = content.replace("""  const [isSidebarOpen, setIsSidebarOpen] = React.useState(true);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = React.useState(false);
  const location = useLocation();""", new_state)

old_input = """              <input 
                type="text" 
                placeholder={t('searchPlaceholder')} 
                className="w-full bg-slate-900/50 border border-slate-800 rounded-xl py-3 pl-12 pr-12 text-base focus:outline-none focus:border-gold transition-all text-white placeholder-slate-500 shadow-inner"
              />
              <div className="absolute right-4 top-1/2 -translate-y-1/2 hidden md:block">
                <span className="bg-slate-800 text-sm px-2 py-1 rounded border border-slate-700 text-slate-400 uppercase tracking-tighter">⌘ K</span>
              </div>"""

new_input = """              <input 
                type="text" 
                value={topSearch}
                onChange={(e) => setTopSearch(e.target.value)}
                onKeyDown={handleTopSearch}
                placeholder={t('searchPlaceholder')} 
                className="w-full bg-slate-900/50 border border-slate-800 rounded-xl py-3 pl-12 pr-4 text-base focus:outline-none focus:border-gold transition-all text-white placeholder-slate-500 shadow-inner"
              />"""

content = content.replace(old_input, new_input)

with open('src/components/Layout.tsx', 'w') as f:
    f.write(content)
