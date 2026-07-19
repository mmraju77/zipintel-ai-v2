import re

with open('src/components/InfrastructureInsights.tsx', 'r') as f:
    content = f.read()

# Replace main container
content = content.replace(
    'className="flex flex-wrap gap-6 mt-8 w-full"',
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-8 w-full"'
)

# Remove flex-1 and min-w-[200px] from the cards, keep overflow-hidden if it helps
content = content.replace(
    'className="flex-1 p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group min-w-[200px] overflow-hidden"',
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group overflow-hidden"'
)

content = content.replace(
    'className="flex-1 p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group relative overflow-hidden min-w-[200px]"',
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group relative overflow-hidden"'
)

with open('src/components/InfrastructureInsights.tsx', 'w') as f:
    f.write(content)
