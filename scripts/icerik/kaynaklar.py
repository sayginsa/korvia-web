from ortak import *

# ---------------- Kaynaklar ----------------
sayfa('poc-rehberi', 'POC rehberi', 'kaynaklar/poc-rehberi', 'kaynaklar', 1,
      'On iki test senaryosu ve bir puanlama tablosu.',
      'Kaynaklar · POC rehberi', 'Demo izlemeyin. Kendi verinizle test edin.',
      'Bir üreticinin demo verisi, bir DLP platformunun size uygun olup olmadığını söyleyemez. Bu rehber Korvia\'yı ya da herhangi bir veri güvenliği ürününü kendi iş akışlarınızda değerlendirmenize yardım eder.',
      [
          metin('Ortamınızda önemli olanı test edin.',
                'Bir kavram kanıtlama (POC), güvenlik ürününün kurumunuz için önemli iş akışlarında nasıl davrandığını göstermelidir.\n\nKorvia ile kendi belge şablonlarınıza, veritabanı şemalarınıza ve yapay zekâ iş akışlarınıza karşı test edersiniz; tespit doğruluğunu, yanlış alarm oranlarını, uç nokta performansını ve olayların ne kadar açıklanabilir olduğunu ilk elden ölçersiniz.'),
          kartlar('Neleri hazırlamalısınız?', [
              ('Bir veri türü seçin', 'En kritik veya en sık sızan veriyle başlayın.'),
              ('Gerçek iş akışlarını listeleyin', 'Bu veriyi kim, hangi araçla, nereye gönderiyor?'),
              ('İzin ve engel örnekleri yazın', 'Meşru veya riskli diyebileceğiniz beş ile on vaka.'),
              ('İş birimini dahil edin', 'Güvenlik ekibi tek başına gerçekçi sonuç üretemez.'),
              ('Altyapıyı hazırlayın', 'Bir sanal makine (8 vCPU, 16 GB RAM, 250 GB disk), dizin erişimi ve test uç noktaları.'),
              ('Başarı ölçütlerini önce yazın', 'POC\'den sonra yazılan ölçütler sonucu anlamsız kılar.'),
          ]),
          notkutu('Gerçek kişisel veriye ihtiyacınız var mı?', 'Hayır. Sağlama doğrulamasından geçen sentetik T.C. kimlik ve IBAN numaraları, gerçek belge şablonlarınızla birlikte gerçekçi sonuç verir.'),
          tablo('Hangi senaryoları test etmelisiniz?', ['No.', 'Senaryo', 'Kanal', 'Beklenen davranış'], [
              ('1', 'Müşteri listesinin kişisel yapay zekâ hesabına yüklenmesi', 'Yapay zekâ, web', 'Engelle ve kullanıcıya nedenini söyle'),
              ('2', 'Aynı listenin kurumsal yapay zekâ hesabına yüklenmesi', 'Yapay zekâ, web', 'İzin ver ve kaydet'),
              ('3', 'Kaynak kod dosyasının USB belleğe kopyalanması', 'Uç nokta', 'Ekibinizin kararına göre engelle veya uyar'),
              ('4', 'Gizli sözleşmenin kişisel web postasıyla gönderilmesi', 'Web, e-posta', 'Engelle ve olayı kaydet'),
              ('5', 'Erişim anahtarının bir yapay zekâ aracına yapıştırılması', 'Yapay zekâ, pano', 'Engelle'),
              ('6', 'CAD dosyası veya formülün kişisel bulut depolamaya yüklenmesi', 'Bulut, web', 'Engelle ve olayı kaydet'),
              ('7', 'Gizli belgenin etiketsiz bir kopyayla gönderilmesi', 'Uç nokta, web', 'Parmak iziyle yakalanır'),
              ('8', 'Hassas içeriğin bir kısmının kopyala-yapıştırla çıkması', 'Yapay zekâ, web, pano', 'İçerik analiziyle yakalanır'),
              ('9', 'Mali raporun onaylı bir paydaşa gönderilmesi', 'E-posta', 'İzin ver, yanlış engelleme yok'),
              ('10', 'Olağan dışı yoğun dosya etkinliği olan kullanıcı', 'İçeriden risk', 'Görünürlük ve bağlamlı bir olay'),
              ('11', 'T.C. kimlik numarası listesi içeren taranmış belge', 'Uç nokta, keşif', 'OCR ile yakalanır'),
              ('12', 'Açık ağ paylaşımında kişisel veri içeren dosya', 'Keşif', 'Aşırı açık dosya olarak raporlanır'),
          ], aciklama='İzin verilmesi gereken akışları da mutlaka test edin. Projeler kaçırılan olaylardan çok yanlış engellemeler yüzünden başarısız olur.'),
          tablo('Başarıyı nasıl ölçersiniz?', ['Ölçüt', 'Nasıl ölçülür', 'Hedef nasıl yazılır'], [
              ('Tespit doğruluğu', 'Hazırlanan riskli örneklerden yakalananların oranı', 'Riskli örnekler sizin belirlediğiniz oranda yakalanır'),
              ('Yanlış pozitif', 'Meşru akışlarda yanlış engelleme ve uyarılar', 'Kabul edilebilir en fazla yanlış alarm'),
              ('Yanlış negatif', 'Gözden kaçan riskli örnekler', 'Kritik veri türü için kabul edilebilir kaçırma'),
              ('Bağlam farkındalığı', 'Kurumsal ve kişisel hesabın ayırt edilmesi', '1. ve 2. senaryo arasında net fark'),
              ('Açıklanabilirlik', 'Tek ekran kim, ne, nereye, hangi politika ve neden sorularını cevaplar', 'Evet veya hayır'),
              ('Performans', 'Uç nokta işlemci ve bellek kullanımı, kullanıcı geri bildirimi', 'Ajan işlemci sınırının altında kalır, şikâyet yok'),
              ('Politika hızı', 'Kural değişikliğinin uç noktalara ulaşma süresi', 'POC ortamınızda ölçülür'),
          ], aciklama='Hedefleri başlamadan önce üzerinde anlaşarak belirleyin. Hedefleri kurumunuz koyar.'),
          adimlar('Yanlış pozitifleri nasıl değerlendirirsiniz?', [
              ('Her olayı sınıflandırın', 'Doğru tespit, yanlış alarm veya kaçırılan olay.'),
              ('Nedeni bulun', 'Kural çok mu geniş, istisna mı eksik, sinyal mi yanlış?'),
              ('Kusuru ayardan ayırın', 'Ayar, POC sırasında birlikte düzeltilebilmelidir.'),
              ('Yeniden çalıştırın', 'Önemli olan iyileştirme döngüsünün ne kadar iyi işlediğidir.'),
          ]),
          tablo('Her üreticiye ne sormalısınız?', ['Konu', 'Soru'], [
              ('Konum', 'Veri nerede tespit ediliyor: uç noktada, ağda, bulutta?'),
              ('Tanıma', 'Yalnızca sayı kalıpları mı, yoksa doğrulanmış tanımlayıcılar ve yapısal olmayan varlıklar da mı?'),
              ('Yapay zekâ', 'Hangi servisler, hangi hesap ayrımı; içerik seviyesinde mi, yalnızca alan adıyla mı?'),
              ('Ağ dışında', 'Evden veya yoldan çalışanlar için koruma devam ediyor mu?'),
              ('Açıklama', 'Olay kaydı kim, ne, nereye, hangi politika ve neden sorularını cevaplıyor mu?'),
              ('Saklama', 'Kayıtlar ve hassas veri nerede, ne kadar süre tutuluyor ve kim okuyabiliyor?'),
          ]),
          tablo('Nasıl karar verirsiniz?', ['Boyut', 'Ağırlık (100 üzerinden)'], [
              ('Tespit kalitesi, yanlış pozitif ve negatif dengesi', '25'),
              ('Yapay zekâ ve bağlam senaryolarının kapsamı', '20'),
              ('Analist ve operasyon deneyimi', '15'),
              ('Kullanıcı deneyimi ve performans etkisi', '15'),
              ('Mimari şeffaflık ve verinin kaldığı yer', '10'),
              ('Kurulum uyumu', '10'),
              ('Toplam sahip olma maliyeti', '5'),
          ], aciklama='Her satırı paydaşlarınızla 1\'den 5\'e puanlayın. Ağırlıklar bir öneridir.'),
          adimlar('Bir Korvia POC\'si nasıl yürür?', [
              ('Tanımla', 'Hedef veri türlerini, gerçek iş akışlarını ve ölçülebilir başarı ölçütlerini sabitleyin.'),
              ('Yapılandır', 'Cihazı kurun, örnek şemaları veya şablonları dizinleyin, politikaları yapılandırın.'),
              ('Test et', 'Uç nokta, web, e-posta ve yapay zekâda izin, uyarı, maskeleme ve engelleme senaryolarını çalıştırın.'),
              ('Değerlendir', 'Yakalama oranlarını, yanlış pozitifleri, uç nokta kaynak kullanımını ve açıklanabilirliği hedeflerinizle karşılaştırın.'),
          ]),
      ], cta=('POC\'nizi planlayın', '/demo/'))

