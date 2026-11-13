from ortak import *

sayfa('yapay-zeka-guvenligi', 'Yapay zekâ güvenliğine genel bakış', 'yapay-zeka-guvenligi', 'yapay-zeka', 1,
      'Gölge yapay zekâyı görün, komutlardaki hassas veriyi koruyun.',
      'Yapay zekâ güvenliği · Daha çok yapay zekâ, daha az risk', 'Yapay zekâ kullanımını kurumunuz için daha güvenli hâle getirin.',
      'Yapay zekâ araçları artık gündelik işin parçası. Ancak çalışanların bu araçlara yapıştırdığı veya yüklediği veri hemen bir risk yaratıyor. Korvia gölge yapay zekâyı görünür kılar ve tarayıcıda, masaüstünde ve kurumsal yapay zekâ iş akışlarında veri koruma politikalarını uygular.',
      [
          ilgili('yapay-zeka-guvenlik-duvari', 'yapay-zeka-veri-guvenligi', 'kod-asistanlari', baslik='Farklı riskler, farklı denetimler'),
          kartlar('Ekipleriniz için ne değişir?', [
              ('Kullanılan araçları görün', 'Hangi yapay zekâ servislerinin, kim tarafından, hangi veriyle kullanıldığı.'),
              ('Engellemek yerine maskeleyin', 'Hassas kısım bir etiketle değiştirilir; komutun geri kalanı gider.'),
              ('Kararı açıklayın', 'Çalışan neyin bulunduğunu ve nedenini o anda görür.'),
          ]),
          metin('Veri riskini görmezden gelmeden yapay zekâyı benimseyin.',
                'Bir pazarlama çalışanı müşteri bilgisini bir yazım asistanıyla paylaşabilir. Bir yazılımcı kaynak kodu bir kod asistanına verebilir. Bir analist gizli bir belgeyi özetletmek için yükleyebilir.\n\nBu durumların iş amacı farklıdır ama temel soru aynıdır: bu bilgi bu şekilde paylaşılmalı mı?\n\nKorvia güvenlik ekiplerinin kurumsal hesabı kişisel hesaptan ayırmasını, komutlardaki hassas değerleri maskelemesini ve izinsiz kod veya dosya yüklemelerini, yapay zekâ kullanımını durdurmadan engellemesini sağlar.'),
          sss('Yapay zekâ güvenliği hakkında sorular', [
              ('Yapay zekâ veri güvenliği geleneksel DLP\'den nasıl farklı?', 'Geleneksel DLP e-posta, USB ve web yüklemeleriyle hareket eden dosyaları denetler. Yapay zekâ veri güvenliği bu korumayı sohbet komutlarına, yapay zekâ dosya yüklemelerine, kod asistanlarına ve model yanıtlarına taşır; aracın tamamını engellemek yerine hassas değerleri satır içinde maskelemenizi sağlar.'),
          ]),
      ],
      seoBaslik='Yapay Zekâ Güvenliği | Korvia')

