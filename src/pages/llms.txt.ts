import type { APIRoute } from 'astro';
import { reader, tumSayfalar, href, ayarlar, BOLUM_ADLARI } from '../lib/icerik';

// Yapay zekâ asistanları için site özeti (llmstxt.org biçimi). Sayfa listesi Keystatic içeriğinden üretilir.
export const GET: APIRoute = async ({ site }) => {
  const a = await ayarlar();
  const url = (yol: string) => new URL(yol, site).href;
  const sayfalar = (await tumSayfalar()).filter((s) => s.bolum !== 'yasal');
  const yazilar = (await reader.collections.blog.all()).sort((x, y) => (y.entry.tarih ?? '').localeCompare(x.entry.tarih ?? ''));

  const bolumler = Object.entries(BOLUM_ADLARI).map(([anahtar, ad]) => {
    const liste = sayfalar
      .filter((s) => s.bolum === anahtar)
      .sort((x, y) => (x.sira ?? 0) - (y.sira ?? 0))
      .map((s) => `- [${s.kimlik}](${url(href(s.yol))})${s.menuAciklama ? `: ${s.menuAciklama}` : ''}`);
    return liste.length ? `## ${ad}\n\n${liste.join('\n')}` : '';
  });

  const metin = `# Korvia

> Korvia – ${a.aciklamaSatiri}. ${a.footerMetni}

- Türkiye'de geliştirilir; satış, kurulum ve destek Türkiye'dedir. Destek Türkçedir.
- Kurulum: yerinde (on-prem), özel bulut, internetten yalıtılmış ağ veya yönetilen hizmet. Yerinde ve özel bulut kurulumda içerik ve kanıt kurumun altyapısında kalır.
- T.C. kimlik, IBAN ve vergi numarası gibi Türkçe veri tipleri hazır gelir.
- Web: ${url('/')} · İletişim: ${a.satisEposta}

${bolumler.filter(Boolean).join('\n\n')}

## Blog

${yazilar.map((y) => `- [${y.entry.baslik}](${url(`/blog/${y.slug}/`)}): ${y.entry.ozet.trim()}`).join('\n')}
`;
  return new Response(metin, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
