// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';
import partytown from '@astrojs/partytown';

import cloudflare from '@astrojs/cloudflare';
import react from '@astrojs/react';
import markdoc from '@astrojs/markdoc';
import keystatic from '@keystatic/astro';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  vite: {
    plugins: [tailwindcss()],
    optimizeDeps: {
      exclude: ['@keystatic/astro', 'virtual:keystatic-config']
    }
  },

  integrations: [partytown(), react(), markdoc(), keystatic()],
  adapter: cloudflare()
});