sayfa('yapay-zeka-guvenlik-duvari', 'Yapay Zekâ Güvenlik Duvarı', 'yapay-zeka-guvenligi/yapay-zeka-guvenlik-duvari', 'yapay-zeka', 2,
      'Giden komutları ve dönen yanıtları tek politikayla inceleyin.',
      'Yapay zekâ güvenliği · Yapay zekâ güvenlik duvarı', 'Yapay zekâya ne girdiğini ve ne döndüğünü denetleyin.',
      'Yapay zekâ etkileşimleri iki yönde risk taşır. Korvia Yapay Zekâ Güvenlik Duvarı giden komutları ve dönen model yanıtlarını gerçek zamanlı inceler: hassas veriyi maskeler, gizli anahtarları yakalar ve yapay zekâ iş akışlarınızda güvenlik politikalarını uygular.',
      [
          senaryo('Bir destek talebi dil modeline gidiyor.', 'Müşterinin IBAN\'ını içeren talep metni', 'Destek sistemindeki temsilci',
                  'Yapay zekâ ağ geçidi üzerinden dil modeli', 'Finansal veri koruması: göndermeden önce maskele', 'maskele',
                  'IBAN gönderilmeden maskelendi; yanıtta yetkili kullanıcı için asıl değer geri yüklendi'),
          metin('Bir komut bir sorudan fazlasını taşıdığında.',
                'Bir çalışan bir müşteri kaydını, finansal bir rakamı veya kaynak kodu bir komuta yapıştırdığında Korvia hassas içeriği tarayıcıdan, uç noktadan veya ağ geçidinden çıkmadan önce tespit eder.\n\nPolitikanıza göre Korvia kullanıcıyı uyarır, komutun güvenle devam edebilmesi için hassas değerleri satır içinde maskeler ya da isteği tamamen engeller.'),
          adimlar('Nerede çalışır?', [
              ('Tarayıcı eklentisi', 'ChatGPT, Claude ve Gemini gibi tarayıcı tabanlı yapay zekâ servislerinde komutları, dosya yüklemelerini ve yanıtları inceler.'),
              ('Uç nokta ajanı', 'Masaüstü yapay zekâ uygulamalarını, yerel kod asistanlarını ve pano yapıştırmalarını izler ve denetler.'),
              ('Yapay zekâ ağ geçidi', 'Salesforce, Teams veya destek sistemleri gibi iş uygulamalarından OpenAI, Gemini veya Mistral gibi modellere giden istekleri ve yanıtları inceler.'),
          ]),
          kartlar('Giderken: komutlar ve dosyalar', [
              ('Kişisel veri maskeleme', 'Ad, kimlik ve hesap numaraları etiketlerle değiştirilir; komut yine gider.'),
              ('Gizli anahtarlar ve token\'lar', 'API anahtarları, parolalar ve token\'lar modele ulaşmadan yakalanır.'),
              ('Kaynak kod', 'Komuta yapıştırılan kod tanınır ve politikaya göre ele alınır.'),
              ('Komut enjeksiyonu ve jailbreak', 'Komut enjeksiyonu ve jailbreak kalıplarını modele ulaşmadan tespit edin.'),
          ], eyebrow='→ Giden'),
          kartlar('Dönerken: yanıtlar', [
              ('Maskelenen değerlerin geri yüklenmesi', 'Kullanıcı yanıtta gerçek değerleri yeniden görür. Model ise hiç görmedi.'),
              ('Yanıtlardaki hassas veri', 'Korunan veri taşıyan yanıtlar dönüşte yakalanır.'),
              ('Hassas içerik ve politika kısıtları', 'Modellerin kısıtlı kurum içi veriyi veya politikaya aykırı çıktıyı kullanıcıya döndürmesini önleyin.'),
          ], eyebrow='← Dönen'),
          sss('Yapay Zekâ Güvenlik Duvarı hakkında sorular', [
              ('Çalışanlar yapay zekâ araçlarını kullanmayı bırakmak zorunda mı?', 'Hayır. Toptan yasak yerine yanıtları veri hassasiyetine ve kullanıcı bağlamına göre ayarlayabilirsiniz. Çalışanlar satır içi maskeleme veya gerekçe isteminden sonra güvenle çalışmaya devam eder; yüksek riskli sızıntılar engellenir.'),
              ('Hangi yapay zekâ servislerini kapsar?', 'Tarayıcı eklentisiyle tarayıcı tabanlı dil modellerini (ChatGPT, Claude, Gemini, Perplexity ve DeepSeek dahil), uç nokta ajanıyla masaüstü yapay zekâ uygulamalarını ve kod asistanlarını (Copilot, Cursor, Claude Code, Codex), yapay zekâ ağ geçidiyle kurumsal API trafiğini (OpenAI, Anthropic, Mistral, Gemini). Servis bazındaki tam denetim tablosunu POC öncesinde paylaşırız.'),
              ('Yapay zekâ güvenlik duvarı neyi inceler?', 'Giden komutları (dosya ekleri dahil) ve dönen model yanıtlarını kişisel veri, finansal veri, API anahtarı, kimlik bilgisi, kaynak kod ve komut enjeksiyonu kalıpları açısından inceler.'),
          ]),
          ilgili('yapay-zeka-veri-guvenligi', 'kod-asistanlari', 'tespit-motoru', 'golge-yapay-zeka'),
      ])

