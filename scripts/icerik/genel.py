from ortak import yaz, _l

# ---------------- Site ayarları ----------------
yaz('ayarlar.yaml', {
    'sirketAdi': '[Tüzel kişilik adı]',
    'aciklamaSatiri': 'Veri & Yapay Zekâ Güvenliği',
    'satisEposta': 'satis@[alan adı]',
    'destekEposta': 'destek@[alan adı]',
    'telefon': '+90 [telefon]',
    'adres': '[Adres]',
    'formAdresi': '',
    'footerMetni': 'Korvia, Türkiye pazarı için veri sızıntısı önleme ve yapay zekâ veri güvenliği markasıdır. Hassas veriyi keşfeder, sınıflandırır ve veri hareket ettiği anda doğru politikayı uygular.',
    'demoEtiketi': 'Demo planlayın',
    'kapanisBaslik': 'Kendi verinizle görün.',
    'kapanisMetin': 'Otuz dakikalık bir görüşmede neyi korumak istediğinizi konuşalım. Ardından kendi dosyalarınız ve iş akışlarınızla bir kavram kanıtlama (POC) planlayalım.',
})

# ---------------- Ana sayfa ----------------
yaz('anasayfa.yaml', {
    'seoBaslik': 'Korvia | Veri Sızıntısı Önleme ve Yapay Zekâ Veri Güvenliği',
    'seoAciklama': 'Korvia hassas veriyi keşfeder, sınıflandırır ve e-posta, USB, tarayıcı ve yapay zekâ araçlarında veri hareket ettiği anda politikayı uygular. Kurum içinde çalışır.',
    'eyebrow': 'Veri sızıntısı önleme',
    'baslik': 'Veri kurumda kalır.',
    'ozet': 'İyi çalışanlar da hata yapar. Bunun bedelini veriniz ödememeli. Korvia hassas veriyi gerçek zamanlı tanır; yapay zekâ aracına, tarayıcı yüklemesine, e-postaya veya USB belleğe gitmeden önce maskeler ya da durdurur. Her kanal için tek politika.',
    'birincilCta': _l('Demo planlayın', '/demo/'),
    'ikincilCta': _l('Platformu inceleyin', '/platform/'),
    'olay': {
        'kategori': 'Müşteri verisi / Yapay zekâ paylaşımı',
        'cumle': 'Müşteri listesi bir yapay zekâ aracına yüklenmek istendi.',
        'dosya': 'musteri-listesi-2026.xlsx',
        'icerik': 'T.C. Kimlik No, IBAN',
        'hedef': 'Üretken yapay zekâ servisi · kişisel hesap',
        'karar': 'engelle',
        'kullaniciMesaji': 'Bu içerik gönderilmedi. Dosyada müşteri kimlik ve hesap bilgisi var. Kurumsal yapay zekâ hesabınızı kullanabilirsiniz.',
    },
    'kanalBaslik': 'Kullanıcı ne gönderdi, kurumdan ne çıktı?',
    'kanalAciklama': 'Aynı politika dört farklı kanalda. Hassas değerler maskelenir; işin geri kalanı devam eder.',
    'kanallar': [
        {'ad': 'Yapay zekâ', 'hedef': 'ChatGPT · Gemini · Copilot',
         'once': 'Bu sözleşmeyi özetle\nMüşteri: Ayşe Yılmaz\nKart: 4111 1111 1111 1111\nYenileme mart ayında',
         'sonra': 'Bu sözleşmeyi özetle\nMüşteri: A*** Y*****\nKart: 4111 **** **** 1111\nYenileme mart ayında'},
        {'ad': 'Tarayıcı yüklemesi', 'hedef': 'musteriler.csv',
         'once': 'TR33 0006 1005 1978 6457 8413 26\nbölge: marmara · plan: yıllık\nTR12 0001 0012 3456 7890 1234 56',
         'sonra': 'TR33 **** **** **** **** **13 26\nbölge: marmara · plan: yıllık\nTR12 **** **** **** **** **34 56'},
        {'ad': 'E-posta', 'hedef': 'kişisel adres',
         'once': 'Perşembe görüşürüz\nT.C. Kimlik No: 10000000146\nHesap: 000123456789\nGündem ektedir',
         'sonra': 'Perşembe görüşürüz\nT.C. Kimlik No: *********46\nHesap: ********6789\nGündem ektedir'},
        {'ad': 'USB bellek', 'hedef': 'çıkarılabilir disk',
         'once': 'kisiler.txt · +90 532 555 01 43\n3Ç-sunum.pptx\nfiyat-listesi · 5555 5555 5555 4444',
         'sonra': 'kisiler.txt · +90 532 555 01 **\n3Ç-sunum.pptx\nfiyat-listesi · 5555 **** **** 4444'},
    ],
    'ilkeBaslik': 'Güvenlik kararı verinin bağlamıyla başlar.',
    'ilkeAciklama': 'Bir dosyanın adı, içindekinin hassas olup olmadığını nadiren söyler. Doğru koruma için içeriği, kullanıcının eylemini, hedefi ve geçerli politikayı birlikte bilmek gerekir.',
    'ilkeler': [
        {'baslik': 'Bilgiyi tanıyın', 'metin': 'İçerik incelemesi, bağlam analizi, parmak izi, birebir veri eşleştirme ve OCR ile hassas veriyi bulun.'},
        {'baslik': 'Doğru politikayı uygulayın', 'metin': 'Kritik veri hareketinin izleneceğine, uyarılacağına, kaydedileceğine veya engelleneceğine gerçek zamanlı karar verin.'},
        {'baslik': 'Ne olduğunu anlayın', 'metin': 'İmzalı politika olaylarını, eşleşen tespitçileri ve dosyanın tüm zaman çizelgesini tek ekranda inceleyin.'},
    ],
    'moduller': [
        {'eyebrow': 'Veri keşfi ve sınıflandırma', 'baslik': 'Neyi koruduğunuzu bilin.',
         'metin': 'Hassas iş bilgisini bulun, içeriğini ve bağlamını anlayın, güvenlik ekibinin karar vermesini kolaylaştıran sınıflandırmaları uygulayın.',
         'maddeler': ['TEDARİKÇİ-SÖZLEŞMESİ-2026.PDF', 'Sözleşme', 'Fiyat modeli', 'Kişisel veri', 'Gizli'],
         'link': _l('Veri sınıflandırmayı inceleyin', '/platform/veri-siniflandirma/')},
        {'eyebrow': 'Veri sızıntısı önleme', 'baslik': 'Hassas verinin nereye gittiğine siz karar verin.',
         'metin': 'USB, yazdırma ve pano gibi uç nokta eylemlerinden e-postaya, web yüklemelerine ve bulut iş akışlarına kadar her kanalda aynı politikayı uygulayın. İhlalleri tam bağlamıyla inceleyin.',
         'maddeler': [],
         'link': _l('DLP\'yi inceleyin', '/platform/dlp/')},
        {'eyebrow': 'Yapay zekâ güvenliği', 'baslik': 'Hassas veri korumasını yapay zekâya taşıyın.',
         'metin': 'Komutları ve yanıtları gerçek zamanlı inceleyerek dış dil modellerine, tarayıcıdaki yapay zekâ araçlarına ve kod asistanlarına (Copilot, Cursor, Claude Code gibi) veri sızmasını önleyin.',
         'maddeler': [],
         'link': _l('Yapay zekâ güvenliğini inceleyin', '/yapay-zeka-guvenligi/')},
    ],
    'kapiBaslik': 'Veri tek kapıdan çıkmaz.',
    'kapiMetin': 'Gizli bir tablo USB belleğe kopyalanabilir, e-postaya eklenebilir, tarayıcıdan yüklenebilir veya bir yapay zekâ komutuna yapıştırılabilir. Her iş akışının riski farklıdır ama temeldeki soru aynıdır: bu bilgi nedir ve nasıl ele alınmalı?\n\nKorvia veri bağlamını uç noktada, ağda, bulutta ve yapay zekâda politikaya dayalı korumayla birleştirir.',
    'dagitimBaslik': 'Esnek kurulum, net veri kontrolü.',
    'dagitimMetin': 'Kurum içinde, özel bulutunuzda veya yönetilen hizmet olarak çalıştırın. Politikaların, içerik incelemesinin ve olay kayıtlarının nerede işlendiğine siz karar verirsiniz. Yönetilen güvenlik hizmeti (MSSP) iş ortakları da Korvia\'yı hizmet olarak sunabilir.',
    'dagitimSecenekleri': [
        {'baslik': 'Kurum içi', 'metin': 'Tüm bileşenler ağınızda. İnternetten yalıtılmış ağlarda da çalışır.'},
        {'baslik': 'Özel bulut', 'metin': 'Kendi bulut kiracılığınızda, verinin yerini siz seçersiniz.'},
        {'baslik': 'Yönetilen hizmet', 'metin': 'Platformu biz veya iş ortağınız işletir; ajanlar sizde kalır.'},
    ],
    'pocNot': 'Kanıt bir sunum değil, kendi verinizle yapılan bir testtir.',
})

