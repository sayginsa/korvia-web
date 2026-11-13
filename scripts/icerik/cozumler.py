from ortak import *

UYARI = 'Korvia bu gereksinimleri teknik kontrollerle destekler. Hukuki yorum hukuk danışmanınıza aittir.'


def kurulum_notu(metin_):
    return notkutu('Hangi kurulum uygun?', metin_, 'Kurulum seçenekleri', '/platform/kurulum/')


# ---------------- Çözümler ----------------
sayfa('golge-yapay-zeka', 'Gölge yapay zekâ', 'cozumler/golge-yapay-zeka', 'cozumler', 1,
      'Onaysız yapay zekâ araçlarını veri açığa çıkmadan bulun.',
      'Çözümler · Gölge yapay zekâ', 'Gölge yapay zekâyı veri açığa çıkmadan keşfedin.',
      'Çalışanlar yapay zekâ araçlarını güvenlik ekibi onaylamadan çok önce kullanmaya başlar. Korvia tarayıcıda ve masaüstünde kullanılan her yapay zekâ servisini ortaya çıkarır, kişisel hesabı kurumsal kiracıdan ayırır ve hassas verinin yönetilmeyen dil modellerine sızmasını durdurur.',
      [
          senaryo('Bütçe dosyası onaysız bir yapay zekâ aracına gidiyor.', 'Gelecek yılın bütçe dosyası', 'Finans analisti',
                  'Tarayıcıdaki onaysız yapay zekâ aracı', 'Finansal veri: yalnızca onaylı yapay zekâ araçları', 'uyar', 'gerekçe istendi, ardından kaydedildi'),
          metin('Güvenliğin hiç onaylamadığı yapay zekâ aracı.',
                'Bir çalışan kurum içi belgeleri özetlemek için kişisel yapay zekâ hesabını kullanır. Etkinlik verimli olabilir ama iş bilgisinin nerede paylaşıldığı konusunda belirsizlik yaratır.\n\nKorvia tarayıcılarda ve uç noktalarda onaysız yapay zekâ araçlarını ortaya çıkarır, hangi hassas verinin paylaşıldığını gösterir ve hesaba duyarlı maskeleme veya engelleme politikaları uygular.'),
          kartlar('Üç adım', [
              ('Kullanımı anlayın', 'Tarayıcıda ve masaüstünde kullanılan her yapay zekâ servisini kullanıcı ve hesap türüne göre görün.'),
              ('Veri riskini belirleyin', 'Kişisel veri, kaynak kod veya finansal veri içeren komutları ve yüklemeleri tespit edin.'),
              ('Yönetişim uygulayın', 'Kurumsal kiracılara izin verin, hassas değerleri satır içinde maskeleyin, onaysız araçları engelleyin.'),
          ]),
          ilgili('yapay-zeka-veri-guvenligi', 'yapay-zeka-guvenlik-duvari', 'uc-nokta-dlp', baslik='Korvia\'nın hangi parçaları bunu yapar?'),
          notkutu('Nereden başlamalı?', 'Yalnızca görünürlükle: yapay zekâ kullanımının ve ilgili hassas verinin envanteri, hiçbir engelleme açılmadan.', 'POC rehberi', '/kaynaklar/poc-rehberi/'),
          mevzuat('kvkk', 'cbigr'),
      ])