sayfa('dlp-satin-alma-rehberi', 'DLP satın alma rehberi', 'kaynaklar/dlp-satin-alma-rehberi', 'kaynaklar', 2,
      'DLP almadan önce sorulacak altı soru.',
      'Kaynaklar · DLP satın alma rehberi', 'DLP almadan önce sormanız gereken altı soru.',
      'Bir DLP ürününün demosunu yapmak kolay, işletmek zordur. Bu sorular bir ürünün kurumunuzda, sizin verinizle nasıl davranacağını gösterir.',
      [
          notkutu('DLP projeleri neden tıkanır?', 'Engellemeyle başlarlar ve alarmlar içinde boğulurlar. Bir ürünün izleme modundan öteye geçip geçemeyeceğini doğruluk ve bağlam belirler.'),
          tablo('Ne sormalısınız?', ['Soru', 'Neden önemli', 'İyi bir cevap'], [
              ('Veri nerede tespit ediliyor?', 'Ağ dışında neyin çalışmaya devam edeceğini ve neyin yeniden yönlendirilmesi gerektiğini belirler.', 'Hangi bileşenin nerede çalıştığını gösteren net bir harita.'),
              ('Ürün gerçekte neyi tanıyabiliyor?', 'Yalnızca kalıplar tasarımları, kodu ve sözleşmeleri kaçırır.', 'Doğrulanmış tanımlayıcılar, parmak izleri ve içerik analizi; sizin dosyalarınızda gösterilmiş.'),
              ('Hangi yapay zekâ senaryoları görünür?', 'Alan adına göre denetim kurumsal hesabı kişiselden ayıramaz.', 'Adıyla servisler, kullanılan hesap ve komutun içeriği.'),
              ('Kurum ağı dışında ne oluyor?', 'Hassas işin büyük kısmı ofis dışında yapılır.', 'Bağlantı olmadan da aynı politika ve aynı kanıt.'),
              ('Analist kararı anlayabiliyor mu?', 'Kimsenin açıklayamadığı bir alarm gürültüye dönüşür.', 'Tek ekran: kim, ne, nereye, hangi politika ve neden eşleşti.'),
              ('Kayıtlar ve hassas veri nerede saklanıyor?', 'Bir sızıntının kanıtı sızan veriyi taşıyabilir.', 'Belirtilmiş saklama süresi, konum, erişim hakları ve içeriğin kopyalanıp kopyalanmadığı.'),
          ]),
          tablo('Hangi kanalları test etmelisiniz?', ['Kanal', 'Çalıştırmaya değer tek test'], [
              ('Uç nokta', 'Etiketli bir dosyayı USB\'ye kopyalayın, sonra yazdırın.'),
              ('E-posta', 'Gizli bir dosyayı kişisel bir adrese gönderin.'),
              ('Web', 'Aynı dosyayı kişisel web postasıyla yükleyin.'),
              ('Bulut uygulamaları', 'Onaysız bir depolama servisinden paylaşın.'),
              ('Yapay zekâ araçları', 'Bir kısmını kişisel bir yapay zekâ hesabına yapıştırın.'),
              ('Ağ dışında', 'Testleri dizüstü bilgisayarın bağlantısı kesikken tekrarlayın.'),
          ]),
          ilgili('poc-rehberi', 'dlp', 'sozluk', baslik='Sırada ne var?'),
      ], cta=('Bir POC planlayın', '/kaynaklar/poc-rehberi/'))