# ---------------- SSS ----------------
yaz('sss.yaml', {
    'baslik': 'Sık sorulan sorular',
    'ozet': 'Korvia\'nın neyi tespit ettiği, nasıl kurulduğu, neyi sakladığı ve nasıl değerlendirileceği hakkında doğrudan cevaplar.',
    'gruplar': [
        {'ad': 'Genel', 'sorular': [
            {'soru': 'DLP (veri sızıntısı önleme) nedir?', 'cevap': 'DLP, hassas verinin izinsiz olarak kurum dışına çıkmasını durduran teknoloji ve süreçlerin bütünüdür. Modern DLP yalnızca e-postayı kapsamaz: uç noktalar, web, bulut uygulamaları, USB cihazlar ve yapay zekâ servisleri de verinin hareket ettiği ve sızdığı kanallardır.'},
            {'soru': 'Korvia geleneksel DLP\'den ne bakımdan farklı?', 'cevap': 'Üç noktada. Yapay zekâ veri güvenliği platformun çekirdeğindedir; çalışanların yapay zekâ servislerine ne gönderdiğini içerik ve bağlamıyla görürsünüz. Tespit tek bir motorda çalışır. Kararlar da ikili değildir: izleme, uyarma, kaydetme ve engelleme bağlama göre seçilir.'},
            {'soru': 'Platform hangi modüllerden oluşur?', 'cevap': 'Veri Keşfi ve DSPM, Veri Sınıflandırma, Uç Nokta DLP, Ağ ve E-posta DLP, Bulut DLP, Yapay Zekâ Güvenlik Duvarı, Yapay Zekâ Veri Güvenliği, Tespit Motoru ve İnceleme. Platform modülerdir; ihtiyacınız olanla başlayıp genişletebilirsiniz.'},
            {'soru': 'Yalnızca kart veya kimlik numarası gibi yapısal veriyi mi tespit eder?', 'cevap': 'Hayır. Kart, T.C. kimlik, vergi ve IBAN numaraları yalnızca biçimle değil sağlama (checksum) doğrulamasıyla kontrol edilir; bu yanlış alarmı azaltır. Belge parmak izi ve içerik analizi tasarım, kaynak kod, fiyat modeli ve formül gibi yapısal olmayan varlıkları da tanır. OCR taranmış belgeleri ve görselleri kapsar.'},
        ]},
        {'ad': 'Teknik', 'sorular': [
            {'soru': 'Ajanlı mı, ajansız mı çalışır?', 'cevap': 'İkisi de. Hafif bir uç nokta ajanı veri hareketini denetler ve içeriği cihazda inceler. Ağ paylaşımlarındaki keşif ise yönetim cihazından ajansız çalışır; dosya sunucusuna ajan kurmanız gerekmez.'},
            {'soru': 'Hangi işletim sistemleri destekleniyor?', 'cevap': 'Windows (imzalı MSI paketi, Grup İlkesi ile sessiz kurulum) ve Linux (Debian, Ubuntu, RHEL, Rocky ve SUSE paketleri). macOS kapsamı için satış ekibimize danışın. Yönetim bileşeni tek bir sanal makinedir.'},
            {'soru': 'Uç nokta performansını etkiler mi?', 'cevap': 'Ajan, politikayla ayarlanabilen bir işlemci sınırının altında kalır ve sınıra yaklaştıkça kendini yavaşlatır. Bellek ve disk etkisini POC sırasında kendi donanımınızda ölçmenizi öneririz; ölçümleri sizinle birlikte değerlendiririz.'},
            {'soru': 'Mevcut etiketleme araçlarımızla çalışır mı?', 'cevap': 'Evet. Korvia mevcut etiketleri tespit motorunun girdilerinden biri olarak okur ve politikaya bağlar. Platform etiketleri, Office belgelerindeki Microsoft duyarlılık (MIP) etiketleriyle eşlenebilir. Diğer etiketleme araçlarıyla birlikte çalışma POC\'de doğrulanır.'},
            {'soru': 'SIEM veya SOAR entegrasyonu var mı?', 'cevap': 'Evet. Olaylar ve denetim kaydı SIEM\'inize syslog üzerinden (CEF veya RFC 5424, TCP veya TLS) gider. Yalnızca üst veri gönderilir, hassas içerik asla gönderilmez. JSON REST API ve CSV/JSON dışa aktarım SOAR ve raporlama akışlarını besleyebilir.'},
        ]},
        {'ad': 'Yapay zekâ veri güvenliği', 'sorular': [
            {'soru': 'Hangi yapay zekâ servislerini görebiliriz?', 'cevap': 'ChatGPT gibi üretken yapay zekâ siteleri, Teams, Slack ve Discord\'a dosya yüklemeleri, WhatsApp Web, dosya paylaşım siteleri ve bulut depolama. Bazı servislerde içerik incelenir; bazılarında erişim veya yükleme kararı uygulanır. Kesin kapsam tablosunu POC öncesinde paylaşırız.'},
            {'soru': 'Kurumsal yapay zekâ hesabını kişisel hesaptan ayırabilir mi?', 'cevap': 'Evet. Kurumsal ve kişisel hesabı ayırmak bağlam değerlendirmesinin parçasıdır. Aynı serviste kurumsal hesaba yüklemeye izin verirken aynı içeriğin kişisel hesaba gitmesini engelleyebilirsiniz.'},
            {'soru': 'Gölge yapay zekâ nedir, nasıl yönetilir?', 'cevap': 'Gölge yapay zekâ, kurumun onayı veya bilgisi dışında yapay zekâ araçlarının kullanılmasıdır. Korvia önce bu kullanımı görünür kılar: hangi kullanıcı, hangi servis, hangi içerik. Ardından her şeyi engellemek yerine izleme ve uyarıyla başlayabilirsiniz.'},
            {'soru': 'Yapay zekâyı tamamen engellemek zorunda mıyız?', 'cevap': 'Hayır, bunu önermiyoruz. Amaç, hassas içeriğin çıkmasını durdururken çalışanların verimli kalmasıdır: içerik türüne, hesaba ve bağlama göre izleyin, uyarın, kaydedin veya engelleyin. Kullanıcı bir iş gerekçesi yazıp devam da edebilir.'},
        ]},
        {'ad': 'Kurulum', 'sorular': [
            {'soru': 'Hangi kurulum modelleri var?', 'cevap': 'Dört model: düzenleyici ve yalıtılmış ağ ihtiyaçları için kurum içi; kendi altyapınızda özel bulut; platformu sizin için işlettiğimiz yönetilen hizmet; ve bir hizmet sağlayıcı üzerinden MSSP modeli.'},
            {'soru': 'Verimiz yurt dışına çıkar mı?', 'cevap': 'Kurum içi ve özel bulut modellerinde veri sizin seçtiğiniz altyapıda kalır. Taranan içerik ve tespit edilen değerler yönetim cihazından çıkmaz; ürün internet bağlantısı olmadan da tam işlevle çalışır. Mimari belgesi her bileşenin nerede çalıştığını gösterir.'},
            {'soru': 'Kurulum ne kadar sürer?', 'cevap': 'Kapsama bağlıdır. Zamanın çoğu yaygınlaştırmaya gider: dizin entegrasyonu, neyin taranacağını seçmek, ilk tarama, ince ayar ve ajan dağıtımı. Canlıya geçiş takvimi uç nokta sayısına göre belirlenir ve yazılı bir yol haritasıyla paylaşılır.'},
        ]},
        {'ad': 'Gizlilik ve güven', 'sorular': [
            {'soru': 'Korvia hangi veriyi inceler ve saklar?', 'cevap': 'Neyin incelendiğini, olay kayıtlarının ne içerdiğini, nerede, ne kadar süre saklandığını ve kimin okuyabildiğini belgeleriz. Olaylar, tarama geçmişi ve günlük özetler varsayılan olarak 400 gün, denetim kaydı 24 ay saklanır. Her iki süreyi de kısaltabilirsiniz.'},
            {'soru': 'Olay kayıtlarında hassas içeriğin kopyası tutulur mu?', 'cevap': 'Olay kayıtları hangi tespitçinin eşleştiğini ve eşleşen değerleri tutar. Yetkili analistler bunları inceleme için görür; kullanıcı bildirimlerinde değer maskelenir. Dosyanın kendisi yalnızca "gölge kopya" eylemi tanımlı kurallarda alınır. Kanıtlar şifrelenir ve her erişim kaydedilir.'},
            {'soru': 'KVKK uyum çalışmalarını nasıl destekler?', 'cevap': 'Korvia programınızın teknik tarafını güçlendirir: kişisel veriyi bulmak, hareketini izlemek ve izinsiz aktarımı durdurmak. Kişisel veri envanteri ve dönem karşılaştırmaları gibi denetim kanıtları üretir. Hukuki sorular için hukuk danışmanınızın görüşünü alın.'},
        ]},
        {'ad': 'Satın alma ve POC', 'sorular': [
            {'soru': 'Satın almadan önce kendi verimizle test edebilir miyiz?', 'cevap': 'Evet, bunu öneriyoruz. POC dört aşamadan oluşur: veriyi ve başarı ölçütlerini tanımlayın, politikaları yapılandırın, gerçekçi senaryoları test edin, sonuçları değerlendirin. POC rehberi süreci ayrıntılı anlatır.'},
            {'soru': 'Lisanslama nasıl işler?', 'cevap': 'Lisans; uç nokta ajanı sayısına, seçilen modüllere ve 1, 2 veya 3 yıllık süreye göre yapılandırılır. Lisans yönetim cihazına bağlıdır ve lisans dosyasıyla çevrim dışı etkinleştirilir. Teklif için satış ekibimize yazın.'},
            {'soru': 'Modülleri ayrı ayrı alabilir miyiz?', 'cevap': 'Evet. Platform modülerdir. Örneğin Uç Nokta DLP ve Yapay Zekâ Veri Güvenliği ile başlayıp sonraki aşamada Veri Keşfi ve İnceleme ekleyebilirsiniz.'},
            {'soru': 'Mevcut DLP ürünümüzden geçiş zor mu?', 'cevap': 'Hayır. Mevcut ürününüzdeki kurallar ve politikalar içe aktarılabilir; karşılığı olmayan öğeler raporlanır. İçe aktarılan kurallar karşılaştırma için önce izleme modunda çalışır; emin olduğunuzda geçişi tamamlarsınız.'},
        ]},
        {'ad': 'Destek', 'sorular': [
            {'soru': 'Desteğe nasıl ulaşırız?', 'cevap': 'Destek e-posta adresimize yazın. Yanıt hedefleri sorunun önem derecesine ve destek sözleşmenize göre belirlenir. Destek sayfası önem derecelerini ve talepte nelerin yer alması gerektiğini anlatır.'},
            {'soru': 'Destek hangi dilde?', 'cevap': 'Türkçe. Yönetim konsolu Türkçe ve İngilizce kullanılabilir; destek kapsamı ve saatleri lisans veya destek sözleşmenizde tanımlanır. İş ortakları yönetilen hizmet ve MSSP müşterilerine birinci seviye destek verebilir.'},
        ]},
    ],
})