sayfa('fikri-mulkiyet', 'Fikri mülkiyetin korunması', 'cozumler/fikri-mulkiyet', 'cozumler', 2,
      'Tasarımları, kaynak kodu, formülleri ve fiyat modellerini koruyun.',
      'Çözümler · Fikri mülkiyet', 'Sizi farklı kılan bilgiyi koruyun.',
      'Fikri mülkiyet patentlerle sınırlı değildir. Ürün tasarımları, kaynak kod, fiyat modelleri, formüller, mühendislik dosyaları ve gizli iş planları da korunması gereken değerli bilgilerdir.',
      [
          senaryo('Bir CAD montajı kişisel bulut sürücüye gidiyor.', 'Parmak izi alınmış CAD montajı', 'Tasarım mühendisi',
                  'Kişisel bulut sürücü', 'Mühendislik fikri mülkiyeti: yalnızca kurum depolaması', 'engelle', 'kısmi kopya tanındı'),
          metin('Hangi bilginin korunması gerektiğini bilin.',
                'Bir mühendislik belgesi tescilli tasarım ayrıntıları içerebilir. Bir geliştirme deposu gizli kod barındırabilir. Ticari bir tablo hassas fiyatlandırma stratejilerini açığa çıkarabilir.\n\nKorvia kritik depoların, CAD çizimlerinin ve finansal modellerin parmak izini alır; tamamı veya bir kısmı USB, kişisel bulut, e-posta veya yapay zekâ komutlarıyla çıkmadan önce yakalanır.\n\nÇalışanların iş birliği yapması, dosya göndermesi ve dış ortaklarla çalışması gerekir. Amaç meşru işi durdurmak değil, gizli bilginin kurum politikasına aykırı biçimde ele alındığı anı tanımaktır.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Tespit Motoru', 'Depoların tamamının parmak izini alın, kısmi kopyaları tanıyın.'),
              ('Veri Sınıflandırma', 'Yeniden adlandırma, dönüştürme ve kopyalamada dosyayla kalan etiketler.'),
              ('Kod asistanları', 'Kaynak kod, politikanızın izin vermediği komutlardan uzak durur.'),
              ('Uç Nokta DLP', 'USB bellekler, yüklemeler ve eşitleme klasörleri aynı kurala uyar.'),
          ]),
          kurulum_notu('Kurum içi. Mühendislik veriniz ve onunla ilgili kanıt ağınızın içinde kalır.'),
          mevzuat('iso'),
      ])

sayfa('iceriden-gelen-risk', 'İçeriden gelen risk', 'cozumler/iceriden-gelen-risk', 'cozumler', 3,
      'Ayrılan çalışanların veya ele geçirilmiş hesapların veri kaçırmasını durdurun.',
      'Çözümler · İçeriden gelen risk', 'İçeriden gelen risk çoğu zaman sıradan iş gibi görünür.',
      'Her veri kaybı olayı dışarıdan bir saldırganla yaşanmaz. Hassas bilgi, zaten meşru erişimi olan biri tarafından kopyalanabilir, iletilebilir veya aktarılabilir. Korvia dosya sınıflandırmasını, uç nokta etkinliğini ve olağan dışı hareket hacmini ilişkilendirir; güvenlik ekipleri ayrılan çalışanların veya ele geçirilmiş hesapların veri kaçırmasını durdurur.',
      [
          senaryo('Ayrılan bir çalışan gizli müşteri verisini kopyalıyor.', 'Hesap listesi, Gizli', 'Ayrılan satış temsilcisi',
                  'USB bellek', 'Gizli veri aktarım politikası', 'engelle', 'durduruldu, olay kaydedildi'),
          metin('Bir politika ihlali kötü niyetin kanıtı değildir.',
                'Bir çalışan bir veri koruma kuralını yanlışlıkla veya meşru bir işi yaparken tetikleyebilir. Güvenlik ekiplerinin olayı adil değerlendirmek için yeterli bağlama ihtiyacı vardır.\n\nKorvia inceleyenlere söz konusu veriyi, gerçekleşen etkinliği ve uygulanan sonucu göstererek politikaya dayalı incelemeyi destekler.'),
          kartlar('Korvia içeriden gelen risk incelemelerini nasıl destekler?', [
              ('İnceleme', 'Dosyanın tüm zaman çizelgesi: hassas veriyi kim açtı, yeniden adlandırdı, arşivledi veya dışarı çıkarmaya çalıştı.'),
              ('Uç Nokta DLP', 'Dizüstü bilgisayarlar ağ dışındayken bile USB belleği, kişisel bulut yüklemelerini, yazdırmayı ve pano yapıştırmalarını denetleyin.'),
              ('Veri Sınıflandırma', 'Etiketler yeniden adlandırmada ve biçim değişikliklerinde dosyayla gider; politikalar her zaman tetiklenir.'),
          ]),
          kurulum_notu('Kurum içi veya özel bulut. Hassas olay kanıtı ve çalışan etkinlik kayıtları rol tabanlı erişimle kendi altyapınızda kalır.'),
          mevzuat('kvkk', 'iso'),
          sss('İçeriden gelen risk hakkında sorular', [
              ('Her DLP politika ihlali içeriden tehdit midir?', 'Hayır. Çalışanlar veri koruma politikalarını yanlışlıkla veya meşru iş sırasında tetikleyebilir. İnceleyenler bir olayın yanlışlıkla ifşa mı, politika sorunu mu, yoksa kötü niyetli etkinlik mi olduğuna karar vermeden önce tüm bağlamı değerlendirmelidir.'),
              ('Çalışan izlemesi KVKK açısından nasıl ele alınmalı?', 'Korvia içeriği yalnızca bir politika eşleştiğinde kaydeder ve erişimi rol bazında sınırlar. Çalışanların aydınlatılması ve işleme şartlarının belirlenmesi kurumunuzun sorumluluğundadır; bu konuda hukuk danışmanınızın görüşünü alın.'),
          ]),
      ])

