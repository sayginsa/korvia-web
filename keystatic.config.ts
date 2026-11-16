import { config, collection, singleton, fields } from '@keystatic/core';
import { IKON_SECENEKLERI } from './src/lib/ikonlar';

const ikonAlani = (label = 'İkon') => fields.select({ label, options: IKON_SECENEKLERI, defaultValue: '' });

/*
 * Korvia web sitesi içerik modeli.
 * Yerelde: `npm run dev` → http://localhost:4321/keystatic
 * Canlıda: GitHub modu (sayginsa/korvia-web). Kurulum adımları README'de.
 */

const KARARLAR = [
  { label: 'İzle', value: 'izle' },
  { label: 'Uyar', value: 'uyar' },
  { label: 'Kaydet', value: 'kaydet' },
  { label: 'Engelle', value: 'engelle' },
  { label: 'Maskele', value: 'maskele' },
] as const;

const BOLUMLER = [
  { label: 'Platform', value: 'platform' },
  { label: 'Yapay Zekâ Güvenliği', value: 'yapay-zeka' },
  { label: 'Çözümler', value: 'cozumler' },
  { label: 'Sektörler', value: 'sektorler' },
  { label: 'Kaynaklar', value: 'kaynaklar' },
  { label: 'Kurumsal', value: 'kurumsal' },
  { label: 'Yasal (menüde görünmez)', value: 'yasal' },
] as const;

const link = (label: string) =>
  fields.object(
    {
      etiket: fields.text({ label: 'Etiket' }),
      url: fields.text({ label: 'Bağlantı (ör. /demo/)' }),
    },
    { label },
  );

const metinListesi = (label: string, itemLabel = 'Başlık') =>
  fields.array(
    fields.object({
      ikon: ikonAlani(),
      baslik: fields.text({ label: itemLabel }),
      metin: fields.text({ label: 'Metin', multiline: true }),
    }),
    { label, itemLabel: (p) => p.fields.baslik.value || 'Öğe' },
  );

