import React from 'react';

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