sayfa('sozluk', 'Sözlük', 'kaynaklar/sozluk', 'kaynaklar', 3,
      'Veri ve yapay zekâ güvenliği terimleri, sade bir dille.',
      'Kaynaklar · Sözlük', 'Veri güvenliği, sade bir dille.',
      'Veriyi korurken ve yapay zekâ kullanırken karşınıza çıkan terimlerin kısa ve doğrudan tanımları. Her biri Korvia\'da nereye karşılık geldiğini gösterir.',
      [])

sayfa('sss', 'Sık sorulan sorular', 'sss', 'kaynaklar', 4,
      'Tespit, kurulum, saklama ve değerlendirme hakkında cevaplar.',
      'Kaynaklar · SSS', 'Sık sorulan sorular',
      'Korvia\'nın neyi tespit ettiği, nasıl kurulduğu, neyi sakladığı ve nasıl değerlendirileceği hakkında doğrudan cevaplar.',
      [])

sayfa('blog', 'Blog', 'blog', 'kaynaklar', 5,
      'Veri, yapay zekâ ve denetim üzerine pratik yazılar.',
      'Blog', 'Veri ve yapay zekâ güvenliği üzerine notlar.',
      'Veri, yapay zekâ ve denetimler üzerine pratik yazılar.',
      [], cta=None)

