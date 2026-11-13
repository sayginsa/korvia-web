import { createReader } from '@keystatic/core/reader';
import Markdoc from '@markdoc/markdoc';
import keystaticConfig from '../../keystatic.config';

export const reader = createReader(process.cwd(), keystaticConfig);

export type Ayarlar = NonNullable<Awaited<ReturnType<typeof reader.singletons.ayarlar.read>>>;

let _ayarlar: Ayarlar | null = null;
export async function ayarlar(): Promise<Ayarlar> {
  if (!_ayarlar) _ayarlar = (await reader.singletons.ayarlar.read())!;
  return _ayarlar;
}

/** Metinlerdeki {sirketAdi}, {satisEposta} gibi yer tutucuları site ayarlarıyla doldurur. */
export async function doldur(metin: string): Promise<string> {
  const a = (await ayarlar()) as Record<string, unknown>;
  return metin.replace(/\{(\w+)\}/g, (m, k) => (typeof a[k] === 'string' ? (a[k] as string) : m));
}

export const BOLUM_ADLARI: Record<string, string> = {
  platform: 'Platform',
  'yapay-zeka': 'Yapay Zekâ Güvenliği',
  cozumler: 'Çözümler',
  sektorler: 'Sektörler',
  kaynaklar: 'Kaynaklar',
  kurumsal: 'Kurumsal',
};

export const href = (yol: string) => (yol ? `/${yol.replace(/^\/|\/$/g, '')}/` : '/');

export async function tumSayfalar() {
  const liste = await reader.collections.sayfalar.all();
  return liste.map((s) => ({ slug: s.slug, ...s.entry }));
}

export type MenuOgesi = { ad: string; aciklama: string; url: string; ikon?: string };
export type MenuBolumu = { anahtar: string; ad: string; gruplar: { ad: string; ogeler: MenuOgesi[] }[] };

/** Menü, Keystatic'teki sayfaların "Menü bölümü" ve "Menü sırası" alanlarından üretilir. */
export async function menu(): Promise<MenuBolumu[]> {
  const sayfalar = await tumSayfalar();
  const grup = (b: string) =>
    sayfalar
      .filter((s) => s.bolum === b)
      .sort((x, y) => (x.sira ?? 0) - (y.sira ?? 0))
      .map((s) => ({ ad: s.kimlik, aciklama: s.menuAciklama, url: href(s.yol), ikon: s.ikon }));
  return [
    { anahtar: 'platform', ad: 'Platform', gruplar: [{ ad: 'Modüller', ogeler: grup('platform') }] },
    { anahtar: 'yapay-zeka', ad: 'Yapay Zekâ Güvenliği', gruplar: [{ ad: 'Yapay zekâ', ogeler: grup('yapay-zeka') }] },
    {
      anahtar: 'cozumler',
      ad: 'Çözümler',
      gruplar: [
        { ad: 'Kullanım alanları', ogeler: grup('cozumler') },
        { ad: 'Sektörler', ogeler: grup('sektorler') },
      ],
    },
    { anahtar: 'kaynaklar', ad: 'Kaynaklar', gruplar: [{ ad: 'Kaynaklar', ogeler: grup('kaynaklar') }] },
    { anahtar: 'kurumsal', ad: 'Kurumsal', gruplar: [{ ad: 'Kurumsal', ogeler: grup('kurumsal').filter((o) => o.url !== '/demo/') }] },
  ];
}

export function markdocHtml(node: Parameters<typeof Markdoc.transform>[0]) {
  return Markdoc.renderers.html(Markdoc.transform(node));
}

const AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
export function tarihTR(iso: string | null | undefined) {
  if (!iso) return '';
  const [y, m, d] = iso.split('-').map(Number);
  return `${d} ${AYLAR[m - 1]} ${y}`;
}

export const KARAR_ADI: Record<string, string> = {
  izle: 'İzle',
  uyar: 'Uyar',
  kaydet: 'Kaydet',
  engelle: 'Engelle',
  maskele: 'Maskele',
};

/** Paragraflar boş satırla ayrılır. */
export const paragraflar = (s: string) => s.split(/\n\s*\n/).map((p) => p.trim()).filter(Boolean);
