import re

with open('src/pages/CountryPage.tsx', 'r') as f:
    content = f.read()

# 1. Update currentZip parsing
content = content.replace(
    "const currentZip = (zipCode || l3 || l2 || l1 || '530001').trim();",
    "const rawZip = (zipCode || l3 || l2 || l1);\n  const currentZip = rawZip ? rawZip.trim() : undefined;"
)

# 2. Update getSEOMeta
old_seo = """  const getSEOMeta = () => {
    const countryNames: Record<string, string> = {
      in: "India (భారతదేశం)", usa: "United States", uk: "United Kingdom",
      gb: "United Kingdom", ca: "Canada", au: "Australia", de: "Germany", fr: "France"
    };
    const name = countryNames[currentCountry] || currentCountry.toUpperCase();
    return {
      title: `${name} Postal Code ${currentZip} - Global Financial Intelligence Hub`,
      description: `Verify financial routing metrics, active clearing node structures, and structural infrastructure values for region node ${currentZip} in ${name}. Powered by ZipIntel AI.`
    };
  };"""

new_seo = """  const getSEOMeta = () => {
    const countryNames: Record<string, string> = {
      in: "India (భారతదేశం)", usa: "United States", uk: "United Kingdom",
      gb: "United Kingdom", ca: "Canada", au: "Australia", de: "Germany", fr: "France"
    };
    const name = countryNames[currentCountry] || currentCountry.toUpperCase();
    if (currentZip) {
      return {
        title: `${name} Postal Code ${currentZip} - Global Financial Intelligence Hub`,
        description: `Verify financial routing metrics, active clearing node structures, and structural infrastructure values for region node ${currentZip} in ${name}. Powered by ZipIntel AI.`
      };
    } else {
      return {
        title: `${name} Regional Directory - Global Financial Intelligence Hub`,
        description: `Verify financial routing metrics, active clearing node structures, and structural infrastructure values for ${name}. Powered by ZipIntel AI.`
      };
    }
  };"""

content = content.replace(old_seo, new_seo)

# 3. Update breadcrumbs
old_breadcrumbs = """      {/* Breadcrumb Navigation - Search Crawlers కి చాలా ముఖ్యం */}
      <div className="w-full max-w-[1920px] mx-auto mb-6 text-sm font-mono flex items-center gap-2 text-slate-100">
        <Link to="/" className="hover:text-blue-300 transition-colors">Home</Link>
        <span>/</span>
        <span className="uppercase text-slate-100">{currentCountry}</span>
        <span>/</span>
        <span className="text-emerald-300">{currentZip}</span>
      </div>"""

new_breadcrumbs = """      {/* Breadcrumb Navigation - Search Crawlers కి చాలా ముఖ్యం */}
      <div className="w-full max-w-[1920px] mx-auto mb-6 text-sm font-mono flex items-center gap-2 text-slate-100">
        <Link to="/" className="hover:text-blue-300 transition-colors">Home</Link>
        <span>/</span>
        <span className="uppercase text-slate-100">{currentCountry}</span>
        {currentZip && (
          <>
            <span>/</span>
            <span className="text-emerald-300">{currentZip}</span>
          </>
        )}
      </div>"""

content = content.replace(old_breadcrumbs, new_breadcrumbs)

# 4. Update Header
old_header = """            <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold text-white tracking-tight mt-3">
              Target Infrastructure: <span className="text-blue-300 font-mono">{currentZip}</span>
            </h1>"""

new_header = """            <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold text-white tracking-tight mt-3">
              Target Infrastructure: <span className="text-blue-300 font-mono">{currentZip ? currentZip : currentCountry.toUpperCase()}</span>
            </h1>"""

content = content.replace(old_header, new_header)

with open('src/pages/CountryPage.tsx', 'w') as f:
    f.write(content)
