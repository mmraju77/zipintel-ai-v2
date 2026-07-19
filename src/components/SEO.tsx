import React from 'react';
import { Helmet } from 'react-helmet-async';

interface SEOProps {
  title?: string;
  description?: string;
  canonical?: string;
  type?: string;
}

export const SEO: React.FC<SEOProps> = ({ 
  title = "ZipIntel - Global Intelligence Protocol",
  description = "Global Intelligence Protocol. Financial routing matrix and analytical logistics node.",
  canonical = "https://www.zipintel-ai.com",
  type = "website"
}) => {
  return (
    <Helmet>
      <title>{title}</title>
      <meta name="description" content={description} />
      <link rel="canonical" href={canonical} />

      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:type" content={type} />
      <meta property="og:url" content={canonical} />
      <meta property="og:image" content="https://www.zipintel-ai.com/og-image.jpg" />

      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      
      {/* Schema Markup for Organization */}
      <script type="application/ld+json">
        {JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Organization",
          "name": "ZipIntel AI",
          "url": "https://www.zipintel-ai.com",
          "logo": "https://www.zipintel-ai.com/logo.png"
        })}
      </script>
    </Helmet>
  );
};
