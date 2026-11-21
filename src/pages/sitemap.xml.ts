import type { APIRoute } from 'astro';
import { reader, tumSayfalar, href } from '../lib/icerik';

// Site haritası: ana sayfa, Keystatic'teki tüm sayfalar ve blog yazıları.
export const GET: APIRoute = async ({ site }) => {
  const url = (yol: string) => new URL(yol, site).href;
  const sayfalar = await tumSayfalar();
  const yazilar = await reader.collections.blog.all();
  const kayitlar = [
    { loc: url('/') },
    ...sayfalar.map((s) => ({ loc: url(href(s.yol)) })),
    ...yazilar.map((y) => ({ loc: url(`/blog/${y.slug}/`), lastmod: y.entry.tarih ?? undefined })),
  ];
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${kayitlar.map((k) => `  <url><loc>${k.loc}</loc>${k.lastmod ? `<lastmod>${k.lastmod}</lastmod>` : ''}</url>`).join('\n')}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