sayfa('destek', 'Destek', 'destek', 'kaynaklar', 6,
      'Teknik destek kanalları, önem dereceleri ve talep süreci.',
      'Kaynaklar · Destek', 'Size nasıl yardımcı olabiliriz?',
      'Korvia müşterileri ve POC sürecindeki kurumlar için teknik destek. Destek Türkçedir; çalışma saatleri ve yanıt hedefleri destek sözleşmenizde belirlenir.',
      [
          tablo('Bize nasıl ulaşırsınız?', ['Kanal', 'Adres', 'Kapsam'], [
              ('E-posta', '{destekEposta}', 'Tüm destek talepleri'),
              ('İş ortağınız', 'İş ortağınız üzerinden', 'Yönetilen hizmet ve MSSP müşterileri için birinci seviye destek'),
          ]),
          tablo('Talepler nasıl önceliklendirilir?', ['Seviye', 'Tanım', 'Örnek'], [
              ('Önem 1, kritik', 'Üretim durdu veya veri koruması çalışmıyor; geçici çözüm yok', 'Yönetim cihazına erişilemiyor veya uç nokta ajanları toplu olarak bağlantısız'),
              ('Önem 2, yüksek', 'Ana bir işlev bozuk, üretim devam ediyor', 'Bir kanal olay üretmiyor veya konsola erişilemiyor'),
              ('Önem 3, orta', 'Sınırlı etki, geçici çözüm var', 'Tek bir uç nokta etkilenmiş, raporlama hatası veya politika ayarı'),
              ('Önem 4, düşük', 'Soru, görsel bir sorun veya özellik talebi', 'Dokümantasyon sorusu veya arayüz önerisi'),
          ], aciklama='Yanıt hedefleri destek sözleşmenize bağlıdır; sözleşmedeki tablo geçerlidir.'),
          kartlar('Destek neleri kapsar?', [
              ('Ürün hataları', 'Teşhis ve çözüm.'),
              ('Kurulum ve yükseltme', 'Kurulum, yükseltme ve yapılandırma yardımı.'),
              ('Politika rehberliği', 'Politika ve kural tasarımı üzerine öneri.'),
              ('Tespit sonuçları', 'Yanlış pozitif ve yanlış negatiflerin değerlendirilmesi.'),
              ('Güvenlik güncellemeleri', 'Güvenlik güncellemeleri ve yamalar.'),
          ]),
          kartlar('Ayrı hizmet olanlar', [
              ('Politika setinizin işletilmesi', 'Uçtan uca tasarım ve işletim; yönetilen hizmet ve MSSP modellerine dahildir.'),
              ('Üçüncü taraf sistemler', 'Korvia olmayan sistemlerin yönetimi.'),
              ('Özel entegrasyonlar', 'Ortamınıza özel geliştirme işleri.'),
          ]),
          adimlar('Bir talep nasıl ilerler?', [
              ('Açın', 'Ortamınızı, etkilenen modülü, hata mesajlarını ve etkiyi gönderin.'),
              ('Önceliklendirme', 'Talep önem derecesine göre sınıflandırılır ve bir mühendise atanır.'),
              ('Yükseltme', 'İlerleme durursa kıdemli mühendise, ardından destek yönetimine taşınır.'),
              ('Kritik olaylar', 'Önem 1 taleplerde çözülene kadar düzenli durum güncellemesi verilir.'),
          ]),
          notkutu('Talepte neler olmalı?', 'Ürün sürümü, kurulum modeli, etkilenen modül, sorunun başladığı zaman, hata mesajları ve etkilenen kullanıcı sayısı.'),
          notkutu('Neleri eklememelisiniz?', 'Gerçek kişisel veri veya müşteri dosyası eklemeyin. Örnek gerekiyorsa destek ekibi sizinle güvenli bir aktarım yöntemi belirler.'),
          notkutu('Güncellemeler nasıl yapılır?', 'İmzalı yükseltme paketleri belirlediğiniz bakım penceresinde kurulur. Yalıtılmış ağlar dosyadan güncellenir.'),
      ], cta=('Destek talebi açın', '/iletisim/'))