sayfa('yapay-zeka-veri-guvenligi', 'Yapay Zekâ Veri Güvenliği', 'yapay-zeka-guvenligi/yapay-zeka-veri-guvenligi', 'yapay-zeka', 3,
      'Gölge yapay zekâ, maskeleme, tarayıcı ve masaüstü uygulamaları.',
      'Yapay zekâ güvenliği · Yapay zekâ veri güvenliği', 'Çalışanların yapay zekâyla veriyi nasıl paylaştığını anlayın.',
      'Çalışanlar yapay zekâyı her gün yazmak, analiz etmek ve kod geliştirmek için kullanıyor. Korvia Yapay Zekâ Veri Güvenliği kullanılan her yapay zekâ aracını keşfeder, kurumsal kiracıyı kişisel hesaptan ayırır ve komutlardaki ve dosya yüklemelerindeki hassas veriyi maskeler veya engeller.',
      [
          maskeleme('Örnek: maskeleme',
                    'Ayşe Yılmaz için bir ödeme hatırlatması yaz. T.C. Kimlik No 10000000146, IBAN TR33 0006 1005 1978 6457 8413 26.',
                    '[AD SOYAD] için bir ödeme hatırlatması yaz. T.C. Kimlik No [TCKN], IBAN [IBAN].',
                    'Temsilî örnektir.'),
          senaryo('Müşteri listesi kişisel bir sohbet botuna gidiyor.', 'Ad ve telefon numaraları içeren müşteri listesi',
                  'Satış müdürü', 'Sohbet botu · kişisel hesap', 'Müşteri verisi / yapay zekâ paylaşımı', 'engelle', 'gönderilmedi, nedeni gösterildi'),
          metin('Denetimden önce görünürlük gelir.',
                'Kurumlar etkili güvenlik politikaları koymadan önce çalışanların hangi yapay zekâ araçlarını kullandığını ve hassas bilginin nerede paylaşılabileceğini anlamalıdır.\n\nKorvia Yapay Zekâ Veri Güvenliği yapay zekâ kullanımının görünürlüğüne, hassas verinin açığa çıkmasına ve yönetişime odaklanır. Yapay Zekâ Güvenlik Duvarı ise komutlar ve yanıtlar için satır içi inceleme ve uygulama sağlar. İkisi birlikte, güvenlik ekiplerinin riskli yapay zekâ etkinliğini anlamasına ve doğru denetimi uygulamasına yardım eder.'),
          adimlar('Nasıl çalışır?', [
              ('Yapay zekâ araçlarını bul', 'Kullanılan yapay zekâ servisleri; kullanıcı ve cihaz bazında, kurumsal veya kişisel hesapla.'),
              ('İçeriği incele', 'Yazılan komutlar, yapıştırılan metin ve eklenen dosyalar çıkmadan önce Tespit Motoru\'ndan geçer.'),
              ('Maskele veya durdur', 'Hassas değerler etikete dönüşür ya da politika öyle diyorsa komut durur.'),
              ('Kullanıcıya söyle', 'Kullanıcı "Bu içerik gönderilmedi" mesajını ve nedenini görür.'),
          ]),
          kartlar('Yapay zekâ modülü ne yapar?', [
              ('Gölge yapay zekâ envanteri', 'Hangi yapay zekâ araçlarının, kim tarafından, ne sıklıkla ve hangi hesapla kullanıldığı.'),
              ('Komut incelemesi', 'Yazılan ve yapıştırılan metin gönderilmeden sınıflandırılır.'),
              ('Yükleme denetimi', 'Komuta eklenen dosyalar diğer tüm yüklemeler gibi incelenir.'),
              ('Maskeleme', 'Ad, kimlik ve hesap numaraları etikete dönüşür; geri kalanı gider.'),
              ('Hesaba duyarlı politika', 'Kurumun yapay zekâ kiracısı ve kişisel hesaplar için farklı kurallar.'),
              ('Tarayıcı ve masaüstü', 'Tarayıcı eklentisi web tabanlı yapay zekâyı, uç nokta ajanı masaüstü uygulamalarını kapsar.'),
          ]),
          sss('Yapay Zekâ Veri Güvenliği hakkında sorular', [
              ('Yapay zekâ araçlarını engellemek zorunda mıyız?', 'Hayır. Yapay zekâyı tamamen engellemek çalışanları yönetilmeyen kişisel cihazlara iter. Korvia komutlardaki kişisel veriyi, finansal veriyi ve gizli anahtarları otomatik maskeleyerek yapay zekâyla verimli çalışmaya izin verir; engellemeyi kritik fikri mülkiyete veya onaysız kişisel hesaplara ayırırsınız.'),
              ('Hangi yapay zekâ araçlarını görür?', 'Tarayıcı tabanlı dil modellerini (ChatGPT, Claude, Gemini, Perplexity ve DeepSeek gibi), masaüstü yapay zekâ uygulamalarını ve kod asistanlarını (Copilot, Cursor, Claude Code, Codex) tespit eder; Teams ve Slack gibi iş birliği araçlarındaki yapay zekâ dosya yüklemelerini de inceler.'),
              ('Nereden başlamalıyız?', 'Gölge yapay zekâ keşfini izleme modunda açarak başlayın. Birkaç gün içinde hangi yapay zekâ servislerinin hangi birimlerde kullanıldığını ve hangi hassas verinin paylaşıldığını gösteren somut bir envanter elde edersiniz. Bu, uygulanabilir maskeleme ve engelleme kuralları koymak için gereken kanıttır.'),
          ]),
          ilgili('yapay-zeka-guvenlik-duvari', 'golge-yapay-zeka', 'bulut-dlp', 'kod-asistanlari'),
      ])

