import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { InfrastructureInsights } from '../components/InfrastructureInsights';
import { MonetizationNodes } from '../components/MonetizationNodes';
import { CommunityLayer } from '../components/CommunityLayer';
import { useI18n } from '../lib/i18n';

export default function CountryPage() {
  const { language } = useI18n();
  const { 
    countryId, l1, l2, l3, 
    countryCode, zipCode 
  } = useParams<{ 
    countryId?: string; l1?: string; l2?: string; l3?: string;
    countryCode?: string;zipCode?: string;
  }>();
  
  const currentCountry = (countryCode || countryId || 'in').toLowerCase().trim();
  const rawZip = (zipCode || l3 || l2 || l1);
  const currentZip = rawZip ? rawZip.trim() : undefined;

  // SEO Meta Text Dynamic Content Generation (Google Search Snippet Moat)
  const getSEOMeta = () => {
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
  };

  const seo = getSEOMeta();

  return (
    <div className="min-h-screen bg-[#0B0F19] text-slate-300 p-6 font-sans">
      <Helmet>
        <title>{seo.title}</title>
        <meta name="description" content={seo.description} />
        <link rel="canonical" href={`https://www.zipintel-ai.com/${currentCountry}/${zipCode || ''}`} />
        <meta property="og:title" content={seo.title} />
        <meta property="og:description" content={seo.description} />
        <meta name="twitter:title" content={seo.title} />
        <meta name="twitter:description" content={seo.description} />
      </Helmet>

      {/* Breadcrumb Navigation - Search Crawlers కి చాలా ముఖ్యం */}
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
      </div>

      {/* Main Dynamic Landing Header */}
      <div className="w-full max-w-[1920px] mx-auto bg-slate-900/40 border border-slate-800/80 rounded-2xl p-6 md:p-8 mb-8 shadow-zipGlow">
        <div className="flex flex-wrap items-center justify-between gap-4 mb-4">
          <div>
            <span className="text-sm font-mono uppercase bg-blue-600/10 text-blue-300 border border-blue-500/20 px-2.5 py-1 rounded">
              Programmatic Data Node Active
            </span>
            <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold text-white tracking-tight mt-3">
              Target Infrastructure: <span className="text-blue-300 font-mono">{currentZip ? currentZip : currentCountry.toUpperCase()}</span>
            </h1>
          </div>
          <div className="text-right">
            <span className="text-sm font-mono text-slate-100 block">REGIONAL DIRECTORY</span>
            <span className="text-base font-semibold text-white uppercase tracking-wider">{currentCountry} / Global Matrix</span>
          </div>
        </div>
        
        <p className="text-slate-100 text-base max-w-3xl leading-relaxed">
          {seo.description} This page was dynamically compiled by our context-aware parser engine using deterministic calculations with zero external latency.
        </p>
      </div>

      {/* Grid Layout containing our Core Infrastructure Insights Card */}
      <div className="w-full max-w-[1920px] mx-auto">
        
        {/* Card 1 & 2: Local Node Metadata (SEO Rich Text Content) */}
        <div className="w-full space-y-6">
          <div className="p-6 bg-slate-900/40 border border-slate-800/80 rounded-xl">
            <h3 className="text-md font-mono uppercase tracking-wider text-slate-100 mb-3 border-b border-slate-800 pb-2">
              📋 Regional SEO Metadata Context
            </h3>
            <div className="space-y-3 text-base">
              <p><span className="text-slate-100 font-mono">Dynamic Page Title:</span> <span className="text-white font-medium">{seo.title}</span></p>
              <p><span className="text-slate-100 font-mono">Index Optimization:</span> <span className="text-emerald-300 font-mono">Ready for Googlebot Indexing / Canonical Active</span></p>
            </div>
          </div>

          <div className="p-6 bg-slate-900/40 border border-slate-800/80 rounded-xl">
            <h3 className="text-md font-mono uppercase tracking-wider text-slate-100 mb-2">
              💡 User Quick Actions
            </h3>
            <p className="text-sm text-slate-100 mb-4">Use our free Phase 2 utilities below to export or format this node data structure.</p>
            <div className="flex flex-wrap gap-3">
              <button onClick={() => window.print()} className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-white font-mono text-sm rounded border border-slate-700 transition-colors">
                [Print/Save PDF]
              </button>
              <Link to="/" className="px-3 py-1.5 bg-blue-600/10 hover:bg-blue-600/20 text-blue-300 font-mono text-sm rounded border border-blue-500/30 transition-colors">
                ← Back to Core Hub
              </Link>
            </div>
          </div>
        </div>

        {/* Card 3: Our Financial Routing Infrastructure Engine (Card 5 from previous fix) */}
        </div>
      <div className="w-full max-w-[1920px] mx-auto mt-6">
        <div className="w-full">
          <InfrastructureInsights 
            districtId={currentZip || 'REGIONAL'} 
            language={language}
            countryCode={currentCountry} 
            zipCode={currentZip} 
          />
          </div>
      </div>
      <div className="w-full max-w-[1920px] mx-auto mt-6">
        <div className="w-full">
          <div className="mt-6">
            <MonetizationNodes zone="sidebar" />
          </div>
        </div>

      </div>

      <div className="w-full max-w-[1920px] mx-auto mt-6">
        <MonetizationNodes zone="bottom" />
      </div>

      <div className="w-full max-w-[1920px] mx-auto mt-2">
        <CommunityLayer />
      </div>
    </div>
  );
}

