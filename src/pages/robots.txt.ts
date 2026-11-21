import type { APIRoute } from 'astro';

// Arama motorları ve yapay zekâ tarayıcıları için açık erişim; site haritası adresi SITE_URL'den gelir.
const BOTLAR = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'PerplexityBot', 'Google-Extended'];

export const GET: APIRoute = ({ site }) => {
  const metin = [
    ...BOTLAR.flatMap((b) => [`User-agent: ${b}`, 'Allow: /', '']),
    'User-agent: *',
    'Allow: /',
    '',
    `Sitemap: ${new URL('/sitemap.xml', site).href}`,
    '',
  ].join('\n');
  return new Response(metin, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
