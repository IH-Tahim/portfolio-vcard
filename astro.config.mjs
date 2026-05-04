// @ts-check
import { defineConfig } from 'astro/config';


import partytown from '@astrojs/partytown';

import cloudflare from '@astrojs/cloudflare';
import react from '@astrojs/react';
import markdoc from '@astrojs/markdoc';
import keystatic from '@keystatic/astro';

const isProd = process.env.NODE_ENV === 'production' || process.env.npm_lifecycle_event === 'build';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  vite: {
    plugins: [],
    optimizeDeps: {
      exclude: ['@keystatic/astro', 'virtual:keystatic-config']
    }
  },

  integrations: [partytown(), react(), markdoc(), keystatic()],
  adapter: isProd ? cloudflare() : undefined
});