const bloklar = fields.blocks(
  {
    bildirim: {
      label: 'Korvia uyarısı (sahne içinde)',
      schema: fields.object({
        eyebrow: fields.text({ label: 'Üst etiket', defaultValue: 'Kullanıcı ne görür?' }),
        baslik: fields.text({ label: 'Bölüm başlığı' }),
        aciklama: fields.text({ label: 'Açıklama', multiline: true }),
        sahne: fields.select({
          label: 'Sahne',
          options: [
            { label: 'Yapay zekâ sohbeti (tarayıcı)', value: 'yapay-zeka' },
            { label: 'USB bellek (dosya gezgini)', value: 'usb' },
            { label: 'E-posta', value: 'eposta' },
            { label: 'Bulut / web yükleme', value: 'bulut' },
            { label: 'Kod asistanı (terminal)', value: 'kod' },
          ],
          defaultValue: 'yapay-zeka',
        }),
        karar: fields.select({
          label: 'Uyarı türü',
          options: [
            { label: 'Engellendi', value: 'engelle' },
            { label: 'Gerekçe istendi', value: 'uyar' },
            { label: 'Maskelendi', value: 'maskele' },
          ],
          defaultValue: 'engelle',
        }),
        hedef: fields.text({ label: 'Hedef (ör. asistan.example)' }),
        uygulama: fields.text({ label: 'Uygulama harfi (1 karakter)', defaultValue: 'A' }),
        veriTuru: fields.text({ label: 'Tespit edilen veri türü (ör. IBAN)' }),
        veriDegeri: fields.text({ label: 'Maskelenmiş değer' }),
        dosya: fields.text({ label: 'Sahnedeki dosya adı (varsa)' }),
      }),
    },
    senaryo: {
      label: 'Senaryo kartı (veri · kullanıcı · hedef · politika · karar)',
      schema: fields.object({
        baslik: fields.text({ label: 'Senaryo cümlesi', description: 'Ör. "Bir fiyat listesi kişisel adrese gidiyor."' }),
        veri: fields.text({ label: 'Veri' }),
        kullanici: fields.text({ label: 'Kullanıcı' }),
        hedef: fields.text({ label: 'Hedef' }),
        politika: fields.text({ label: 'Politika' }),
        karar: fields.select({ label: 'Karar', options: KARARLAR, defaultValue: 'engelle' }),
        kararNotu: fields.text({ label: 'Karar notu', description: 'Ör. "durduruldu, gönderene nedeni gösterildi"' }),
      }),
    },
    metin: {
      label: 'Metin bölümü',
      schema: fields.object({
        eyebrow: fields.text({ label: 'Üst etiket' }),
        baslik: fields.text({ label: 'Başlık' }),
        govde: fields.text({ label: 'Metin (paragraflar boş satırla ayrılır)', multiline: true }),
      }),
    },
    adimlar: {
      label: 'Numaralı adımlar',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        ogeler: metinListesi('Adımlar', 'Adım'),
      }),
    },
    kartlar: {
      label: 'Kart ızgarası',
      schema: fields.object({
        eyebrow: fields.text({ label: 'Üst etiket' }),
        baslik: fields.text({ label: 'Başlık' }),
        aciklama: fields.text({ label: 'Açıklama', multiline: true }),
        ogeler: metinListesi('Kartlar'),
      }),
    },
    karar: {
      label: 'Karar ölçeği (İzle · Uyar · Kaydet · Engelle)',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        aciklama: fields.text({ label: 'Açıklama', multiline: true }),
        izle: fields.text({ label: 'İzle açıklaması' }),
        uyar: fields.text({ label: 'Uyar açıklaması' }),
        kaydet: fields.text({ label: 'Kaydet açıklaması' }),
        engelle: fields.text({ label: 'Engelle açıklaması' }),
      }),
    },
    tablo: {
      label: 'Tablo',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        aciklama: fields.text({ label: 'Açıklama', multiline: true }),
        sutunlar: fields.array(fields.text({ label: 'Sütun başlığı' }), {
          label: 'Sütunlar',
          itemLabel: (p) => p.value || 'Sütun',
        }),
        satirlar: fields.array(
          fields.object({
            hucreler: fields.array(fields.text({ label: 'Hücre' }), { label: 'Hücreler', itemLabel: (p) => p.value }),
          }),
          { label: 'Satırlar', itemLabel: (p) => p.fields.hucreler.elements[0]?.value || 'Satır' },
        ),
      }),
    },
    maskeleme: {
      label: 'Maskeleme örneği (önce / sonra)',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        once: fields.text({ label: 'Kullanıcının yazdığı', multiline: true }),
        sonra: fields.text({ label: 'Yapay zekâ aracına giden', multiline: true }),
        not: fields.text({ label: 'Not' }),
      }),
    },
    not: {
      label: 'Vurgu notu',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        metin: fields.text({ label: 'Metin', multiline: true }),
        link: link('Bağlantı (isteğe bağlı)'),
      }),
    },
    sss: {
      label: 'Soru · cevap',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        ogeler: fields.array(
          fields.object({
            soru: fields.text({ label: 'Soru' }),
            cevap: fields.text({ label: 'Cevap', multiline: true }),
          }),
          { label: 'Sorular', itemLabel: (p) => p.fields.soru.value || 'Soru' },
        ),
      }),
    },
    mevzuat: {
      label: 'İlgili mevzuat',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        ogeler: metinListesi('Mevzuat', 'Mevzuat adı'),
      }),
    },
    ilgili: {
      label: 'İlgili sayfalar',
      schema: fields.object({
        baslik: fields.text({ label: 'Başlık' }),
        sayfalar: fields.array(fields.relationship({ label: 'Sayfa', collection: 'sayfalar' }), {
          label: 'Sayfalar',
          itemLabel: (p) => p.value || 'Sayfa',
        }),
      }),
    },
    form: {
      label: 'Form',
      schema: fields.object({
        tur: fields.select({
          label: 'Form türü',
          options: [
            { label: 'Demo talebi', value: 'demo' },
            { label: 'İletişim', value: 'iletisim' },
            { label: 'İş ortaklığı başvurusu', value: 'is-ortakligi' },
            { label: 'Güvenlik belgesi talebi', value: 'belge' },
          ],
          defaultValue: 'iletisim',
        }),
        baslik: fields.text({ label: 'Başlık' }),
        aciklama: fields.text({ label: 'Açıklama', multiline: true }),
        secenekBasligi: fields.text({ label: 'Seçenek sorusu' }),
        secenekler: fields.array(fields.text({ label: 'Seçenek' }), {
          label: 'Seçenekler',
          itemLabel: (p) => p.value,
        }),
        mesajEtiketi: fields.text({ label: 'Mesaj alanı etiketi' }),
        gonderEtiketi: fields.text({ label: 'Gönder butonu metni' }),
      }),
    },
  },
  { label: 'Sayfa blokları' },
);