# ---------------- Kurumsal ----------------
sayfa('hakkimizda', 'Hakkımızda', 'hakkimizda', 'kurumsal', 1,
      'Korvia neden var, nasıl düşünür.',
      'Hakkımızda', 'Verinizi, çalışanlarınızı ve itibarınızı koruyun.',
      'İyi çalışanlar da hata yapar: yanlış sohbete yapıştırılan bir liste, yanlış adrese giden bir dosya. Korvia bu anları pahalı bir olaya dönüşmeden yakalamak için var.',
      [
          notkutu('Hassas veri artık yalnızca e-postadan çıkmıyor.', 'Müşteri listeleri yapay zekâ sohbetlerine, kod kişisel bulutlara, dosyalar USB belleklere gidiyor.'),
          kartlar('Nasıl düşünüyoruz?', [
              ('Her veri eşit değildir', 'Aynı dosya, onu kimin nereye taşıdığına göre farklı risk taşır.'),
              ('Etiketler karara dönüşmeli', '"Gizli" damgası, bir politika ona göre davranmadıkça hiçbir şeyi korumaz.'),
              ('Alarm değil, bağlam', 'Analist ne olduğunu, kimin yaptığını, hangi verinin nereye gittiğini ve nedenini görür.'),
              ('Kendi verimiz konusunda açığız', 'Neyi incelediğimizi, neyi sakladığımızı ve nerede tuttuğumuzu söyleriz.'),
          ]),
          metin('Kim geliştiriyor?',
                'Korvia, yirmi yılı aşkın süredir kurumlarda veri güvenliği projeleri yürüten bir ekip tarafından Türkiye pazarı için hazırlandı. Hantal ajanlardan, yapay zekâ etrafındaki kör noktalardan ve bağlamı olmayan alarmlardan yorulan güvenlik ekipleri için tek hafif ajan, varsayılan olarak kurum içi veri egemenliği ve sınıflandırma etiketlerini gerçekten uygulayan politikalar sunar.\n\nTürkiye\'de satış, kurulum ve destek iş ortağı kanalıyla verilir.'),
          tablo('Şirket bilgileri', ['', ''], [
              ('Marka', 'Korvia'),
              ('Tüzel kişilik', '{sirketAdi}'),
              ('Odak', 'Veri keşfi (DSPM), veri sınıflandırma, uç nokta/ağ/bulut DLP ve yapay zekâ güvenliği'),
              ('Kurulum', 'Kurum içi, özel bulut, yalıtılmış ağ ve yönetilen hizmet'),
              ('Adres', '{adres}'),
              ('İletişim', '{satisEposta}'),
          ]),
      ])

