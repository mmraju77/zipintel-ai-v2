import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { I18nProvider } from './lib/i18n';
import Layout from './components/Layout';
import Home from './pages/Home';
import CountryPage from './pages/CountryPage';
import AITools from './pages/AIToolsPage';
import Dashboard from './pages/Dashboard';
import AboutUs from './pages/AboutUs';

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
      <I18nProvider>
        <BrowserRouter>
          <Layout>
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
          </Layout>
        </BrowserRouter>
      </I18nProvider>
    </HelmetProvider>
  );
}