sayfa('uyum-ve-denetim', 'Uyum ve denetim', 'cozumler/uyum-ve-denetim', 'cozumler', 4,
      'Kişisel veri envanteri, tutarlı politika ve imzalı kanıt.',
      'Çözümler · Uyum ve denetim', 'Veri koruma kararlarını açıklamayı kolaylaştırın.',
      'Güvenlik ve uyum ekipleri hassas bilginin nasıl tanındığını, korunduğunu ve olaylarda nasıl ele alındığını göstermek zorundadır. Korvia güncel kişisel veri envanteri, tutarlı politika uygulaması ve kriptografik olarak imzalanmış olay kayıtlarıyla KVKK, BDDK, SPK, PCI DSS ve ISO 27001 denetimlerine hazırlığı kolaylaştırır.',
      [
          senaryo('Bir dizüstü bilgisayarda kart numaraları çıkıyor.', 'Kart numaraları içeren döküm', 'Destek analisti',
                  'İndirilenler klasörü', 'Onaylı sistemler dışında kart verisi', 'kaydet', 'vaka açıldı, kanıt saklandı'),
          metin('Kanıt alarmdan fazlasıdır.',
                'Denetçiler iki şey ister: koyduğunuz kurallar ve bunların çalıştığının kanıtı. Korvia etkin sınıflandırma ve DLP politikalarınızı kriptografik olarak imzalanmış olay kayıtları ve kişisel veri envanterleriyle eşleştirir. Denetçilere ham hassas dosyaları göstermeden doğrulanabilir kanıt sunarsınız.'),
          kartlar('Üç kanıt katmanı', [
              ('Politikalar', 'Sınıflandırma ve DLP kurallarını düzenleyici kontrollerle doğrudan eşleyin.'),
              ('Olaylar', 'Neyin eşleştiğini, hangi kuralın tetiklendiğini ve hangi eylemin uygulandığını gösteren imzalı, değiştirilemez kayıtlar üretin.'),
              ('Değerlendirmeler', 'İç ve dış denetçilere ham hassas içeriği göstermeden rol tabanlı rapor erişimi verin.'),
          ]),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Veri Keşfi ve DSPM', 'Uç noktalarda, sunucularda ve bulut sürücülerde kişisel veri envanteri.'),
              ('DLP', 'Düzenlemeye tabi verinin uç nokta, e-posta, web, bulut ve yapay zekâda nereye gidebileceğini tek politika belirler.'),
              ('İnceleme', 'İmzalı kanıt ve vakalar; denetçiler için rol tabanlı erişim.'),
          ]),
          kurulum_notu('Kurum içi. İçerik ve kanıt ağınızda kalır; bu çoğu zaman veri yerelliği sorusunu da kapatır.'),
          mevzuat('kvkk', 'bddk', 'spk', 'pci', 'iso'),
          notkutu('"Destekler" ne demek?', UYARI),
      ])