sayfa('guven-merkezi', 'Güven merkezi', 'guven-merkezi', 'kurumsal', 2,
      'Neyi incelediğimiz, sakladığımız ve nerede tuttuğumuz.',
      'Güven merkezi', 'Güvenlikte şeffaflık önemlidir.',
      'Güvenlik ekipleri bir güvenlik aracının neyi incelediğini, neyi sakladığını veya ağ üzerinden neyi gönderdiğini tahmin etmek zorunda kalmamalı. Korvia Güven Merkezi bileşenlerin nerede çalıştığını, olay kayıtlarının neyi tuttuğunu, kayıtların ne kadar saklandığını ve verinizin nasıl sizin denetiminizde kaldığını belgeler.',
      [
          kartlar('Altı soru, altı cevap', [
              ('Korvia neyi inceler?', 'Politikalarınızın kapsadığı kanallardaki dosyaları, mesajları, yüklemeleri ve yapay zekâ komutlarını. İçerik hareket ettiği yerde kontrol edilir ve karar orada verilir. Açmadığınız kanallar incelenmez.'),
              ('Neyi saklar?', 'Olayları: neyin tespit edildiğini, hangi kuralın neden eşleştiğini, kullanıcıyı, hedefi ve uygulanan eylemi. İçerik yalnızca bir politika onu kanıt olarak istediğinde saklanır. Olaylar imzalıdır; sonradan yapılan her değişiklik görünür.'),
              ('Nerede saklanır?', 'Kurum içi sürümler her şeyi ağınızın içinde tutar; siz göndermeyi seçmedikçe hiçbir şey çıkmaz. Yönetilen sürümlerde veri, kurulumdan önce sizinle kararlaştırılan bölgedeki barındırılan depoda tutulur.'),
              ('Kim erişebilir?', 'Konsol rolü verdiğiniz kişiler. Erişim rol tabanlıdır; denetçiler ham içeriği görmeden raporları görebilir. Her yönetici eylemi konsolun kendi denetim kaydına yazılır.'),
              ('Hangi bileşenler ağınızda çalışır?', 'Kurum içi sürümde hepsi: uç nokta ajanları, konsoluyla birlikte politika sunucusu ve kanıt deposu. Yönetilen sürümlerde uç nokta ajanları sizde çalışır, politika sunucusu sizin için barındırılır.'),
              ('Veri ne kadar saklanır?', 'Olaylar, keşif tarama geçmişi ve günlük özetler varsayılan olarak 400 gün, denetim kaydı 24 ay saklanır. Kurumunuz bu süreleri kısaltabilir. Gerekçesi değerlendirme sırasında paylaştığımız saklama belgesindedir.'),
          ]),
          form('belge', 'Güvenlik belgesi talep edin', 'İncelemeniz için hangi belgelere ihtiyacınız olduğunu yazın. Sürümünüze ve kurulumunuza uygun olanları göndeririz.',
               mesajEtiketi='Hangi belgelere, neden ihtiyacınız var?', gonderEtiketi='Belge talep edin'),
      ])

