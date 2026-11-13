import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';
import node from '@astrojs/node';
import vercel from '@astrojs/vercel';

// KORVIA_STATIC=1 → yalnızca statik site (admin paneli olmadan) üretir.
const STATIC_ONLY = process.env.KORVIA_STATIC === '1';
// Vercel'de derlenirken Vercel adaptörü, diğer yerlerde Node adaptörü kullanılır.
const adapter = STATIC_ONLY ? undefined : process.env.VERCEL ? vercel() : node({ mode: 'standalone' });

export default defineConfig({
  site: process.env.SITE_URL || (process.env.VERCEL_PROJECT_PRODUCTION_URL ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}` : 'https://www.example.com.tr'),
  trailingSlash: 'ignore',
  output: 'static',
  integrations: STATIC_ONLY ? [] : [react(), keystatic()],
  adapter,
  build: { inlineStylesheets: 'auto' },
});