# ---------------- Sektörler ----------------
sayfa('finans', 'Finans', 'sektorler/finans', 'sektorler', 1,
      'Bankalar, sigorta ve ödeme kuruluşları.',
      'Sektörler · Finans', 'Düzenleyici kanıt ister. Müşteri, verisinin yerinde kalmasını.',
      'Bankalar, sigorta şirketleri ve ödeme kuruluşları BDDK, SPK ve PCI DSS gereksinimleriyle ve verinin nerede tutulabileceğine dair kurallarla çalışır. Korvia ağınızın içinde çalışır ve her olay için imzalı kanıt saklar.',
      [
          senaryo('Bir kart verisi dökümü kişisel adrese gidiyor.', 'Kart verisi dökümü', 'Ödeme sistemleri analisti',
                  'Kişisel e-posta adresi', 'Kart verisi: yalnızca onaylı sistemler', 'engelle', 'durduruldu, gönderene nedeni gösterildi'),
          metin('Finansal bilgiyi gündelik iş akışlarında koruyun.',
                'Analistler, danışmanlar ve operasyon ekipleri her gün ana bankacılık dökümleri, kart verisi (PAN), IBAN listeleri, birleşme ve satın alma modelleri ve kredi dosyalarıyla çalışır. Yanlış adreslenmiş tek bir e-posta, onaysız bir bulut yüklemesi veya bir yapay zekâ komutu bildirim gerektiren bir ihlale dönüşebilir.\n\nKorvia müşteri ve kart kayıtlarınızı birebir veri eşleştirme (EDM) ve sağlama doğrulamasıyla yerel olarak dizinler. Uç nokta, e-posta, web ve yapay zekâda izinsiz aktarımları durdururken tüm incelemeyi ve imzalı denetim kanıtını ağınızın içinde tutar.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Ağ ve E-posta DLP', 'Giden posta ve yüklemeler çıkmadan kontrol edilir.'),
              ('Tespit Motoru', 'Kendi müşteri ve kart kayıtlarınıza karşı birebir veri eşleştirme.'),
              ('İnceleme', 'Denetçiler için imzalı kanıt ve vaka zaman çizelgeleri.'),
              ('Kurulum', 'Kurum içinde, kendi ağınızda.'),
          ]),
          kurulum_notu('Kurum içi; gerektiği yerde yalıtılmış ağ güncellemeleri ve SIEM\'inize gönderilen olaylarla.'),
          mevzuat('bddk', 'spk', 'pci', 'kvkk'),
      ])

sayfa('saglik', 'Sağlık', 'sektorler/saglik', 'sektorler', 2,
      'Hastaneler, klinikler ve laboratuvarlar.',
      'Sektörler · Sağlık', 'Hasta kayıtları gün boyu hareket eder. Kaybolmaları işin parçası değildir.',
      'Klinik personel kayıtları e-postayla gönderir, yazdırır ve ekranların fotoğrafını çeker. Korvia servisi durdurmadan politika uygular; bir kaydın taşınması gerektiğinde gerekçe ister.',
      [
          senaryo('Bir epikriz sevk eden kliniğe gidiyor.', 'Epikriz raporu', 'Hemşire', 'Sevk eden klinik',
                  'Hasta kayıtları: gerekçe zorunlu', 'uyar', 'gerekçe kaydedildi'),
          metin('Bakımı aksatmadan hassas bilgiyi koruyun.',
                'Hastaneler, klinikler ve laboratuvarlar sürekli epikriz, tahlil sonucu, görüntüleme ve sigorta dosyası alışverişi yapar. Klinik personeli doğrudan engellemek hasta bakımını aksatır; denetlenmeyen USB bellekler, kişisel web postası ve çıktılar ise özel nitelikli sağlık verisini açığa çıkarır.\n\nKorvia tıbbi tanımlayıcıları, T.C. kimlik numaralarını ve OCR ile taranmış belgeleri tanır. Yetkili sevklerin kayıtlı bir klinik gerekçeyle ilerlemesine izin verirken çıkarılabilir belleklere, kişisel bulut hesaplarına veya herkese açık yapay zekâ araçlarına izinsiz aktarımı engeller.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Uç Nokta DLP', 'E-posta, yazdırma ve pano tek politikaya uyar.'),
              ('Tespit Motoru', 'Tıbbi kayıt biçimlerini ve tanımlayıcıları tanır.'),
              ('İnceleme', 'Kimin neyi, neden gönderdiğinin kaydı.'),
          ]),
          kurulum_notu('Kurum içi veya özel bulut; hasta verisi sizin denetlediğiniz altyapıda kalır.'),
          mevzuat('kvkk', 'saglik'),
      ])