sayfa('is-ortaklari', 'İş ortakları', 'is-ortaklari', 'kurumsal', 3,
      'Bayi, entegratör ve MSSP iş ortaklığı.',
      'İş ortakları', 'Veri ve yapay zekâ güvenliğini müşterilerinize taşıyın.',
      'Korvia; bayiler, sistem entegratörleri, çözüm ortakları ve yönetilen güvenlik hizmeti sağlayıcılarıyla çalışır. DSPM, uç nokta DLP ve yapay zekâ güvenliğini kurum içinde veya çok kiracılı yönetilen hizmet olarak sunun; fırsat koruması ve doğrudan mühendislik desteğiyle.',
      [
          metin('Müşteri ihtiyacına göre kurulmuş bir güvenlik portföyü.',
                'Müşteriler geleneksel bir DLP ihtiyacıyla, bir veri görünürlüğü sorunuyla veya çalışanların yapay zekâ araçlarıyla hassas bilgi paylaşma endişesiyle başlayabilir.\n\nMüşteri ister gölge yapay zekâ keşfiyle, ister mevzuat kaynaklı sınıflandırmayla, ister tam uç nokta DLP değişimiyle başlasın; tek modülle girip aynı ajan üzerinde genişleyebilirsiniz.'),
          tablo('İş ortaklığının üç yolu', ['', 'Bayi / entegratör', 'MSSP / yönetilen hizmet', 'Bölge iş ortağı'], [
              ('Siz satarsınız', 'Korvia lisansları ve kendi kurulum ve desteğiniz', 'Aylık veri koruma hizmeti', 'Bölgenizdeki bayi ağınız üzerinden Korvia'),
              ('Biz sağlarız', 'Lisans, teknik eğitim, POC desteği, fırsat kaydı', 'Çok kiracılı konsol, müşteri bazında politika ve raporlar', 'Lisans, teknik eğitim, satış ve pazarlama kitleri, POC desteği'),
              ('Müşterinin kurulumu', 'Müşterinin tercihine göre kurum içi, özel bulut veya yönetilen', 'Sizde veya bizde barındırılır; uç nokta ajanları müşteride', 'Müşterinin tercihine göre kurum içi, özel bulut veya yönetilen'),
              ('Ticari model', 'Abonelik veya süresiz lisans üzerinden marj', 'Her iş ortağıyla ayrıca kararlaştırılır', 'Abonelik veya süresiz lisans üzerinden marj'),
          ]),
          kartlar('MSSP sürümü size neler verir?', [
              ('Kesin kiracı ayrımı', 'Tek konsol; her müşteri yalnızca kendi verisini görür.'),
              ('Politika şablonları', 'Bir kez kurun, her müşteriye dağıtın, müşteri bazında değiştirin.'),
              ('Panolar ve raporlar', 'Müşteri ve portföy bazında, zamanlanmış olarak.'),
              ('Hızlı devreye alma', 'Kiracıyı oluşturun, ajanı dağıtın, şablonu uygulayın. Genellikle bir öğleden sonra.'),
          ]),
          notkutu('Yapmadıklarımız', 'Kayıtlı müşterilerinize satış yapmayız ve bölgenizde rakip bir yönetilen hizmet işletmeyiz.'),
          kartlar('Yetkinlik desteği', [
              ('Teknik eğitim', 'İki gün; çevrim içi veya yerinde.'),
              ('Satış desteği', 'Konumlandırma, demo ortamı, itiraz karşılama ve POC el kitabı.'),
              ('Pazarlama kitleri', 'Ortak markalı ürün föyleri ve kampanya kitleri.'),
              ('İsimli iş ortağı yöneticisi', 'Ve mühendislerimize doğrudan bir kanal.'),
          ]),
          form('is-ortakligi', 'Korvia iş ortağı olun', 'Nerede çalıştığınızı ve nasıl sattığınızı anlatın. İlk kavram kanıtlamanızı uçtan uca birlikte yürütürüz.',
               'Nasıl iş ortaklığı yapmak istiyorsunuz?',
               ['Bayi / entegratör: müşterilere satış ve kurulum', 'MSSP / yönetilen hizmet: kendi hizmetiniz olarak işletme', 'Bölge iş ortağı: bir bölgeyi kapsama', 'Henüz emin değilim: birlikte seçelim'],
               'İşinizi kısaca anlatın (isteğe bağlı)', 'Başvurun'),
      ], cta=('Başvurun', '#form'))

sayfa('iletisim', 'İletişim', 'iletisim', 'kurumsal', 4,
      'Satış, iş ortaklığı ve destek.',
      'İletişim', 'Ürünü geliştirenlerle konuşun.',
      'Platform, iş ortaklığı veya mevcut bir kurulum hakkında sorularınız mı var? Doğru adrese yazın ya da formu kullanın.',
      [
          form('iletisim', 'Bize yazın', '', 'Konu', ['Satış', 'İş ortaklığı', 'Destek', 'Basın', 'Diğer'], 'Mesajınız', 'Mesajı gönderin'),
      ], cta=None)

