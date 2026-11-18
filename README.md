# Korvia web sitesi

Türkçe kurumsal site + Keystatic içerik yönetim paneli (CMS).
Astro 7 · Keystatic · Korvia Kurumsal Kimlik Kılavuzu v1.0 · ui-ux-pro-max tasarım kuralları.

## Hızlı başlangıç

```bash
npm install
npm run dev
```

- Site: http://localhost:4321
- **Admin paneli: http://localhost:4321/keystatic**

Panelde yapılan her değişiklik `src/content/` altındaki YAML/Markdoc dosyalarına yazılır.

## İçerik yapısı (panelde)

| Bölüm | Ne düzenlenir |
|---|---|
| Site ayarları | Tüzel kişilik adı, e-postalar, telefon, adres, form gönderim adresi, alt bilgi, sayfa sonu çağrısı |
| Ana sayfa | Üst başlık, olay kartı, kanal örnekleri, ilkeler, modüller, kurulum |
| Sayfalar | 33 sayfa. Her sayfa bloklardan oluşur: senaryo kartı, metin, adımlar, kartlar, karar ölçeği, tablo, maskeleme örneği, not, SSS, mevzuat, ilgili sayfalar, form. Bloklar eklenip sıralanabilir. |
| Blog yazıları | Zengin metin editörüyle |
| Sözlük, SSS | Terimler ve soru grupları |

Menü otomatik oluşur: her sayfanın **Menü bölümü** ve **Menü sırası** alanları belirler.
Yeni sayfa eklemek için: Sayfalar → Ekle → "Adres" alanına ör. `sektorler/telekom` yazın.

Metinlerde `{sirketAdi}`, `{satisEposta}`, `{destekEposta}`, `{adres}` yazarsanız site ayarlarındaki değer yerleşir.

## Yayına alma (Cloudflare Workers) — güncel

Site Cloudflare Workers'ta statik olarak yayınlanır (`wrangler.jsonc`, `dist/`).

- Cloudflare → Workers & Pages → Create → Import a repository → `sayginsa/korvia-web`
- Build command: `npm run build:static` · Deploy command: `npx wrangler deploy`
- `main` dalına her push'ta Cloudflare siteyi yeniden derleyip yayınlar.
- Alan adı: Worker → Settings → Domains & Routes → `s-korvia.com` ve `www.s-korvia.com`.
- Bu modda admin paneli (/keystatic) yayında yoktur; içerik yerelde `npm run dev` ile düzenlenip push edilir.

## Yayına alma (Vercel + GitHub) — eski seçenek

Kod: https://github.com/sayginsa/korvia-web. `main` dalına her push'ta Vercel siteyi yeniden yayınlar.

1. **Vercel'e bağlayın:** vercel.com → Add New → Project → `sayginsa/korvia-web` → Deploy. Ayar gerekmez (Astro otomatik tanınır).
2. **Admin panelini açın:** yayındaki adreste `/keystatic` sayfasına gidin → "Create GitHub App" → GitHub'ın gösterdiği adımları onaylayın. Keystatic gerekli ortam değişkenlerini (`KEYSTATIC_GITHUB_CLIENT_ID`, `KEYSTATIC_GITHUB_CLIENT_SECRET`, `KEYSTATIC_SECRET`, `PUBLIC_KEYSTATIC_GITHUB_APP_SLUG`) üretir; bunları Vercel → Project → Settings → Environment Variables'a ekleyip yeniden deploy edin.
3. **Editör ekleyin:** Editörlerin `sayginsa/korvia-web` reposunda yazma yetkisi olmalı. Panelde yapılan her kayıt bir commit olur, site 1-2 dakikada güncellenir.

Yerelde `npm run dev` her zaman dosyalara yazar (GitHub gerekmez).

**Alternatif, yalnızca statik site:** `npm run build:static` → `dist/` klasörünü herhangi bir statik sunucuya (ör. Netlify Drop) yükleyin. Bu modda panel yoktur.

`SITE_URL` ortam değişkeniyle kanonik adres verilir (ör. `SITE_URL=https://www.korvia.com.tr`).

## Formlar

Formlar (demo, iletişim, iş ortaklığı, belge talebi) **Site ayarları → Form gönderim adresi**'ne JSON POST eder (Formspree, kendi API'niz vb.). Adres boşsa kullanıcının e-posta uygulaması açılır. Tüm formlarda KVKK onay kutusu vardır.

## Yayından önce doldurulacaklar

- Site ayarları: tüzel kişilik, alan adı, e-postalar, telefon, adres, form adresi
- KVKK aydınlatma metni: taslaktır, hukuk danışmanı onayı gerekir
- "Yerli/milli" ifadesi bilerek kullanılmadı (kılavuz bölüm 06: yalnızca belgeyle). Belge gelince Hakkımızda'ya eklenebilir.
- Logo yazısı Telegraf fontundadır, SVG olarak sabittir. Font lisansı alınmalıdır (kılavuz bölüm 08).

## Tasarım kuralları (özet)

- Renk: Canvas + Beyaz %65 · Mürekkep %22 · kırmızı tonları az ve kararlı. Mavi, yeşil, turuncu, degrade ve gölge yok.
- Font: başlık Manrope 800/700, gövde Inter 17/27, etiket JetBrains Mono. Fontlar siteden sunulur (üçüncü taraf istek yok).
- Karar ölçeği renkleri sabittir: İzle stone-100 · Uyar red-100 · Kaydet red-300 · Engelle Korvia Kırmızı.
- Kilit, kalkan, kurukafa, kapüşonlu figür kullanılmaz; fotoğraf yok.
- Erişilebilirlik: atlama bağlantısı, görünür odak, klavyeyle menü ve sekmeler (Esc, ok tuşları), 44 px dokunma alanı, `prefers-reduced-motion`.

## Dosyalar

```
keystatic.config.ts      İçerik modeli (panel alanları)
src/content/             Tüm içerik (YAML + Markdoc)
src/pages/               index, [...yol] (tüm sayfalar), blog/[slug]
src/components/          Üst/alt bilgi, bloklar, olay kartı, form
src/styles/global.css    Tasarım belirteçleri ve bileşen stilleri
public/logo/             Logo kitinden SVG'ler
scripts/icerik/          İlk içeriği üreten betikler (bir kez çalıştırıldı)
```