sayfa('kod-asistanlari', 'Kod asistanları', 'yapay-zeka-guvenligi/kod-asistanlari', 'yapay-zeka', 4,
      'Claude Code, Codex, Copilot ve Cursor.',
      'Yapay zekâ güvenliği · Kod asistanları', 'Yapay zekâ destekli geliştirmede hassas kodu koruyun.',
      'Yapay zekâ kod asistanları yazılım geliştirmeyi hızlandırır; ancak geliştirici iş akışları kaynak kod, yapılandırma dosyaları, kimlik bilgileri ve kurum içi teknik belgeler de içerebilir. Korvia Claude Code, Codex, GitHub Copilot ve Cursor genelinde özel depolarınızı, API anahtarlarınızı ve müşteri verinizi, geliştiricileri yavaşlatmadan korur.',
      [
          tablo('Depo sınıfları', ['Depo', 'Sınıf', 'Asistan erişimi', 'Karar'], [
              ('ana-bankacilik/', 'Kırmızı · kritik', 'Asistan okuyamaz', 'Engelle · hiçbir şey çıkmaz'),
              ('odeme-api/', 'Sarı · kurum içi', 'Ağ geçidi üzerinden okunabilir', 'Kaydet · gizli anahtarlar maskelenir'),
              ('dokuman-araclari/', 'Yeşil · açık', 'Okunabilir', 'İzle · kaydedilir'),
          ]),
          senaryo('Bir API anahtarı modele gidiyor.', 'Canlı API anahtarı içeren bir fonksiyon', 'Claude Code kullanan geliştirici',
                  'Anthropic API', 'Kırmızı depo: hiçbir kod çıkmaz', 'engelle', 'nedeni terminalde gösterildi'),
          metin('Bir kod aracı hassas bağlam aldığında.',
                'Bir geliştirici bir uygulamadaki sorunu çözmek için yapay zekâ asistanından yardım ister. İstek kaynak kod, yapılandırma değerleri veya dışarıyla paylaşılmaması gereken kurum içi teknik ayrıntılar taşıyabilir.\n\nKorvia herhangi bir komut veya dosya bağlamı geliştiricinin makinesinden çıkmadan önce depo seviyesinde erişim kurallarını ve satır içi gizli anahtar maskelemesini uygular.'),
          kartlar('Kapsanan araçlar', [
              ('Komut satırı ajanları', 'Claude Code ve Codex; yönetilen kancalar (hook) üzerinden.'),
              ('API trafiği', 'Anthropic ve OpenAI API çağrıları; yapay zekâ ağ geçidi üzerinden.'),
              ('Editör asistanları', 'GitHub Copilot ve Cursor; aynı kurallarla.'),
          ]),
          adimlar('Nerede kontrol eder?', [
              ('Ajan kancaları', 'Claude Code ve Codex kancaları her komutu ve ajanın okuduğu her dosyayı kontrol eder.'),
              ('Yapay zekâ ağ geçidi', 'Tüm Anthropic ve OpenAI API trafiği denetim kaydıyla birlikte tek geçitten çıkar.'),
              ('Depo sınıfları', 'Kırmızı, Sarı ve Yeşil depoların kendi okuma ve gönderme kuralları vardır.'),
              ('Karar motoru', 'Gizli anahtarlar ve kişisel veri maskelenir. Kritik kod maskelenmez, engellenir.'),
          ]),
          kartlar('Neleri kapsar?', [
              ('Claude Code ve Codex', 'Yönetilen kancalar komutları, dosya okumalarını ve araç çıktısını kontrol eder.'),
              ('Yapay zekâ ağ geçidi', 'Anthropic ve OpenAI API trafiği için tek çıkış ve denetim kaydı.'),
              ('GitHub Copilot ve Cursor', 'Editör içindeki asistanlar için aynı kurallar.'),
              ('Depo sınıfları', 'Kırmızı, Sarı ve Yeşil; her birinin kendi kuralları.'),
              ('Kritik depolarda okuma engeli', 'Asistan Kırmızı bir depoyu hiç okuyamaz.'),
              ('Bağlantı kesilirse kapalı', 'Karar motoruna ulaşılamazsa Kırmızı depolar engelli kalır.'),
          ]),
          sss('Kod asistanları hakkında sorular', [
              ('Kodu engellemek yerine neden maskelemiyorsunuz?', 'Maskeleme anahtarlar, IBAN\'lar ve kurum içi sunucu adları gibi değişmez değerlerde işe yarar; model farkı neredeyse hissetmez. Kodun kendisini yeniden adlandırmak ise modeli kör eder ve yanıt işe yaramaz hâle gelir. Kritik kod için dürüst karar ya izin vermek ya engellemektir.'),
              ('Kimler için?', 'Geliştiricileri Claude Code, Codex, Copilot veya Cursor kullanan ve kendi kaynak kodunun ve müşteri verisinin bu araçlardan çıkmadığını göstermesi gereken bankalar ve düzenlemeye tabi diğer yazılım ekipleri için.'),
              ('Geliştirici ne görür?', 'Terminalde veya editörde neyin bulunduğunu ve hangi depodan veya dosyadan geldiğini söyleyen kısa bir mesaj. İstisna talep edilebilir; ekipler kurallar ayarlanırken yalnızca uyarı modunda başlayabilir.'),
          ]),
          ilgili('yapay-zeka-guvenlik-duvari', 'yapay-zeka-veri-guvenligi', 'fikri-mulkiyet', 'tespit-motoru'),
      ])
