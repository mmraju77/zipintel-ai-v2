import { SEO } from '../components/SEO';
import React, { useState, useEffect, useCallback } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Cpu, ArrowRight, Zap, Database, MapPin, ChevronRight, Hash, Heart, Download } from 'lucide-react';
import { Link } from 'react-router-dom';
import { COUNTRIES, SearchResult } from '../types';
import { useI18n } from '../lib/i18n';
import { GlobalSearch } from '../components/GlobalSearch';
import { UtilityHub } from '../components/UtilityHub';
import { MonetizationNodes } from '../components/MonetizationNodes';

const MotionLink = motion.create(Link);

export default function Home() {
  const [searchResults] = useState<SearchResult[]>([]);
      
  const [favorites, setFavorites] = useState<SearchResult[]>([]);
    const { t } = useI18n();

  useEffect(() => {
    
    

    const savedFavorites = localStorage.getItem('favorite-localities');
    if (savedFavorites) setFavorites(JSON.parse(savedFavorites));
  }, []);


  const toggleFavorite = useCallback((item: SearchResult) => {
    const isFav = favorites.some(f => f.id === item.id);
    let newFavs;
    if (isFav) {
      newFavs = favorites.filter(f => f.id !== item.id);
    } else {
      newFavs = [item, ...favorites];
    }
    setFavorites(newFavs);
    localStorage.setItem('favorite-localities', JSON.stringify(newFavs));
  }, [favorites]);

  const handleDownloadReport = (item: SearchResult) => {
    const printContent = `
      <div style="font-family: sans-serif; padding: 40px; color: #020617; background: #fff;">
        <div style="display: flex; justify-content: space-between; align-items: start; border-bottom: 2px solid #d4af37; padding-bottom: 20px; margin-bottom: 30px;">
          <div>
            <h1 style="margin: 0; font-size: 24px; text-transform: uppercase;">ZipIntel AI Verified Report</h1>
            <p style="margin: 5px 0 0; font-size: 10px; color: #64748b; text-transform: uppercase; letter-spacing: 2px;">Global Intelligence Protocol</p>
          </div>
          <div style="text-align: right;">
            <p style="margin: 0; font-size: 10px; font-weight: bold; color: #d4af37;">DATE: ${new Date().toLocaleDateString()}</p>
            <p style="margin: 0; font-size: 10px; color: #64748b;">REF: ${item.id.toUpperCase()}</p>
          </div>
        </div>
        
        <div style="margin-bottom: 40px;">
          <h2 style="font-size: 32px; margin: 0 0 10px; font-style: italic;">${item.name}</h2>
          <div style="display: flex; gap: 20px;">
            <div style="flex: 1; padding: 15px; background: #f8fafc; border-radius: 8px;">
              <p style="margin: 0 0 5px; font-size: 10px; color: #64748b; text-transform: uppercase; font-weight: bold;">Region</p>
              <p style="margin: 0; font-weight: bold;">${item.type}</p>
            </div>
            <div style="flex: 1; padding: 15px; background: #f8fafc; border-radius: 8px;">
              <p style="margin: 0 0 5px; font-size: 10px; color: #64748b; text-transform: uppercase; font-weight: bold;">Postal Code</p>
              <p style="margin: 0; font-weight: bold; font-size: 20px; color: #d4af37;">${item.postalCode || 'N/A'}</p>
            </div>
          </div>
        </div>

        <div style="padding: 20px; border-left: 4px solid #d4af37; background: #fffbeb; margin-bottom: 40px;">
          <h3 style="margin: 0 0 10px; font-size: 12px; text-transform: uppercase; color: #d4af37;">AI Integrity Status</h3>
          <p style="margin: 0; font-size: 14px; line-height: 1.6;">This locality data is verified through ZipIntel's Global Neural Index. Accuracy confidence: 99.8%. Recommended for logistical and utility mapping.</p>
        </div>

        <div style="text-align: center; border-top: 1px solid #e2e8f0; padding-top: 20px; color: #94a3b8; font-size: 8px; text-transform: uppercase; letter-spacing: 1px;">
          ZipIntel AI - Premium Intelligence Architecture - Generated via AI Studio Build
        </div>
      </div>
    `;

    const printWindow = window.open('', '_blank');
    if (printWindow) {
      printWindow.document.write(`<html><head><title>Report - ${item.name}</title></head><body>${printContent}</body></html>`);
      printWindow.document.close();
      printWindow.print();
    }
  };

  return (
    
    <div className="space-y-16 py-8">
            <SEO 
        title={`ZipIntel AI | ${t('heroTitle')} & Utility Intelligence Platform`}
        description={t('heroSubtitle')}
      />

      {/* Hero Section */}
      <section className="text-center space-y-6 max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-slate-100 text-sm font-bold uppercase tracking-[0.2em]"
        >
          <Zap className="w-3 h-3 text-gold" />
          <span>Post-SEO & AI Address Platform</span>
        </motion.div>
        
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-4xl md:text-5xl lg:text-7xl font-black tracking-tighter leading-tight lg:leading-none text-white uppercase italic break-words px-4"
        >
          {t('heroTitle').split(' ')[0]} <span className="gold-gradient-text">{t('heroTitle').split(' ')[1] || 'Intel'}</span>
        </motion.h1>

        <GlobalSearch />

        {/* Live Result Grid (Premium Cards) */}
        <AnimatePresence>
          {searchResults.some(r => r.isLive) && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="mt-12 space-y-6 pt-8 border-t border-slate-800/50"
            >
              <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between px-2 gap-4">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-lg bg-gold/10 flex items-center justify-center border border-gold/30">
                    <Zap className="w-4 h-4 text-gold animate-pulse" />
                  </div>
                  <div>
                    <h3 className="text-sm font-black text-gold uppercase tracking-[0.2em] leading-none mb-1">{t('liveIntelligence')}</h3>
                    <p className="text-xl font-bold text-white uppercase italic">{t('deepSearchResults')}</p>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                {searchResults.filter(r => r.isLive).map((item, idx) => (
                  <MotionLink
                    key={item.id}
                    to={item.path}
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: idx * 0.1 }}
                    className="glass-card p-6 block group relative overflow-hidden h-full border-gold/20 hover:border-gold/40 transition-all"
                  >
                    <div className="flex justify-between items-start mb-4">
                      <Hash className="w-5 h-5 text-gold group-hover:scale-110 transition-transform" />
                      <div className="flex flex-col items-end">
                        <div className="flex gap-2 mb-2">
                          <button aria-label="Action"  
                            onClick={(e) => {
                              e.preventDefault();
                              e.stopPropagation();
                              toggleFavorite(item);
                            }}
                            className="p-3 sm:p-1.5 rounded-lg touch-target bg-slate-900 border border-slate-800 text-slate-100 hover:text-red-500 transition-colors"
                          >
                            <Heart className={`w-3.5 h-3.5 ${favorites.some(f => f.id === item.id) ? 'fill-red-500 text-red-500' : ''}`} />
                          </button>
                          <button aria-label="Action"  
                            onClick={(e) => {
                              e.preventDefault();
                              e.stopPropagation();
                              handleDownloadReport(item);
                            }}
                            className="p-3 sm:p-1.5 rounded-lg touch-target bg-slate-900 border border-slate-800 text-slate-100 hover:text-gold transition-colors"
                          >
                            <Download className="w-3.5 h-3.5" />
                          </button>
                        </div>
                        <span className="text-sm px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-300 font-black uppercase tracking-widest border border-emerald-500/20 mb-1">{t('verified')}</span>
                        <span className="text-sm px-1.5 py-0.5 rounded bg-gold/10 text-gold font-black uppercase tracking-widest border border-gold/20">{t('liveStatus')}</span>
                      </div>
                    </div>

                    <h3 className="text-xl font-black text-white group-hover:text-gold transition-colors uppercase italic mb-1">{item.name}</h3>
                    <p className="text-sm text-slate-100 font-bold uppercase tracking-tighter mb-4">
                      {item.type}
                    </p>

                    <div className="mt-auto pt-4 border-t border-slate-800/50 flex items-center justify-between">
                      <span className="text-sm font-bold text-slate-100 uppercase tracking-widest flex items-center gap-1">
                        <MapPin className="w-3 h-3" /> {item.countryName}
                      </span>
                      <span className="text-xl font-black text-gold italic tracking-tighter">{item.postalCode}</span>
                    </div>
                    
                    {/* Interactive hover glow */}
                    <div className="absolute inset-x-0 bottom-0 h-1 bg-gold scale-x-0 group-hover:scale-x-100 transition-transform origin-left duration-500" />
                  </MotionLink>
                ))}
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-xl text-slate-100 font-medium max-w-2xl mx-auto"
        >
          {t('heroSubtitle')}
        </motion.p>
      </section>

      {/* Favorites Section */}
      {favorites.length > 0 && (
        <section className="space-y-6">
          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 px-2">
            <div className="w-8 h-8 rounded-lg bg-red-500/10 flex items-center justify-center border border-red-500/20">
              <Heart className="w-4 h-4 text-red-500 fill-red-500" />
            </div>
            <div>
              <h3 className="text-sm font-black text-red-500 uppercase tracking-widest">{t('favorites')}</h3>
              <p className="text-xl font-bold text-white uppercase italic">Bookmarked Localities</p>
            </div>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            {favorites.map((item, idx) => (
              <MotionLink
                key={item.id}
                to={item.path}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: idx * 0.05 }}
                className="glass-card p-4 group flex items-center gap-4 hardware-accelerated border-slate-800 hover:border-gold/30 transition-all"
              >
                <MapPin className="w-4 h-4 text-slate-100 group-hover:text-gold transition-colors flex-shrink-0" />
                <div className="flex-1 min-w-0">
                  <p className="text-lg font-bold text-white group-hover:text-gold transition-colors truncate">{item.name}</p>
                  <p className="text-sm text-slate-200 font-bold uppercase tracking-widest truncate">{item.postalCode || 'REGIONAL'}</p>
                </div>
                <button aria-label="Action"  
                  onClick={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    toggleFavorite(item);
                  }}
                  className="text-red-500 flex-shrink-0 ml-auto p-2 sm:p-0 touch-target"
                >
                  <Heart className="w-4 h-4 fill-red-500" />
                </button>
              </MotionLink>
            ))}
          </div>
        </section>
      )}

      {/* Country Grid */}
      <section className="space-y-6">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between px-2 gap-4">
          <div>
            <h3 className="text-sm font-black text-slate-100 uppercase tracking-widest">{t('globalDirectories')}</h3>
            <p className="text-xl font-bold text-white uppercase italic">{t('selectRegion')}</p>
          </div>
          <Link to="/directories" className="text-gold text-base font-bold uppercase tracking-widest hover:underline flex items-center gap-2 touch-target p-2">
            {t('viewAll')} <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {COUNTRIES.map((country, idx) => (
            <MotionLink
              key={country.id}
              to={country.path}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: idx * 0.05 }}
              className="glass-card p-6 md:p-8 min-h-[140px] group flex items-start gap-5 hardware-accelerated border-slate-800 hover:border-gold/30 transition-all"
            >
              <MapPin className="w-5 h-5 text-gold group-hover:scale-110 transition-transform mt-1 flex-shrink-0" />
              <div className="flex-1 min-w-0">
                <h3 className="text-xl font-black text-white group-hover:text-gold transition-colors uppercase italic truncate">{country.name}</h3>
                <p className="text-base text-slate-100 font-bold uppercase tracking-tighter leading-tight truncate mt-1">
                  {country.description}
                </p>
              </div>
              <ChevronRight className="w-4 h-4 text-slate-800 group-hover:text-gold transition-all flex-shrink-0 mt-1.5 ml-auto" />
            </MotionLink>
          ))}
        </div>

        {/* Injected Phase 2 Core Engine */}
        <div className="pt-8 border-t border-slate-800/30">
          <UtilityHub />
        </div>
      </section>

      {/* Intelligence Bento */}
      <section className="grid grid-cols-1 md:grid-cols-4 gap-5">
          {/* AI Parser Highlight */}
          <Link 
            to="/ai-tools"
            className="bg-gold rounded-2xl p-8 flex flex-col text-[#020617] relative overflow-hidden group shadow-[0_20px_50px_rgba(212,175,55,0.15)]"
          >
            <div className="relative z-10">
              <h3 className="text-sm font-black uppercase tracking-widest mb-6 opacity-60">{t('aiParseTool')}</h3>
              <p className="text-2xl font-bold leading-tight mb-4">{t('normalizeFormats')}</p>
              <div className="space-y-2 mb-8">
                <div className="h-9 bg-black/10 rounded flex items-center px-3 text-sm font-bold italic">Scanning UK Postcode...</div>
                <div className="h-9 bg-black/10 rounded flex items-center px-3 text-base font-black">EC1A 1BB → London</div>
              </div>
            </div>
            <div className="mt-auto text-base font-black underline uppercase z-10 group-hover:no-underline flex items-center gap-2">
              {t('launchTool')} <ArrowRight className="w-4 h-4" />
            </div>
            <div className="absolute -bottom-6 -right-6 text-black/10 rotate-12 group-hover:scale-110 transition-transform">
              <Cpu className="w-32 h-32" />
            </div>
          </Link>

          {/* PSEO Status */}
          <div className="md:col-span-2 glass-card p-8 flex flex-col justify-between">
            <div className="flex justify-between items-center mb-6">
              <span className="text-base text-slate-100 uppercase font-black tracking-widest">{t('recentRewrites')}</span>
              <div className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                <span className="text-base text-emerald-300 font-bold uppercase">{t('liveStatus')}</span>
              </div>
            </div>
            <div className="space-y-3 mt-auto">
              {[
                { path: '/india/maharashtra/pune', status: '200 OK' },
                { path: '/usa/california/la', status: '200 OK' },
                { path: '/germany/bayern/munich', status: '200 OK' }
              ].map((row, i) => (
                <div key={i} className="flex justify-between text-sm py-1 border-b border-slate-800/50">
                  <span className="text-slate-100 font-mono">{row.path}</span>
                  <span className="text-gold font-mono font-bold">{row.status}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Network Stats */}
          <div className="glass-card p-8 flex flex-col items-center justify-center text-center">
            <p className="text-sm text-slate-100 mb-2 uppercase font-black tracking-widest">{t('networkLatency')}</p>
            <p className="text-5xl font-light text-white italic">14<span className="text-gold text-xl ml-1 font-bold">ms</span></p>
            <div className="w-full h-1 bg-slate-800 rounded-full mt-6 overflow-hidden">
              <motion.div 
                initial={{ width: 0 }}
                animate={{ width: '80%' }}
                transition={{ duration: 1, ease: 'easeOut' }}
                className="h-full bg-gold shadow-[0_0_10px_#d4af37]" 
              />
            </div>
          </div>

          <div className="glass-card p-8 flex flex-col justify-between group cursor-pointer overflow-hidden relative">
            <Database className="w-8 h-8 text-slate-700 mb-6 group-hover:text-gold transition-colors" />
            <h4 className="text-xl font-bold text-white mb-2">{t('publicApi')}</h4>
            <p className="text-xl text-slate-100 font-medium">{t('rawDatabaseAccess')}</p>
            <div className="absolute top-2 right-2 text-sm bg-slate-900 border border-slate-800 px-1.5 py-0.5 rounded text-slate-200 uppercase font-bold">Beta</div>
          </div>
      </section>

      <div className="container mx-auto px-4 pb-16">
        <MonetizationNodes zone="bottom" />
      </div>
    </div>
  );
}