# ---------------- Sözlük ----------------
terimler = [
    ('dlp', 'DLP nedir?', 'Veri sızıntısı önleme (DLP), hassas verinin izinsiz olarak kurum dışına çıkmasını durduran teknoloji ve süreçlerin bütünüdür.', '/platform/dlp/', 'Korvia DLP'),
    ('veri-siniflandirma', 'Veri sınıflandırma nedir?', 'Kurumun hangi bilgiye sahip olduğunu bulma ve bu bilgiyi hassasiyetine göre "Genel", "Kurum İçi" veya "Gizli" gibi etiketlerle işaretleme sürecidir.', '/platform/veri-siniflandirma/', 'Veri Sınıflandırma'),
    ('dspm', 'DSPM nedir?', 'Veri güvenliği duruş yönetimi (DSPM); hassas verinin nerede durduğunu, kimin sahibi olduğunu, kimin erişebildiğini ve ne kadar açıkta olduğunu bulma pratiğidir.', '/platform/veri-kesfi-dspm/', 'Veri Keşfi ve DSPM'),
    ('yapay-zeka-guvenlik-duvari', 'Yapay zekâ güvenlik duvarı nedir?', 'İnsanlar veya uygulamalar ile yapay zekâ modelleri arasında duran bir kontrol noktasıdır. Giden komutları ve dönen yanıtları politikaya göre inceler.', '/yapay-zeka-guvenligi/yapay-zeka-guvenlik-duvari/', 'Yapay Zekâ Güvenlik Duvarı'),
    ('golge-yapay-zeka', 'Gölge yapay zekâ nedir?', 'Yapay zekâ araçlarının kurumun onayı veya bilgisi dışında kullanılmasıdır.', '/cozumler/golge-yapay-zeka/', 'Gölge Yapay Zekâ'),
    ('belge-parmak-izi', 'Belge parmak izi nedir?', 'Hassas belgeleri bir kalıba göre değil, içeriklerine göre tanıma yöntemidir. Bir belgenin tamamı da tek bir paragrafı da yakalanabilir.', '/platform/tespit-motoru/', 'Tespit Motoru'),
    ('birebir-veri-eslestirme', 'Birebir veri eşleştirme nedir?', 'Birebir veri eşleştirme (EDM), içeriği müşteri veya kart verisi gibi kendi kayıtlarınızdan oluşturulan korumalı bir dizinle karşılaştırır.', '/platform/tespit-motoru/', 'Tespit Motoru'),
    ('yapay-zeka-dlp', 'Yapay zekâ DLP nedir?', 'Yapay zekâ araçlarını bir veri kanalı olarak ele alan veri sızıntısı önlemedir. Komutlar ve yüklemeler diğer kanallar gibi politikaya tabi olur.', '/yapay-zeka-guvenligi/yapay-zeka-veri-guvenligi/', 'Yapay Zekâ Veri Güvenliği'),
]
for i, (slug, terim, tanim, yol, etiket) in enumerate(terimler):
    yaz(f'sozluk/{slug}.yaml', {'terim': terim, 'sira': i + 1, 'tanim': tanim, 'ilgiliYol': yol, 'ilgiliEtiket': etiket})
