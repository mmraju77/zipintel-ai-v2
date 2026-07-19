import { SEO } from '../components/SEO';
import React from 'react';
import { motion } from 'motion/react';
import { Shield, Cpu, Globe, Award, Linkedin, Mail } from 'lucide-react';

export default function AboutUs() {
  return (
    
    <>
      <SEO title="About Us - ZipIntel AI" description="Learn more about the ZipIntel AI project and our mission." />
      <div className="min-h-screen bg-[#0B0F19] text-slate-300 py-12 px-6 font-sans">
      <div className="max-w-4xl mx-auto">
        {/* Header Section */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-16"
        >
          <span className="text-sm font-mono uppercase tracking-[0.3em] text-blue-500 bg-blue-500/10 border border-blue-500/20 px-3 py-1 rounded-full mb-6 inline-block">
            Founding Vision
          </span>
          <h1 className="text-4xl md:text-5xl lg:text-7xl font-bold text-white tracking-tight mb-4">
            Architecting the Future of <span className="text-blue-500">Global Financial Data</span>
          </h1>
          <p className="text-slate-400 text-xl max-w-2xl mx-auto leading-relaxed">
            ZipIntel AI is built on the principle of deterministic precision. We bridge the gap between global postal nodes and complex financial routing infrastructures.
          </p>
        </motion.div>

        {/* Founder Profile - Dark Premium Fintech Card */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          className="relative group bg-slate-900/40 border border-slate-800/80 rounded-3xl p-8 md:p-12 overflow-hidden shadow-2xl mb-16"
        >
          <div className="absolute top-0 right-0 w-64 h-64 bg-blue-600/5 rounded-full blur-[100px] -mr-32 -mt-32"></div>
          
          <div className="grid md:grid-cols-3 gap-12 items-center relative z-10">
            {/* Visual/Image Placeholder */}
            <div className="md:col-span-1">
              <div className="aspect-square rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-900 flex items-center justify-center border border-blue-400/20 shadow-[0_0_30px_rgba(37,99,235,0.2)]">
                <Cpu className="w-20 h-20 text-white/90" />
              </div>
            </div>

            {/* Profile Details */}
            <div className="md:col-span-2 space-y-6">
              <div>
                <h2 className="text-3xl font-bold text-white mb-1">Munchangi Matyaraju (mm Raju)</h2>
                <p className="text-blue-400 font-mono text-base uppercase tracking-widest font-semibold italic">Chief AI Architect & Founder</p>
              </div>

              <p className="text-slate-300 leading-relaxed italic border-l-2 border-blue-500/50 pl-6 text-base">
                "Our mission is to eliminate the 'last-mile' friction in global fintech. By indexing the core geometry of postal codes, we provide a mathematical foundation for routing that legacy systems simply cannot match."
              </p>

              <div className="grid grid-cols-2 gap-4">
                <div className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-xl">
                  <p className="text-sm text-slate-400 uppercase font-bold mb-1">Specialization</p>
                  <p className="text-sm text-white font-mono">Neural Routing Matrix</p>
                </div>
                <div className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-xl">
                  <p className="text-sm text-slate-400 uppercase font-bold mb-1">Project Scale</p>
                  <p className="text-sm text-white font-mono">17+ Jurisdictions</p>
                </div>
              </div>

              <div className="flex gap-4 pt-4">
                <a aria-label="LinkedIn Profile"
                  href="https://www.linkedin.com/in/munchingi-matya-raju-52baa71bb/"
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="p-2.5 bg-blue-600/10 hover:bg-blue-600 border border-blue-500/20 text-blue-400 hover:text-white rounded-lg transition-all"
                >
                  <Linkedin className="w-5 h-5" />
                </a>
                <a aria-label="Email Address"
                  href="mailto:MooVi7g@gmail.com"
                  className="flex items-center gap-2 px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white text-sm font-mono uppercase font-bold rounded-lg border border-slate-700 transition-colors"
                >
                  <Mail className="w-4 h-4" /> Direct Node
                </a>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Core Values / Infrastructure */}
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { 
              title: "Global Compliance", 
              icon: Shield, 
              desc: "Adhering to strict regulatory frameworks across EU, NAM, and APAC regions." 
            },
            { 
              title: "AI Verfication", 
              icon: Award, 
              desc: "Every routing node is validated through our proprietary neural context engine." 
            },
            { 
              title: "High Precision", 
              icon: Globe, 
              desc: "Deterministic postal geometry ensuring 99.99% clearing accuracy." 
            }
          ].map((v, i) => (
            <motion.div 
              key={v.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 + (i * 0.1) }}
              className="p-6 bg-slate-900/40 border border-slate-800/80 rounded-2xl"
            >
              <v.icon className="w-8 h-8 text-blue-500 mb-4" />
              <h4 className="text-white font-bold mb-2 uppercase tracking-tight text-base">{v.title}</h4>
              <p className="text-sm text-slate-400 leading-relaxed">{v.desc}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
    </>
  );
}