sayfa('demo', 'Demo planlayın', 'demo', 'kurumsal', 5,
      'Otuz dakika; önce sizin sorularınız.',
      'Demo', 'Otuz dakika. Önce sizin sorularınız.',
      'Neyi korumak istediğinizi ve nerede durduğunu anlatın. Platformun sizin için önemli kısımlarını gösteririz; başka bir çözüm daha uygunsa bunu da söyleriz.',
      [
          form('demo', 'Demo talebi', '', 'Ne görmek istersiniz?',
               ['Veri sınıflandırma', 'DLP', 'Yapay zekâ güvenlik duvarı', 'Yapay zekâ veri güvenliği', 'Kod asistanları', 'Henüz emin değilim'],
               'Neyi korumak istiyorsunuz? (isteğe bağlı)', 'Demo talep edin'),
      ], cta=None)

# ---------------- Yasal ----------------
sayfa('kvkk-aydinlatma', 'KVKK aydınlatma metni', 'kvkk-aydinlatma', 'yasal', 1,
      'Kişisel verilerin işlenmesine ilişkin aydınlatma metni.',
      'Yasal', 'Kişisel verilerin işlenmesine ilişkin aydınlatma metni',
      'Bu metin taslaktır ve yayına alınmadan önce hukuk danışmanınız tarafından gözden geçirilmelidir.',
      [
          metin('Veri sorumlusu', '6698 sayılı Kişisel Verilerin Korunması Kanunu ("KVKK") kapsamında veri sorumlusu {sirketAdi}\'dır (adres: {adres}).'),
          metin('Hangi verileri işliyoruz?', 'Bu sitedeki formlar aracılığıyla ilettiğiniz ad soyad, iş e-postası, şirket, ülke ve mesaj içeriği. Site, çerez veya benzeri izleme teknolojisiyle davranışsal veri toplamaz.'),
          metin('Hangi amaçla işliyoruz?', 'Demo, iletişim, iş ortaklığı ve belge taleplerinizi cevaplamak; talebinizle ilgili teklif ve bilgi sunmak.'),
          metin('Hukuki sebep', 'Kişisel verileriniz, KVKK md. 5/2-c (bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması) ve md. 5/2-f (veri sorumlusunun meşru menfaati) hukuki sebeplerine dayanılarak işlenir.'),
          metin('Kimlere aktarıyoruz?', 'Talebinizin karşılanması için gerekli olduğu ölçüde, yetkili iş ortaklarımıza ve hizmet aldığımız altyapı sağlayıcılarına aktarılabilir. Yurt dışına aktarım yapılması hâlinde KVKK md. 9 hükümlerine uyulur.'),
          metin('Haklarınız', 'KVKK md. 11 kapsamındaki haklarınızı kullanmak için {satisEposta} adresine yazabilirsiniz.'),
      ], cta=None, seoBaslik='KVKK Aydınlatma Metni | Korvia')

sayfa('cerezler', 'Çerez politikası', 'cerezler', 'yasal', 2,
      'Bu sitenin kullandığı çerezler.',
      'Yasal', 'Çerez politikası',
      'Bu site reklam, analiz veya izleme amacıyla çerez kullanmaz.',
      [
          metin('Kullandığımız çerezler', 'Site yalnızca çalışması için zorunlu olan teknik depolamayı kullanabilir. Yazı tipleri sitenin kendi sunucusundan yüklenir; üçüncü taraf yazı tipi veya analiz servisine istek gönderilmez.'),
          metin('Yönetim paneli', 'İçerik yönetim paneli (/keystatic) yalnızca yetkili editörler içindir ve oturum için zorunlu çerezler kullanır.'),
          metin('Değişiklikler', 'Bir analiz aracı eklenirse bu sayfa güncellenir ve gerekli durumlarda açık rızanız alınır.'),
      ], cta=None, seoBaslik='Çerez Politikası | Korvia')