sayfa('uretim', 'Üretim', 'sektorler/uretim', 'sektorler', 3,
      'CAD dosyaları, formüller ve tedarikçi fiyatları.',
      'Sektörler · Üretim', 'Ürün çizimlerin içindedir.',
      'Üreticiler için hassas veri tekniktir: CAD dosyaları, formüller, tedarikçi fiyatları ve test sonuçları. Korvia bunları tanır ve nereye gidebileceklerini denetler.',
      [
          senaryo('Test sonuçları bir tedarikçi portalına gidiyor.', 'Yeni bir parçanın test sonuçları', 'Kalite mühendisi',
                  'Tedarikçi portalı', 'Mühendislik verisi: yalnızca onaylı ortaklar', 'uyar', 'gerekçe istendi'),
          metin('Mühendislik bilgisini ve operasyonel veriyi koruyun.',
                'Üretimde rekabet avantajı yapısal olmayan dosyalarda yaşar: CAD montajları, ürün ağaçları (BOM), kimyasal formüller, PLC/SCADA yapılandırmaları ve tedarikçi fiyat matrisleri. Standart kalıplar çalınmış bir çizimi veya bir test raporunun kısmi kopyasını tanıyamaz.\n\nKorvia mühendislik depolarınızın parmak izini alır ve dosya yeniden adlandırılsa da kalan etiketler uygular. Tedarikçi portallarına, üretim sahasındaki USB belleklere ve dış bulut depolamaya aktarımları denetler.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Tespit Motoru', 'Mühendislik depolarının parmak izini alın, kısmi kopyaları tanıyın.'),
              ('Uç Nokta DLP', 'Tasarım ofisinde ve üretim sahasında USB bellekler ve eşitleme klasörleri.'),
              ('Bulut DLP', 'Her bulut uygulaması için yükleme ve paylaşım kuralları.'),
          ]),
          kurulum_notu('Kurum içi; internet bağlantısı olmayan sahalar dahil.'),
          mevzuat('iso', 'kvkk'),
      ])

sayfa('kamu', 'Kamu', 'sektorler/kamu', 'sektorler', 4,
      'Bakanlıklar, belediyeler ve kamu kurumları.',
      'Sektörler · Kamu', 'Vatandaş verisi, sizin altyapınızda.',
      'Kamu kurumları kimlik belgeleri, vergi ve sosyal güvenlik kayıtlarıyla çalışır ve çoğu zaman yurt dışında barındırılan servisleri kullanamaz. Korvia kendi altyapınızda, internet bağlantısı olsun olmasın çalışır.',
      [
          senaryo('Bir T.C. kimlik numarası listesi kişisel bulut sürücüye gidiyor.', 'Vatandaş T.C. kimlik numarası listesi', 'Dosya sorumlusu',
                  'Kişisel bulut sürücü', 'Vatandaş verisi: yalnızca kurum içi sistemler', 'engelle', 'durduruldu, nedeni gösterildi'),
          metin('Kamu hizmetlerinde hassas bilgiyi koruyun.',
                'Bakanlıklar, belediyeler ve kamu kurumları T.C. kimlik numaralarını, vergi beyannamelerini, sosyal yardım kayıtlarını ve ihale belgelerini sıkı veri egemenliği şartlarıyla işler. Üst veriyi veya içeriği yurt dışına yönlendiren yalnızca bulut tabanlı güvenlik araçları çoğu zaman söz konusu bile olamaz.\n\nKorvia tamamen kurum içinde veya internetten yalıtılmış ağlarda kurulur. Sağlama doğrulamalı T.C. kimlik tespitini, otomatik sınıflandırmayı ve imzalı denetim izlerini KVKK ve Bilgi ve İletişim Güvenliği Rehberi çalışmalarınız için bir araya getirir.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Kurulum', 'Kendi altyapınızda bir cihaz; gerektiğinde yalıtılmış ağda.'),
              ('Veri Keşfi ve DSPM', 'Kişisel veri mevzuatının istediği kişisel veri envanteri.'),
              ('Tespit Motoru', 'T.C. kimlik ve vergi numaraları yalnızca biçimle değil sağlama doğrulamasıyla kontrol edilir.'),
          ]),
          kurulum_notu('Kurum içi. Siz açmadıkça ağınızdan hiçbir şey çıkmaz.'),
          mevzuat('kvkk', 'cbigr'),
      ])

