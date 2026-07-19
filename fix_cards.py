import re

with open('src/components/InfrastructureInsights.tsx', 'r') as f:
    content = f.read()

# Replace main grid container
content = content.replace(
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4 mt-8"',
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-6 mt-8"'
)

# Add min-w-[200px] overflow-hidden to each motion.div card
content = content.replace(
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group"',
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group min-w-[200px] overflow-hidden"'
)

content = content.replace(
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group relative overflow-hidden"',
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group relative overflow-hidden min-w-[200px]"'
)

with open('src/components/InfrastructureInsights.tsx', 'w') as f:
    f.write(content)

