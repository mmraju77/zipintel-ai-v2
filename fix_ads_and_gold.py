import os
import re

# 1. Update index.css to make gold actually gold (#FFD700)
with open('src/index.css', 'r') as f:
    css = f.read()
css = re.sub(r'--color-gold:\s*#[a-zA-Z0-9]+;', '--color-gold: #FFD700;', css)
css = re.sub(r'--color-brass:\s*#[a-zA-Z0-9]+;', '--color-brass: #FBBF24;', css) # Amber 400 for brass
with open('src/index.css', 'w') as f:
    f.write(css)

# Let's write AdPlaceholder.tsx
ad_component = """import React from 'react';

interface AdPlaceholderProps {
  format: 'banner' | 'rectangle';
  className?: string;
}

export const AdPlaceholder: React.FC<AdPlaceholderProps> = React.memo(({ format, className = '' }) => {
  const isBanner = format === 'banner';
  
  return (
    <div className={`flex flex-col items-center justify-center bg-slate-900/60 border border-slate-800/80 rounded-2xl relative overflow-hidden group ${isBanner ? 'w-full max-w-[728px] h-[90px] mx-auto' : 'w-[300px] h-[250px] mx-auto'} ${className}`}>
      <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
      <span className="text-xs font-mono text-slate-100 uppercase tracking-widest mb-1 opacity-50">Advertisement</span>
      <div className="flex items-center gap-2 text-slate-200">
        <span className="text-sm font-bold tracking-wider">{isBanner ? '728 x 90' : '300 x 250'}</span>
        <span className="text-gold font-bold text-lg leading-none">Premium Ad Space</span>
      </div>
    </div>
  );
});
"""
with open('src/components/AdPlaceholder.tsx', 'w') as f:
    f.write(ad_component)

def process_file(filepath):
    if not filepath.endswith('.tsx') and not filepath.endswith('.ts'):
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content

    # Upgrade H1 and H2 and prominent text to text-gold
    # We will look for <h1 and <h2 and add text-gold, removing text-white
    
    # Simple regex to replace text-white with text-yellow-400 on h1, h2, h3, or big text (text-3xl, text-4xl, text-5xl)
    
    # We also need to inject AdPlaceholders into Home and CountryPage.
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

