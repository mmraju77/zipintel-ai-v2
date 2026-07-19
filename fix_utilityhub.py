import re

with open('src/components/UtilityHub.tsx', 'r') as f:
    content = f.read()

# Make the ROI cards larger
content = content.replace(
    'className="p-3 bg-slate-950 border border-slate-800/80 rounded-xl"',
    'className="p-6 bg-slate-950 border border-slate-800/80 rounded-xl min-h-[120px] flex flex-col justify-center"'
)
content = content.replace(
    'className="p-3 bg-slate-950 border border-slate-800/80 rounded-xl ring-1 ring-emerald-500/30"',
    'className="p-6 bg-slate-950 border border-slate-800/80 rounded-xl ring-1 ring-emerald-500/30 min-h-[120px] flex flex-col justify-center"'
)
content = content.replace(
    'className="p-3 bg-slate-950 border border-slate-800/80 rounded-xl bg-blue-950/20"',
    'className="p-6 bg-slate-950 border border-slate-800/80 rounded-xl bg-blue-950/20 min-h-[120px] flex flex-col justify-center"'
)

# Text size bumps
content = content.replace('text-sm uppercase font-mono', 'text-base uppercase font-mono')
content = content.replace('text-xl font-bold', 'text-2xl font-bold') # For the $ amounts in ROI

# QR generator box
content = content.replace(
    'className="flex flex-col items-center justify-center p-4 bg-slate-950 border border-slate-800 rounded-xl max-w-[220px] mx-auto"',
    'className="flex flex-col items-center justify-center p-6 bg-slate-950 border border-slate-800 rounded-xl max-w-[260px] mx-auto min-h-[200px]"'
)

with open('src/components/UtilityHub.tsx', 'w') as f:
    f.write(content)