sayfa('hukuk', 'Hukuk', 'sektorler/hukuk', 'sektorler', 5,
      'Hukuk büroları ve danışmanlık şirketleri.',
      'Sektörler · Hukuk', 'Müvekkil dosyaları gizli kalır. Her müvekkil de farklıdır.',
      'Hukuk büroları ve danışmanlık şirketleri dosyaları ve gizli yazışmaları korurken çalışanları taslak ve özet için yapay zekâ kullanıyor. Korvia araçları yasaklamadan nelerin girdiğini denetler.',
      [
          senaryo('Bir müvekkil sözleşmesinden madde herkese açık bir yapay zekâ aracına gidiyor.', 'Müvekkil sözleşmesinden bir madde',
                  'Avukat', 'Herkese açık yapay zekâ aracı', 'Müvekkil belgeleri: yalnızca onaylı araçlar', 'uyar', 'onaylı araç önerildi'),
          metin('Gizli müvekkil ve dosya bilgisini koruyun.',
                'Avukatlar ve ortaklar yüzlerce müvekkil dosyasında çalışır: sözleşme taslağı hazırlar, birleşme ve satın alma veri odalarını inceler ve giderek daha çok dilekçe özetlemek için dil modellerini kullanır. Gizli tek bir maddeyi herkese açık bir yapay zekâ aracına yapıştırmak veya yanlış müvekkilin dosyasını e-postaya eklemek, müvekkil güvenini sarsar.\n\nKorvia belgeleri müvekkile veya dosyaya göre etiketler, hassas sözleşmelerin tek bir paragrafa kadar parmak izini alır ve gizli maddeleri onaysız yapay zekâ araçlarına veya kişisel e-postaya ulaşmadan maskeler ya da engeller.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Yapay Zekâ Veri Güvenliği', 'Onaylı asistana izin verin, diğerlerine nelerin ulaştığını denetleyin.'),
              ('Tespit Motoru', 'Parmak izleri yalnızca kopyalanan dosyayı değil, kopyalanan maddeyi de tanır.'),
              ('Veri Sınıflandırma', 'Kendi kurallarınızla müvekkile veya dosyaya göre etiketler.'),
          ]),
          kurulum_notu('Yönetilen hizmet veya özel bulut; Yapay Zekâ Veri Güvenliği baştan açık.'),
          mevzuat('kvkk', 'iso'),
      ])

sayfa('perakende', 'Perakende', 'sektorler/perakende', 'sektorler', 6,
      'Mağazalar, e-ticaret ve çağrı merkezleri.',
      'Sektörler · Perakende', 'Her mağaza, müşteri verisi için bir çıkış kapısıdır.',
      'Perakende; yüksek personel değişimi, çok sayıda uç nokta ve büyük müşteri listeleri demektir. Korvia müşteri ve kart verisini bulur; genel müdürlük ve tüm mağazalar için tek politikayı tek konsoldan yönetir.',
      [
          senaryo('Ayrılan bir mağaza müdürü sadakat listesini USB\'ye kopyalıyor.', 'Sadakat programı listesi', 'Ayrılan mağaza müdürü',
                  'USB bellek', 'Müşteri verisi: çıkarılabilir bellek yok', 'engelle', 'durduruldu, vaka açıldı'),
          metin('Müşteri ve ticari veriyi koruyun.',
                'Perakendeciler ve e-ticaret markaları mağazalarda ve çağrı merkezlerinde yüksek personel değişimini büyük sadakat veritabanları, ödeme kayıtları ve sezonluk fiyat tablolarıyla bir arada yaşar. Ayrılan çalışanlar ve ortak kullanılan arka ofis bilgisayarları sürekli sızıntı yolları oluşturur.\n\nKorvia uç noktalarda ve paylaşımlarda unutulmuş kart ve sadakat dökümlerini bulur, USB ve kişisel web postası üzerinden veri kaçırmayı engeller ve genel müdürlük güvenlik ekibine tüm lokasyonları yönetebileceği tek konsol verir.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Uç Nokta DLP', 'Arka ofis bilgisayarları ve genel müdürlük tek politikaya uyar.'),
              ('İnceleme', 'Ayrılan personel bilinen bir örüntüdür; kanıt saklanır.'),
              ('Veri Keşfi ve DSPM', 'Kart ve sadakat verisini biriktiği her yerde bulun.'),
          ]),
          kurulum_notu('Platform ekibi olmayan perakendeciler için yönetilen hizmet; kurum içi kurulum her şeyi içeride tutar.'),
          mevzuat('pci', 'kvkk'),
      ])

