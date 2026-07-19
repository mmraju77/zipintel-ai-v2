import re

with open('src/components/InfrastructureInsights.tsx', 'r') as f:
    content = f.read()

# Replace main grid container with flex flex-wrap
content = content.replace(
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-6 mt-8"',
    'className="flex flex-wrap gap-6 mt-8 w-full"'
)

# Add flex-1 to each card so it stretches nicely
content = content.replace(
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group min-w-[200px] overflow-hidden"',
    'className="flex-1 p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group min-w-[200px] overflow-hidden"'
)

content = content.replace(
    'className="p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group relative overflow-hidden min-w-[200px]"',
    'className="flex-1 p-6 rounded-3xl bg-slate-900 border border-slate-800 hover:border-gold/30 transition-all group relative overflow-hidden min-w-[200px]"'
)

with open('src/components/InfrastructureInsights.tsx', 'w') as f:
    f.write(content)