export default config({
  // Yerelde (npm run dev) dosyalara yazar. Canlıda GitHub'a commit atar:
  // editörler GitHub hesabıyla girer, her kayıt sayginsa/korvia-web'e bir commit olur ve Vercel siteyi yeniden yayınlar.
  storage: import.meta.env.PROD
    ? { kind: 'github', repo: 'sayginsa/korvia-web' }
    : { kind: 'local' },
  locale: 'tr-TR',
  ui: {
    brand: { name: 'Korvia · İçerik' },
    navigation: {
      'Site': ['anasayfa', 'ayarlar'],
      'İçerik': ['sayfalar', 'blog', 'sozluk', 'sss'],
    },
  },
  singletons: {
    ayarlar: singleton({
      label: 'Site ayarları',
      path: 'src/content/ayarlar',
      format: { data: 'yaml' },
      schema: {
        sirketAdi: fields.text({ label: 'Şirket adı (yasal)' }),
        aciklamaSatiri: fields.text({ label: 'Açıklama satırı', defaultValue: 'Veri & Yapay Zekâ Güvenliği' }),
        satisEposta: fields.text({ label: 'Satış e-postası' }),
        destekEposta: fields.text({ label: 'Destek e-postası' }),
        telefon: fields.text({ label: 'Telefon' }),
        adres: fields.text({ label: 'Adres', multiline: true }),
        formAdresi: fields.text({
          label: 'Form gönderim adresi (endpoint)',
          description: 'Formların POST edileceği URL (ör. Formspree, kendi API\'niz). Boşsa formlar e-posta istemcisini açar.',
        }),
        footerMetni: fields.text({ label: 'Alt bilgi açıklaması', multiline: true }),
        demoEtiketi: fields.text({ label: 'Demo butonu metni', defaultValue: 'Demo isteyin' }),
        kapanisBaslik: fields.text({ label: 'Sayfa sonu çağrı başlığı' }),
        kapanisMetin: fields.text({ label: 'Sayfa sonu çağrı metni', multiline: true }),
      },
    }),
    anasayfa: singleton({
      label: 'Ana sayfa',
      path: 'src/content/anasayfa',
      format: { data: 'yaml' },
      schema: {
        seoBaslik: fields.text({ label: 'SEO başlığı' }),
        seoAciklama: fields.text({ label: 'SEO açıklaması', multiline: true }),
        eyebrow: fields.text({ label: 'Üst etiket' }),
        baslik: fields.text({ label: 'Ana başlık' }),
        ozet: fields.text({ label: 'Özet', multiline: true }),
        birincilCta: link('Birincil buton'),
        ikincilCta: link('İkincil buton'),
        olay: fields.object(
          {
            kategori: fields.text({ label: 'Kategori' }),
            cumle: fields.text({ label: 'Olay cümlesi' }),
            dosya: fields.text({ label: 'Dosya' }),
            icerik: fields.text({ label: 'İçerik (virgülle)' }),
            hedef: fields.text({ label: 'Hedef' }),
            karar: fields.select({ label: 'Karar', options: KARARLAR, defaultValue: 'engelle' }),
            kullaniciMesaji: fields.text({ label: 'Kullanıcının gördüğü mesaj', multiline: true }),
          },
          { label: 'Üst bölümdeki olay kartı' },
        ),
        kanalBaslik: fields.text({ label: 'Kanal bölümü başlığı' }),
        kanalAciklama: fields.text({ label: 'Kanal bölümü açıklaması', multiline: true }),
        kanallar: fields.array(
          fields.object({
            ad: fields.text({ label: 'Kanal' }),
            hedef: fields.text({ label: 'Hedef etiketi' }),
            once: fields.text({ label: 'Gönderilen', multiline: true }),
            sonra: fields.text({ label: 'Çıkan', multiline: true }),
          }),
          { label: 'Kanallar', itemLabel: (p) => p.fields.ad.value },
        ),
        ilkeBaslik: fields.text({ label: 'İlkeler başlığı' }),
        ilkeAciklama: fields.text({ label: 'İlkeler açıklaması', multiline: true }),
        ilkeler: metinListesi('İlkeler'),
        moduller: fields.array(
          fields.object({
            eyebrow: fields.text({ label: 'Üst etiket' }),
            baslik: fields.text({ label: 'Başlık' }),
            metin: fields.text({ label: 'Metin', multiline: true }),
            maddeler: fields.array(fields.text({ label: 'Madde' }), { label: 'Maddeler', itemLabel: (p) => p.value }),
            link: link('Bağlantı'),
          }),
          { label: 'Modül bölümleri', itemLabel: (p) => p.fields.baslik.value },
        ),
        kapiBaslik: fields.text({ label: '"Tek kapı" bölümü başlığı' }),
        kapiMetin: fields.text({ label: '"Tek kapı" bölümü metni', multiline: true }),
        dagitimBaslik: fields.text({ label: 'Kurulum başlığı' }),
        dagitimMetin: fields.text({ label: 'Kurulum metni', multiline: true }),
        dagitimSecenekleri: metinListesi('Kurulum seçenekleri'),
        pocNot: fields.text({ label: 'POC notu' }),
      },
    }),
    sss: singleton({
      label: 'Sık sorulan sorular',
      path: 'src/content/sss',
      format: { data: 'yaml' },
      schema: {
        baslik: fields.text({ label: 'Başlık' }),
        ozet: fields.text({ label: 'Özet', multiline: true }),
        gruplar: fields.array(
          fields.object({
            ad: fields.text({ label: 'Grup adı' }),
            sorular: fields.array(
              fields.object({
                soru: fields.text({ label: 'Soru' }),
                cevap: fields.text({ label: 'Cevap', multiline: true }),
              }),
              { label: 'Sorular', itemLabel: (p) => p.fields.soru.value },
            ),
          }),
          { label: 'Gruplar', itemLabel: (p) => p.fields.ad.value },
        ),
      },
    }),
  },
  collections: {
    sayfalar: collection({
      label: 'Sayfalar',
      path: 'src/content/sayfalar/*',
      slugField: 'kimlik',
      format: { data: 'yaml' },
      columns: ['kimlik', 'yol'],
      schema: {
        kimlik: fields.slug({ name: { label: 'Sayfa adı (menüde görünür)' } }),
        yol: fields.text({ label: 'Adres', description: 'Baştaki ve sondaki "/" olmadan. Ör. platform/dlp/uc-nokta' }),
        bolum: fields.select({ label: 'Menü bölümü', options: BOLUMLER, defaultValue: 'platform' }),
        sira: fields.integer({ label: 'Menü sırası', defaultValue: 10 }),
        ikon: ikonAlani('Menü ikonu'),
        menuAciklama: fields.text({ label: 'Kısa açıklama (menü ve ilgili sayfa kartlarında)' }),
        seoBaslik: fields.text({ label: 'SEO başlığı' }),
        seoAciklama: fields.text({ label: 'SEO açıklaması', multiline: true }),
        eyebrow: fields.text({ label: 'Üst etiket' }),
        baslik: fields.text({ label: 'Başlık' }),
        ozet: fields.text({ label: 'Özet', multiline: true }),
        cta: link('Üst buton'),
        bloklar,
      },
    }),
    blog: collection({
      label: 'Blog yazıları',
      path: 'src/content/blog/*',
      slugField: 'baslik',
      format: { contentField: 'icerik' },
      entryLayout: 'content',
      columns: ['baslik', 'tarih'],
      schema: {
        baslik: fields.slug({ name: { label: 'Başlık' } }),
        kategori: fields.select({
          label: 'Kategori',
          options: [
            { label: 'Yapay Zekâ Güvenliği', value: 'Yapay Zekâ Güvenliği' },
            { label: 'Veri Koruma', value: 'Veri Koruma' },
            { label: 'Uyum', value: 'Uyum' },
          ],
          defaultValue: 'Veri Koruma',
        }),
        tarih: fields.date({ label: 'Yayın tarihi' }),
        sure: fields.integer({ label: 'Okuma süresi (dk)', defaultValue: 3 }),
        ozet: fields.text({ label: 'Özet', multiline: true }),
        icerik: fields.markdoc({ label: 'İçerik' }),
      },
    }),
    sozluk: collection({
      label: 'Sözlük',
      path: 'src/content/sozluk/*',
      slugField: 'terim',
      format: { data: 'yaml' },
      schema: {
        terim: fields.slug({ name: { label: 'Terim' } }),
        sira: fields.integer({ label: 'Sıra', defaultValue: 10 }),
        tanim: fields.text({ label: 'Tanım', multiline: true }),
        ilgiliYol: fields.text({ label: 'Korvia\'daki karşılığı (adres)' }),
        ilgiliEtiket: fields.text({ label: 'Bağlantı metni' }),
      },
    }),
  },
});