sayfa('enerji', 'Enerji', 'sektorler/enerji', 'sektorler', 7,
      'Enerji, su ve telekom; yalıtılmış ağlar.',
      'Sektörler · Enerji', 'Kritik veri, buluta hiç dokunmayan ağlarda.',
      'Enerji, su ve telekom için bir sızıntı finansal kayıptan fazlasıdır. Korvia kapalı ağlarda çalışır; şebeke haritalarını, tesis planlarını ve SCADA yapılandırmalarını korur.',
      [
          senaryo('Bir SCADA dosyası USB belleğe gidiyor.', 'SCADA yapılandırma dosyası', 'Operasyon mühendisi',
                  'OT iş istasyonundaki USB bellek', 'Tesis verisi: çıkarılabilir bellek yok', 'engelle', 'durduruldu, bulut bağlantısı gerekmedi'),
          metin('Hassas operasyonel ve ticari bilgiyi koruyun.',
                'Elektrik dağıtım şirketleri, petrol ve gaz işletmeleri ve su idareleri; şebeke topolojilerini, SCADA yapılandırmalarını, tesis şemalarını ve teklif modellerini internet bağlantısının kısıtlı veya hiç olmadığı ayrık BT ve OT ortamlarında korur.\n\nKorvia tamamen kurum içinde ve yalıtılmış ağlarda, imzalı çevrim dışı güncellemelerle çalışır. USB portlarını, mühendislik iş istasyonlarını ve dışarı aktarımları denetim altına alır.'),
          kartlar('Korvia\'nın hangi parçaları bunu yapar?', [
              ('Kurulum', 'Sunucu, sınıflandırma ve analiz kapalı ağınızın içinde çalışır.'),
              ('Veri Sınıflandırma', 'Şebeke haritaları, tesis planları ve acil durum prosedürleri hassas olarak etiketlenir.'),
              ('Uç Nokta DLP', 'USB ve dosya aktarımları iş istasyonunda durdurulur.'),
          ]),
          kurulum_notu('Kurum içi ve yalıtılmış ağ; güncellemeler imzalı dosyalar olarak gelir.'),
          mevzuat('cbigr', 'iso'),
      ])

# ---------------- Mevzuat ----------------
sayfa('mevzuat', 'Mevzuata genel bakış', 'mevzuat', 'cozumler', 20,
      'KVKK, BDDK, SPK, Bilgi ve İletişim Güvenliği Rehberi, PCI DSS, ISO 27001.',
      'Mevzuat', 'Her düzenleme aynı iki soruyu sorar.',
      'Veri nerede, ona ne oldu? Korvia programınızın teknik tarafını destekler: düzenlemeye tabi verinin envanteri, nereye gidebileceğine dair denetimler ve kanıt.',
      [
          mevzuat('kvkk', 'bddk', 'spk', 'cbigr', 'pci', 'iso', 'saglik', 'gdpr', baslik='Hangi düzenlemeye ihtiyacınız var?'),
          tablo('Teknik gereksinimden Korvia\'ya', ['Teknik soru', 'Korvia\'daki karşılığı'], [
              ('Kişisel veri nerede duruyor?', 'Veri Keşfi ve DSPM: konuma göre kişisel veri envanteri'),
              ('Veri hangi kanallardan çıkabilir?', 'DLP: uç nokta, e-posta, web, bulut ve yapay zekâda tek politika'),
              ('Bir olayda ne oldu, kim yaptı?', 'İnceleme: imzalı olay kayıtları ve vaka zaman çizelgesi'),
              ('Kayıtlar değiştirilebilir mi?', 'İmzalı kanıt; denetim kaydına erişim de kaydedilir'),
              ('Veri yurt dışına çıkıyor mu?', 'Kurum içi ve özel bulut kurulumda içerik ve kanıt ağınızda kalır'),
          ]),
          notkutu('"Destekler" ne demek?', UYARI),
      ],
      seoBaslik='Mevzuat: KVKK, BDDK, SPK ve Bilgi ve İletişim Güvenliği Rehberi | Korvia')
