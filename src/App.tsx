import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { I18nProvider } from './lib/i18n';
import Layout from './components/Layout';
import { SEO } from './components/SEO';
import Home from './pages/Home';
const CountryPage = React.lazy(() => import('./pages/CountryPage'));
const AITools = React.lazy(() => import('./pages/AIToolsPage'));
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const AboutUs = React.lazy(() => import('./pages/AboutUs'));

declare global {
  interface Window {
    dataLayer: any[];
    gtag: (...args: any[]) => void;
  }
}

export default function App() {
  useEffect(() => {
    // Dynamic GA4 Injection
    const GA_MEASUREMENT_ID = 'G-SH6KFVW7ZK';
    
    // Inject the main gtag script
    const script = document.createElement('script');
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`;
    script.async = true;
    document.head.appendChild(script);

    // Initialize dataLayer and gtag
    window.dataLayer = window.dataLayer || [];
    window.gtag = function() {
      window.dataLayer.push(arguments);
    };
    
    window.gtag('js', new Date());
    window.gtag('config', GA_MEASUREMENT_ID);

    return () => {
      // Clean up if component unmounts (optional for App, but good practice)
      if (document.head.contains(script)) {
        document.head.removeChild(script);
      }
    };
  }, []);

  return (
    <HelmetProvider>
      <SEO />
      <I18nProvider>
        <BrowserRouter>
          <Layout>
            <React.Suspense fallback={<div className="min-h-screen flex items-center justify-center bg-[#0B0F19]"><div className="w-8 h-8 border-4 border-gold border-t-transparent rounded-full animate-spin"></div></div>}>
              <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<AboutUs />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/ai-tools" element={<AITools />} />
              <Route path="/zip/:countryCode/:region/:zipCode" element={<CountryPage />} />
              <Route path="/:countryId" element={<CountryPage />} />
              <Route path="/:countryId/:l1" element={<CountryPage />} />
              <Route path="/:countryId/:l1/:l2" element={<CountryPage />} />
              <Route path="/:countryId/:l1/:l2/:l3" element={<CountryPage />} />
            </Routes>
            </React.Suspense>
          </Layout>
        </BrowserRouter>
      </I18nProvider>
    </HelmetProvider>
  );
}
