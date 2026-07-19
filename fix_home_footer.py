import re

with open('src/pages/Home.tsx', 'r') as f:
    home_content = f.read()

# 1. Enlarge Cards (Country cards)
# Find the glass-card p-5 group flex... and replace with p-6 md:p-8 min-h-[120px]
home_content = home_content.replace(
    'className="glass-card p-5 group flex items-start gap-4 hardware-accelerated border-slate-800 hover:border-gold/30 transition-all"',
    'className="glass-card p-6 md:p-8 min-h-[140px] group flex items-start gap-5 hardware-accelerated border-slate-800 hover:border-gold/30 transition-all"'
)
# Update text size in country descriptions
home_content = home_content.replace(
    '<p className="text-sm text-slate-100 font-bold uppercase tracking-tighter leading-tight truncate mt-0.5">',
    '<p className="text-base text-slate-100 font-bold uppercase tracking-tighter leading-tight truncate mt-1">'
)

# 2. Recent rewrites text size
home_content = home_content.replace(
    '<div className="flex justify-between text-sm py-1 border-b border-slate-800/50">',
    '<div className="flex justify-between text-base py-2 border-b border-slate-800/50">'
)
# And the header for recent rewrites
home_content = home_content.replace(
    '<span className="text-sm text-slate-100 uppercase font-black tracking-widest">{t(\'recentRewrites\')}</span>',
    '<span className="text-base text-slate-100 uppercase font-black tracking-widest">{t(\'recentRewrites\')}</span>'
)
# And live status
home_content = home_content.replace(
    '<span className="text-sm text-emerald-300 font-bold uppercase">{t(\'liveStatus\')}</span>',
    '<span className="text-base text-emerald-300 font-bold uppercase">{t(\'liveStatus\')}</span>'
)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(home_content)

# 3. Footer fixes
with open('src/components/TrustFooter.tsx', 'r') as f:
    footer = f.read()

# text-sm -> text-base for descriptions
footer = footer.replace('text-sm text-slate-100 leading-relaxed max-w-sm', 'text-base text-slate-100 leading-relaxed max-w-sm')

# headers
footer = footer.replace('text-sm font-mono uppercase tracking-widest', 'text-base font-mono uppercase tracking-widest')
footer = footer.replace('text-sm font-mono uppercase tracking-[0.2em]', 'text-base font-mono uppercase tracking-[0.2em]')

# lists
footer = footer.replace('<ul className="space-y-2 text-sm font-mono">', '<ul className="space-y-2 text-base font-mono">')

# System Authority badges
footer = footer.replace('text-sm font-mono text-emerald-300', 'text-base font-mono text-emerald-300')
footer = footer.replace('text-sm font-mono text-blue-300', 'text-base font-mono text-blue-300')
footer = footer.replace('text-sm font-mono text-slate-100 bg-slate-800/50', 'text-base font-mono text-slate-100 bg-slate-800/50')

# Regulatory disclosure text
footer = footer.replace('text-xs font-mono leading-relaxed', 'text-sm font-mono leading-relaxed')

# Bottom text
footer = footer.replace('text-sm font-mono text-slate-200', 'text-base font-mono text-slate-100')
footer = footer.replace('text-slate-200', 'text-slate-100') # Ensure no muted text

with open('src/components/TrustFooter.tsx', 'w') as f:
    f.write(footer)

