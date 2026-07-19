import React from 'react';
import { Link } from 'react-router-dom';

export const TrustFooter: React.FC = React.memo(() => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="w-full mt-16 bg-[#070a12] border-t border-slate-800/80 text-slate-100 py-10 px-6 font-sans">
      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
        
        {/* Column 1: Brand Authority Description */}
        <div className="md:col-span-2 space-y-3">
          <div className="flex items-center gap-2">
            <span className="font-sans font-bold tracking-tight text-white text-xl">
              Zip<span className="text-blue-300 font-medium">Intel</span> AI
            </span>
          </div>
          <p className="text-base text-slate-100 leading-relaxed max-w-sm">
            Oka scalable digital ecosystem for context-aware global financial routing matrix computations. Providing deterministic verification patterns for 17 target countries with zero latency.
          </p>
        </div>

        {/* Column 2: Quick Compliance / Legal Links */}
        <div>
          <h4 className="text-base font-mono uppercase tracking-widest text-slate-100 font-bold mb-3">Legal Registry</h4>
          <ul className="space-y-2 text-base font-mono">
            <li><Link to="/privacy" className="hover:text-emerald-300 transition-colors">Privacy Policy</Link></li>
            <li><Link to="/terms" className="hover:text-emerald-300 transition-colors">Terms of Service</Link></li>
            <li><Link to="/disclaimer" className="hover:text-emerald-300 transition-colors">Financial Disclaimer</Link></li>
          </ul>
        </div>

        {/* Column 3: Trust & Security Indicators */}
        <div>
          <h4 className="text-base font-mono uppercase tracking-widest text-slate-100 font-bold mb-3">System Authority</h4>
          <div className="space-y-2">
            {/* SSL & GDPR Badges */}
            <div className="flex items-center gap-2 text-base font-mono text-emerald-300 bg-emerald-500/5 border border-emerald-500/10 px-2 py-1 rounded w-fit">
              <span>🔒 SSL SECURE NODE</span>
            </div>
            <div className="flex items-center gap-2 text-base font-mono text-blue-300 bg-blue-500/5 border border-blue-500/10 px-2 py-1 rounded w-fit">
              <span>🇪🇺 GDPR COMPLIANT</span>
            </div>
            <div className="flex items-center gap-2 text-base font-mono text-slate-100 bg-slate-800/50 border border-slate-700/50 px-2 py-1 rounded w-fit">
              <span>⚡ HOSTING: VERCEL EDGE</span>
            </div>
          </div>
        </div>

      </div>

      {/* Regulatory Disclosure Section */}
      <div className="max-w-6xl mx-auto mb-8 p-4 bg-slate-900/30 border border-slate-800/50 rounded-xl">
        <h4 className="text-base font-mono uppercase tracking-[0.2em] text-slate-100 font-bold mb-3 border-b border-slate-800 pb-2">
          Global Regulatory & Financial Disclosure
        </h4>
        <div className="grid md:grid-cols-2 gap-6 text-sm font-mono leading-relaxed text-slate-100 italic">
          <p>
            <strong className="text-slate-100 uppercase">Financial Accuracy:</strong> ZipIntel AI is a data analysis platform. Routing codes (IFSC, ABA, SWIFT, IBAN) are generated via deterministic interpolation. While we maintain a 99.9% verification baseline, users MUST verify all mission-critical data with their primary financial institution before executing transactions. We are not a bank or registered financial advisor.
          </p>
          <p>
            <strong className="text-slate-100 uppercase">Jurisdictional Notice:</strong> This software operates under the digital services frameworks of India (IT Act 2000), the European Union (GDPR), and the United States (Electronic Communications Privacy Act). All routing matrices are provided "as-is" for informational purposes. Local jurisdictional restrictions may apply to specific ledger node queries.
          </p>
        </div>
      </div>

      {/* Bottom Footer Fine Print */}
      <div className="max-w-6xl mx-auto pt-6 border-t border-slate-900 flex flex-col md:flex-row justify-between items-center gap-4 text-base font-mono text-slate-100 text-center md:text-left">
        <p>© {currentYear} ZipIntel AI Digital Infrastructure. All rights reserved.</p>
        <p className="text-slate-100">
          Founder Status:{" "}
          <a 
            href="https://www.linkedin.com/in/munchingi-matya-raju-52baa71bb/"
            target="_blank" 
            rel="noopener noreferrer" 
            className="text-blue-300 hover:text-blue-300 underline transition-colors font-semibold"
          >
            Verified Professional Node via LinkedIn →
          </a>
        </p>
      </div>
    </footer>
  );
});
