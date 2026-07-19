import express from "express";
import helmet from "helmet";
import compression from "compression";

import path from "path";
import app from "./api/index";

const PORT = 3000;

// Vite middleware and Server start
async function startApp() {
  app.use(compression());
  app.use(helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", "'unsafe-inline'", "'unsafe-eval'", "https://www.googletagmanager.com"],
        styleSrc: ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"],
        fontSrc: ["'self'", "https://fonts.gstatic.com"],
        imgSrc: ["'self'", "data:", "https://www.googletagmanager.com"],
        connectSrc: ["'self'", "https://www.google-analytics.com", "https://region1.google-analytics.com"],
        frameSrc: ["'self'"],
        frameAncestors: ["*"],
      }
    },
    crossOriginEmbedderPolicy: false,
    frameguard: false,
  }));

  
  if (process.env.NODE_ENV !== "production") {
    const { createServer: createViteServer } = await import("vite");
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    app.use(express.static(distPath, {
      maxAge: '1y',
      etag: true
    }));
    app.get('*all', (_req, res) => {
      res.sendFile(path.join(distPath, 'index.html'));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
  });
}

startApp();

