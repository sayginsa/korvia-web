import os
from ortak import KOK

YAZILAR = [
    ('yapay-zekayi-engellemek-ise-yarar-mi', 'Yapay zekâyı engellemek işe yarar mı?', 'Yapay Zekâ Güvenliği', 4,
     'Uzun süre değil. Engelleme, yapay zekâ kullanımını göremediğiniz yerlere taşır. Onaylı araçlara izin verip her durdurmayı açıklamak daha iyi sonuç verir.',
     """Yapay zekâ araçlarına konan katı bir engel nadiren uzun süre işe yarar. Görebildiğiniz trafiği durdurur, geri kalanını göremediğiniz yerlere taşır: telefonlara, kişisel dizüstü bilgisayarlara, ev ağlarına. Asıl soru yapay zekânın engellenip engellenmeyeceği değil; hangi verinin hangi araca ulaşacağı ve cevap "hayır" olduğunda çalışanın ne gördüğüdür.

## Engelleme neden doğru gibi gelir?

Engelleme ilk hamle olarak makul nedenlere dayanır. Risk gerçektir, kurallar açıktır. Bir sohbet botuna yapıştırılan müşteri listesi kurumdan çıkmıştır. Kişisel bir hesaba yüklenen kaynak kod artık sizin elinizde değildir. Hukuk ekibi bir çizgi çekilmesini ister ve engellenmiş bir alan adı herkesin gösterebileceği bir çizgidir.

Üstelik hızlıdır. Web filtresine tek bir kayıt eklenir ve sorun çözülmüş gibi görünür. Pano sessizleşir; sessiz bir pano da denetim gibi görünür.

Sorun bu sessizliktedir. Size izlediğiniz ağda trafiğin durduğunu söyler. İşin durduğunu söylemez.

## İş nereye gider?

Çalışanlar bu araçları zaman kazandırdığı için kullanır. Bir özet bir saat yerine bir dakikada çıkar. İlk taslak toplantı başlamadan hazırdır. Kurumsal araç engellendiğinde teslim tarihi yerinde durur; iş başka yere taşınır.

Mobil veriye bağlı bir telefona taşınır. Mutfak masasındaki kişisel dizüstüne taşınır. Filtrenin henüz duymadığı yeni bir yapay zekâ servisine taşınır; çünkü yenileri hiçbir listenin yetişemeyeceği hızda çıkar.

Artık aynı veri aynı araçlardadır ama üç şey eksiktir: göremezsiniz, kaydınız yoktur ve bunu yapan kişi güvenliğin etrafından dolaşılacak bir şey olduğunu öğrenmiştir. Dikkatli çalışanları saklanmaya iten bir politika riski küçültmez, bulunmasını zorlaştırır.

## Her şeye izin vermek de neden başarısız olur?

Tersi cevabın da kendi başarısızlığı vardır. Her şeye izin verilir ve hiçbir şey kontrol edilmezse sohbet botundaki müşteri listesini aylar sonra, genellikle başkasından öğrenirsiniz. "Müşteri verisini yapıştırmayın" diyen yazılı bir politika iyi bir başlangıçtır; ama her çalışanın her yoğun günde bunu hatırlamasına dayanır. İyi çalışanlar da hata yapar; çeyrek sonunda yorgun biri daha çok yapar.

Duvar ile açık kapı arasındaki seçim sahte bir seçimdir. İkisi de asıl ihtiyacınızı karşılamaz: veri hareket ettiği anda, veri hakkında verilen bir karar.

## Daha iyi işleyen yol

Orta yolun dört parçası var ve hiçbiri sıra dışı değil.

**Onaylı araçlara izin verin.** Kurumunuzun sözleşmesi olan servisleri seçin ve çalışanların kullanmasına izin verin. Kurumsal hesap size saklama şartları, yönetici denetimleri ve denetim kayıtları verir. Burada "evet" demek, politikanın geri kalanını inandırıcı kılar.

**Kişisel hesapları farklı ele alın.** Aynı servis kurumsal hesapta güvenli, kişisel hesapta riskli olabilir. Alan adının tamamını engellemek onaylı aracı bozar; izin vermek kişisel hesabı içeri alır. Politikanın farkı görmesi gerekir.

**Hedefe değil, içeriğe göre karar verin.** Komutların çoğu zararsızdır. Bir tabloyu biçimlendirme sorusu müdahale gerektirmez. Müşteri listesi taşıyan bir komut gerektirir. Hassas değerler maskelenebilir; komut yine gider, çalışan işine devam eder.

**Durdurmayı o anda açıklayın.** Sessiz bir engel hiçbir şey öğretmez ve bir geçici çözüm aranmasına yol açar. Neyin bulunduğunu ve neden önemli olduğunu söyleyen kısa bir mesaj, politikayı tam gerektiği anda öğretir. Durumun belirsiz olduğu yerde doğrudan reddetmek yerine iş gerekçesi isteyin ve cevabı kayıt altına alın.

## Bakarak başlayın

Bunların hiçbiri uygulamayla başlamak zorunda değil. İlk adım ne olduğunu anlamaktır: hangi araçlar, hangi ekipler, hangi hesaplar ve ne tür veriler. Önce izleme modunda çalışın; kimsenin gününü değiştirmeden gerçek riskin nerede olduğunu öğrenirsiniz.

Bu ilk görünüm tartışmayı genellikle kapatır. Güvenlik ekibi genel olarak yapay zekâyı tartışmayı bırakır; tek bir ekipten, tek bir araçtan ve tek bir veri türünden konuşmaya başlar. O vaka için yazılan kural savunması kolay, açıklaması kolay ve çalışanları telefonlarına gönderme ihtimali çok daha düşük bir kuraldır.

Oradan adım adım ilerleyin. En önemli veride uyarın, çalışanların verdiği gerekçeleri kaydedin ve riskin açık olduğu yerde engelleyin. İzleme moduyla başlayan bir politika yeni bir yaygınlaştırma gerektirmeden sıkılaştırılabilir.

## Kendinize sormanız gerekenler

Bir engelin işe yarayıp yaramadığını üç soru gösterir:

- Geçen hafta çalışanlarınızın hangi yapay zekâ araçlarını, hangi cihazlardan ve hangi hesaplarla kullandığını söyleyebilir misiniz?
- Bir komut durdurulduğunda çalışan nedenini öğreniyor mu?
- Engel yarın kaldırılsa neyin değiştiğini bilir misiniz?

Bunlardan birine dürüst cevabınız "hayır" ise engel size denetim değil, sessiz bir pano veriyor.

Amaç hiçbir zaman çalışanların yapay zekâ kullanmasını durdurmak değildi. Amaç, iş devam ederken hassas verinin yanlış yere gitmesini önlemek. [Yapay Zekâ Veri Güvenliği'nin aynı politikayı komutlara ve yüklemelere nasıl uyguladığını okuyun.](/yapay-zeka-guvenligi/yapay-zeka-veri-guvenligi/)
"""),
    ('anahtarlari-komuttan-uzak-tutun', 'Anahtarları komuttan uzak tutun', 'Yapay Zekâ Güvenliği', 4,
     'Bir kodlama komutundaki risk nadiren algoritmadır. Asıl risk onunla birlikte gidenlerdir: anahtarlar, bağlantı dizeleri ve test verisindeki müşteri bilgisi.',
     """Bir kodlama komutundaki asıl risk nadiren algoritmadır. Asıl risk kodla birlikte gidenlerdir: bir yapılandırma dosyasında unutulmuş API anahtarı, bir bağlantı dizesi, test verisindeki müşteri bilgisi, kurum içi bir sunucu adı. Kodu yapay zekâ asistanlarından korumak, geliştiricileri asistandan uzak tutmakla değil, bunları komuttan uzak tutmakla başlar.

## Gerçekte ne çıkıyor?

Bir geliştiricinin, hata veren bir fonksiyonu düzeltmesi için asistandan yardım istediğini düşünün. Asistanın yardım edebilmesi için bağlama ihtiyacı vardır; çevredeki dosyaları okur. Bu dosyalar hiçbir zaman dışarıdan bir okuyucu düşünülerek yazılmamıştır. Gece yarısı yapılmış bir düzeltmeden kalan sabit bir token, üretimden kopyalanmış örnek bir kayıt, kodun konuştuğu sunucunun adını veren bir yorum satırı taşırlar.

Bunların hiçbirini paylaşmaya kimse karar vermedi. Araç onları topladı; çünkü araç böyle çalışır. Bir depoyu okuyabilen ajan o depodaki her şeyi okuyabilir ve bunu saatte defalarca yapabilir.

Bu yüzden "gizli anahtarları yapay zekâ araçlarına yapıştırmayın" gibi yazılı bir kural yetersiz kalır. Geliştirici hiçbir şey yapıştırmadı. Ajan aldı.

## Asistanları yasaklamak neden işe yaramaz?

Bazı kurumlar kod asistanlarını tamamen yasaklayarak cevap verir. Yasağı duyurmak kolay, sürdürmek zordur. Geliştiriciler bu araçlarla daha hızlıdır ve bunu bilirler. Onaylı yol kapandığında iş kişisel bir hesaba veya ev bilgisayarına taşınır; aynı kod aynı modellere, bu kez kimse bakmadan ulaşır.

Yasak en önemli soruyu da cevapsız bırakır. Hangi kodun önemli olduğu hakkında hiçbir şey söylemez. Bir pazarlama sitesi ile ana ödeme servisi aynı risk değildir; ikisine aynı davranmak ya herkesi yavaşlatır ya hiçbir şeyi korumaz.

## Denetlemeye değer üç şey

Uygulanabilir bir yaklaşımın üç parçası vardır.

**Komutta ne olduğunu tanıyın.** Kaynak kod kendi başına bir veri kategorisidir; politika onu bir pazarlama belgesinden farklı ele alabilmelidir. Gizli anahtarların kendi tespiti olmalıdır: API anahtarları, token'lar ve bağlantı dizeleri başka hiçbir şeye benzemez ve yola çıkmadan bulunabilir. Test verisindeki kişisel veri, diğer her yerdeki kişisel veri gibi yakalanır.

**Yolu denetleyin.** Ajan kancaları Claude Code ve Codex gibi araçlarda bir komutu gönderilmeden kontrol edebilir. Bir yapay zekâ ağ geçidi Anthropic ve OpenAI API trafiğine tek çıkış ve arkasında bir denetim kaydı verir. Copilot ve Cursor da kapsanmalıdır; çünkü geliştiriciler nadiren tek bir araç kullanır.

**Depolarınızı sınıflandırın.** Her kod aynı kuralı hak etmez. Depoları Kırmızı, Sarı veya Yeşil olarak sınıflandırmak politikayı riske uydurur. Kırmızı bir depo kritik kod barındırır; asistan onu hiç okuyamaz. Sarı bir depo dikkatle ve kayıt altında kullanılabilir. Yeşil bir depo normal kullanıma açıktır.

## Maskelemenin burada yapamadıkları

Maskeleme kişisel veride iyi çalışır. Bir ad veya hesap numarası bir etiketle değiştirilir, modele gönderilir ve yanıtta geri yüklenir. Kod böyle çalışmaz. Mantığı maskelenmiş bir fonksiyon artık bir fonksiyon değildir; asistan ona yardım edemez.

Bu, kararı basitleştirir. Kişisel değerleri yapabildiğiniz yerde maskeleyin, gizli anahtarları her seferinde durdurun ve kritik kod için karar engellemek olsun. Karar motoruna ulaşılamıyorsa Kırmızı bir depo kapalı kalmalıdır; böylece bir ağ arızası sessizce açık bir kapıya dönüşmez.

## Geliştiricilerin yaşayabileceği bir politika

Bir politikanın sınavı, yoğun bir cuma günü de uygulanıp uygulanmadığıdır. Birkaç alışkanlık yardımcı olur.

- Kurumsal hesaptaki onaylı asistana izin verin ve gündelik kodda normal çalışmasına izin verin.
- Bir komutu yalnızca gizli bir anahtar veya kritik bir depo söz konusu olduğunda durdurun ve nedenini tek satırda söyleyin.
- Geliştiriciye bir çıkış yolu verin: anahtarı kaldırın, onaylı hesabı kullanın veya işi izin veren bir depoya taşıyın.
- Olayı kaydedin; ardından anahtar yenilensin ve bir ders çıkarılsın.

Durdurulan bir komut kendi başına faydalıdır. Çoğu zaman, dışarıdan biri bulmadan çok önce, depoda hiç olmaması gereken bir anahtarı ortaya çıkarır.

## Nereden başlamalı?

Bakarak başlayın. Hangi asistanların, hangi hesaplarla, hangi depolara karşı kullanıldığını öğrenin. Ardından depolarınızı sınıflandırın; sızdığında en çok canınızı yakacak birkaç depoyla başlayın. Sonra gizli anahtar tespitini açın; tek bir hatanın en pahalıya mal olduğu yer orasıdır.

Yapay zekâyı mühendislikten yasaklamak kodu korumaz. Yalnızca kodun nasıl kullanıldığını gizler. Amaç anahtarları dışarıda tutmak ve geliştiricilerin devam etmesine izin vermektir. [Kod asistanlarının Korvia'da nasıl kapsandığını okuyun.](/yapay-zeka-guvenligi/kod-asistanlari/)
"""),
    ('kurumsal-hesap-mi-kisisel-hesap-mi', 'Kurumsal hesap mı, kişisel hesap mı?', 'Yapay Zekâ Güvenliği', 3,
     'Aynı yapay zekâ servisi, çok farklı iki risk. Yalnızca alan adına bakan bir politika ikisini ayıramaz.',
     """Aynı yapay zekâ servisi bir hesapta güvenli, diğerinde riskli olabilir. Kurumunuzun kiracısında oturum açmış bir çalışan sözleşmenizin kapsamındadır: saklama şartları, yönetici denetimleri ve denetim kayıtları. Aynı çalışan kişisel hesabındayken kendi tüketici şartlarının kapsamındadır. Yalnızca alan adına bakan bir politika bu ikisini ayıramaz.

## Tek adres, çok farklı iki risk

Ağ açısından iki oturum birbirine benzer. Aynı adrese giderler, aynı uygulamayı kullanırlar. Bir web filtresi tek bir hedef görür.

Kurum için ise bundan farklı olamazlar. Kurumsal hesapta şartları siz seçtiniz. Verinin ne kadar saklandığını, bir modeli eğitip eğitmediğini ve kayıtları kimin okuyabildiğini bilirsiniz. Biri ayrıldığında hesap kapanır, geçmiş sizde kalır.

Kişisel hesapta hiçbir şeyi siz seçmediniz. Veri, kişinin aceleyle kabul ettiği şartlar altında durur. O kişi kurumdan ayrıldığında sohbet geçmişi de onunla gider. Kaydınız, saklama denetiminiz ve geri bir şey isteme imkânınız yoktur.

## Alan adı kuralları neden iki yönde de başarısız olur?

Bununla karşılaşan ekiplerin çoğu zaten sahip olduğu araca uzanır ve bu araç onlara iki zayıf seçenek sunar.

Alan adını engellerseniz onaylı aracı bozarsınız. Ona güvenen çalışanlar işi bırakır ya da başka bir yol bulur. Güvenlik, faydalı şeyi elinden alan birim hâline gelir.

Alan adına izin verirseniz kişisel hesap aynı kapıdan girer. Kurumsal bir servis için ödeme yapmış, yanındaki yan kapıyı açık bırakmışsınızdır.

Yaygın bir uzlaşma yazılı bir kuraldır: yalnızca kurum hesabını kullanın. Sahip olmaya değer ama çalışanların, ikisinin de açık olabileceği bir tarayıcıda hangi hesapta oturum açtığını fark etmesine dayanır. Yanlış profilden iş mesajı göndermiş herkes bunun nasıl sonuçlandığını bilir.

## Hesaba duyarlı politika neye benzer?

Çözüm, politikanın hangi hesabın kullanıldığını bilmesi ve ikisine farklı davranmasıdır. Uygulamada kurallar kısadır.

- **Onaylı kurumsal hesap:** izin verin, içeriği kontrol edin ve kayıt tutun.
- **Aynı serviste kişisel hesap:** çalışanı uyarın, iş gerekçesi isteyin veya engelleyin.
- **Her ikisinde hassas içerik:** kararı alan adı değil, tespit motoru verir.

Üçüncü kural göründüğünden önemlidir. Kurumsal hesap her komutu kabul edilebilir kılmaz. Bir müşteri listesi veya bir sözleşme, nereye giderse gitsin politikanızın dışında kalabilir. Hesap başlangıç noktasını, içerik sonucu belirler.

## Çalışan ne görür?

İyi politika o anda kendini gösterir. Biri bir müşteri listesini bir sohbet botuna yapıştırır ve kişisel hesapta olduğunu fark etmemiştir. Sessiz bir başarısızlık yerine kısa bir mesaj görür: bu müşteri verisine benziyor, bu kişisel bir hesap, lütfen kurumsal olanı kullanın.

Bu mesaj üç faydalı iş yapar. Veriyi durdurur. Kuralı önemli olduğu noktada öğretir. Çalışana işi bitirmesi için hemen bir yol da verir; çünkü zaten bunun için oradaydı.

Bunu hiçbir neden göstermeyen bir engelleme sayfasıyla karşılaştırın. Biri çalışanları bilgilendirip çalışır hâlde bırakır. Diğeri geçici çözüm aramaya iter.

## Kendi kurulumunuz için sorular

Birkaç soru nerede durduğunuzu gösterir.

- Yalnızca hangi servislerin değil, hangi yapay zekâ hesaplarının kullanıldığını görebiliyor musunuz?
- Politikanız aynı servisteki kurumsal ve kişisel hesaba farklı davranıyor mu?
- Biri durdurulduğunda hangi hesapta olduğunu ve sonra ne yapacağını öğreniyor mu?
- Biri ayrıldığında, onun işi için oluşturulan yapay zekâ geçmişine ne oluyor?

Cevapların belirsiz olduğu yerde izleme moduyla başlayın. Kullanımın ne kadarının kişisel hesaplardan geçtiğini ve hangi ekiplerde olduğunu öğrenin. Çoğu zaman bu, onaylı aracın karşılamadığı gerçek bir ihtiyacı olan küçük bir gruptur; herhangi bir kural değişmeden önce yapılmaya değer bir konuşmadır.

## Bu ayrımın amacı

Kurumsal bir asistanı onaylayıp kişisel olanı kısıtlamak teknik bir ayrıntı değildir. Net bir politikayı mümkün kılan şey budur. Çalışanların istediği araca "evet" diyebilir, sözleşmenizin korumalarını sürdürebilir ve çıkmaması gereken veriyi, servise güvenenler için onu bozmadan durdurabilirsiniz.

[Yapay Zekâ Veri Güvenliği'nin kurumsal ve kişisel hesapları nasıl ayırdığını okuyun.](/yapay-zeka-guvenligi/yapay-zeka-veri-guvenligi/)
"""),
    ('ajan-ag-disinda-ne-yapar', 'Ajan ağ dışında ne yapar?', 'Veri Koruma', 3,
     'Yalnızca ofiste çalışan bir politika bir öneridir. Dizüstü bilgisayarın hiç bağlantısı olmadığında olması gerekenler.',
     """Yalnızca ofiste çalışan bir politika bir öneridir. Korvia çalışan bir dizüstü bilgisayar kurum ağından ayrıldığında ajan aldığı son politikayı saklar, cihazda uygulamaya devam eder, olanları kaydeder ve politika sunucusuna yeniden ulaşabildiğinde kanıtı geri gönderir. Koruma bir VPN'e bağlı değildir.

## Bu soru neden önemli?

Hassas işin çoğu artık ofis ağında yapılmıyor. Trende, mutfak masasında, otelde, havalimanı kapısında yapılıyor. Yalnızca ağ sınırında yaşayan her denetim, cihaz binadan çıktığı anda onu görmeyi bırakır.

Eski tasarımlar bunu trafiği VPN üzerinden merkeze zorlayarak çözdü. VPN açıkken bu işe yarar. Dizüstü çevrim dışıyken, biri iki bağlantı arasındayken veya görüntülü görüşme zorlandığı için VPN'i kapattığında hiçbir işe yaramaz. Bir USB belleğin ise hiç ağa ihtiyacı yoktur.

Yani yararlı soru basittir: denetim hiçbir yere ulaşamadığında ne yapar?

## Adım adım ne olur?

Cevabın dört parçası var.

**Politika önbellektedir.** Ajan aldığı son politikayı cihazda saklar. Kuralların ne olduğunu kimseye sorması gerekmez.

**Uygulama devam eder.** Aynı kurallar USB belleklere, yazdırmaya, panoya, yüklemelere ve yapay zekâ komutlarına uygulanır. İçerik cihazda incelenir; karar bir sunucuyu beklemek zorunda kalmaz.

**Olaylar yerel olarak kaydedilir.** Her karar cihaza yazılır: ne bulundu, hangi kural eşleşti, kim yaptı ve veri nereye gidiyordu.

**Kanıt yeniden bağlanınca merkeze döner.** Dizüstü politika sunucusuna yeniden ulaştığında kanıt yüklenir ve diğer her şeyle aynı vaka zaman çizelgesine düşer. Bir analist o kişinin haftasını tek yerde okuyabilir.

## Test etmeye değer üç durum

Çevrim dışı davranış hakkında iddiada bulunmak kolaydır; bu yüzden test etmeye değer. Bizimki dahil her ürün için üç basit kontrol:

**Kabloyu çekin.** Bir test dizüstünü tüm ağlardan ayırın ve politikanızın durdurması gereken eylemleri deneyin: etiketli bir dosyayı USB'ye kopyalayın, yazdırın, yerel bir uygulamaya yapıştırın. Sonuç ofistekiyle aynı olmalı ve kullanıcı aynı açıklamayı görmeli.

**Cihaz uzaktayken politikayı değiştirin.** Dizüstü çevrim dışıyken yeni bir kural yayımlayın, sonra yeniden bağlayın. Yeni kural gelmeli; cihaz uzaktayken kaydedilen olaylar konsolda orijinal zamanlarıyla görünmeli.

**Bir süre uzak kalın.** Cihazı bir hafta sonundan daha uzun süre ağdan uzak tutun. Uygulama sessizce sona ermemeli; döndüğünde kanıt eksiksiz gelmeli.

## Kullanıcı ne görür?

Ağ dışında çalışanların yine çalışması ve bir şeyin neden durduğunu bilmesi gerekir. Aldıkları mesaj masalarında görecekleriyle aynı olmalıdır. Politika bir iş gerekçesi istiyorsa kişi bunu yazabilir ve cevap kanıtla birlikte merkeze gider.

Bu göründüğünden önemlidir. Ofiste bir türlü, yolda başka türlü davranan bir denetim, çalışanlara kuralların nerede oturduklarına bağlı olduğunu öğretir. Tutarlı bir denetim ise kuralı öğretir.

## Sınırlar nerede?

Dürüst cevaplar sınırları da içerir. Cihazdaki bir ajan yalnızca üzerinde çalıştığı cihazı koruyabilir. Kişisel bir telefon kapsamı dışındadır; dizüstü uzaktayken yayımlanan bir politika, dizüstü yeniden bağlanana kadar uygulanmaz. İnternetteki bir servise karşı kontrol gibi canlı sorgu gerektiren her şey bağlantıya bağlıdır.

Bunların hiçbiri dizüstünden vazgeçmek için bir neden değildir. Denetiminizin tam olarak ne yaptığını bilmek ve buna göre plan yapmak için bir nedendir.

## Her üreticiye sorulacak soru

Hibrit çalışma, ağ dışı davranışı bir özellik değil temel bir gereksinim hâline getirdi. Bu yüzden doğrudan sorun: ajanınız hiç bağlantı yokken ne yapar? Hangi kanallar kapsamda kalır? Kanıt nerede tutulur ve merkeze nasıl döner?

Net bir cevap, ürünün insanların gerçekte nasıl çalıştığına göre tasarlandığını söyler. Uzun bir duraksama da bir şey söyler.

[Uç Nokta DLP'nin politikayı cihazda nasıl tuttuğunu okuyun.](/platform/dlp/uc-nokta/)
"""),
    ('pci-dss-4-0-1-ve-hareket-halindeki-veri', 'PCI DSS 4.0.1 ve hareket hâlindeki veri', 'Uyum', 3,
     'İki PCI DSS gereksinimi aslında birer veri kaybı sorunudur. İkisi de kart verisini bulabildiğinizi ve nasıl hareket ettiğini denetleyebildiğinizi varsayar.',
     """PCI DSS 4.0.1, aslında veri kaybı sorunu olan iki şey ister. Gereksinim 3.4.2, uzaktan erişim sırasında kart numaralarının kopyalanmasını veya taşınmasını durduran teknik denetimler ister. Gereksinim 12.10.7, saklanan kart numaraları olmamaları gereken bir yerde ortaya çıktığında olay müdahalesinin başlamasını ister. İkisi de kart verisini bulabildiğinizi ve nasıl hareket ettiğini, onu tutmak için kurduğunuz sistemlerin dışında da denetleyebildiğinizi varsayar.

## Ne değişti, ne zaman?

PCI DSS 4.0 2022'de yayımlandı ve bir süre isteğe bağlı kalan gereksinimler içeriyordu; kurumlar hazırlanmak için zaman buldu. Konsey Haziran 2024'te, gereksinim eklemeyen veya çıkarmayan sınırlı bir revizyon olarak 4.0.1 sürümünü yayımladı. İleri tarihli gereksinimler 31 Mart 2025'te zorunlu hâle geldi; değerlendiriciler artık bunlara bakıyor.

Programların çoğu emeğini kart sahibi veri ortamına harcar; haklı olarak. Bu iki gereksinim ise o ortamın kenarlarına, kart verisinin gündelik işe sızdığı yerlere bakar.

## Gereksinim 3.4.2: uzaktan oturumlarda kart numaraları

Metin kısadır. Uzaktan erişim teknolojileri kullanıldığında, belgelenmiş açık yetkisi ve meşru iş ihtiyacı olanlar dışında herkes için birincil hesap numaralarının kopyalanmasını veya taşınmasını önleyen teknik denetimler bulunmalıdır.

Bunun neyi kapsadığını düşünün. Uzaktan oturumdaki bir destek temsilcisi bir kart numarasını görebilir. Denetim yoksa onu panoya kopyalayabilir, yerel bir nota yapıştırabilir veya bir dosyayı kişisel bir sürücüye sürükleyebilir. Kimsenin kötü niyetli olması gerekmez; yardımsever bir alışkanlık yeter.

Bir politika belgesi bunların hiçbirini önleyemez; çünkü gereksinim teknik denetim der. Ayrıca istisnaları kanıtlamanızı ister: kime izin verildi, neden ve bu nerede yazılı. Yani uç noktada eylemi gören, veriyi tanıyan ve karar veren bir şeye, ayrıca her istisnanın kaydına ihtiyacınız var.

## Gereksinim 12.10.7: yanlış yerdeki kart numaraları

Bu gereksinim dürüst bir varsayımla başlar: kart numaraları ait olmadıkları yerlerde ortaya çıkacaktır. Bir destek talebinde yapıştırılmış bir kart. İndirilenler klasöründe duran bir döküm. Çoktan bitmiş bir projeden dosya sunucusunda kalmış bir tablo.

Gereksinim, o an için olay müdahale prosedürlerinin bulunmasını ve bu an geldiğinde başlatılmasını söyler. Prosedürler veriyle ne yapılacağına karar vermeyi, oraya nasıl geldiğini bulmayı ve nedeni düzeltmeyi içerir.

Neyi varsaydığına dikkat edin. Yalnızca tespit ettiğiniz şeye müdahale edebilirsiniz. Kart sahibi veri ortamının dışında kimse bakmıyorsa prosedür hiç çalışmaz, veri de orada kalır.

## İkisinin ortak noktası

İki gereksinim de aynı üç yeteneği ister.

**Veriyi bulun.** Uç noktaları ve dosya sunucularını kart numaraları için tarayın; on altı haneli bir sipariş numarası alarm üretmesin diye sağlama doğrulaması kullanın. Tek başına bir kalıp, harekete geçilemeyecek kadar çok gürültü üretir.

**Hareketi denetleyin.** Pano, dosya kopyalama, çıkarılabilir bellek ve yüklemelerin hepsinin cihazda, eylem anında kuralı olmalıdır. Uzaktan oturum bu yollardan yalnızca biridir.

**Kaydı tutun.** Her olay neyin tespit edildiğini, kimin işin içinde olduğunu, nereye gittiğini ve ne olduğunu göstermelidir. Bir denetimi kanıta dönüştüren bu kayıttır.

## Değerlendiriciniz için hazırlanacak sorular

Bir sonraki değerlendirmeden önce birkaç basit sorunun cevabını hazır tutmaya değer.

- Kart sahibi veri ortamı dışında kart verisi gerçekte nerede ortaya çıkıyor?
- Uzaktan erişim sırasında kopyalamayı hangi teknik denetim durduruyor ve çalıştığını nereden biliyorsunuz?
- Kimin istisnası var ve gerekçesi nerede kayıtlı?
- Saklanan kart verisini olmaması gereken bir yerde en son ne zaman buldunuz ve sonra ne oldu?

Son sorunun cevabı yoksa bu nadiren iyi haberdir. Genellikle kimsenin bakmadığı anlamına gelir.

## Bir taramayla başlayın

En hızlı ilk adım uç noktalarda ve dosya sunucularında bir keşif taramasıdır. Beklediğiniz yerlerin dışında ne kadar kart verisi durduğunu gösterir ve size gerçek bir başlangıç listesi verir. Oradan, en önemli kanallar için kurallar koyun; önce izleme modunda, gördüğünüze güvendiğinizde engellemeye geçin.

Değerlendiriciniz niyet değil kanıt ister. Aynı kanıt, bir şey ters gittiği gün de işe yarar. [Korvia'nın PCI DSS çalışmalarını nasıl desteklediğini okuyun.](/mevzuat/)
"""),
    ('denetcinin-guvenebilecegi-kanit', 'Denetçinin güvenebileceği kanıt', 'Uyum', 3,
     'Bir denetçi ne olduğunu sorduğunda "sanırız" bir cevap değildir. Yararlı bir kayıt kendini açıklar ve sessizce değiştirilemez.',
     """Bir denetçi ne olduğunu sorduğunda "sanırız" bir cevap değildir. Denetçinin güvenebileceği kanıt neyin tespit edildiğini, neden eşleştiğini, kimin yaptığını, verinin nereye gittiğini ve sistemin ne yaptığını kaydeder. İmzalıdır; sonradan sessizce değiştirilemez ve kimin okuyabileceğine dair net kuralları olan bir yerde tutulur. Gerisi bir hikâyedir.

## Kayıtlar neden yetmez?

Kurumların çoğunun bol miktarda kaydı vardır. Çoğu zaman eksik olan bir cevaptır. Bir kayıt satırı bir dosyanın taşındığını söyler. Dosyanın ne olduğunu, neden önemsenmesi gerektiğini veya o sırada politikanın ne olduğunu nadiren söyler.

Bir denetim sorusu genellikle elinizdeki veriden daha dardır. Bu sözleşmeyi kim dışarı gönderdi, izni var mıydı? Bununla ilgili ne yaptınız? Kaydın eksiksiz olduğunu nereden biliyorsunuz? Kısmi kayıtları olan altı sistem buna cevap vermez. Birine bir haftalık iş ve yine de boşlukları olan bir sonuç çıkarır.

## Yararlı bir olay ne içerir?

İyi bir olay beş soruyu tek ekranda cevaplar.

- **Ne tespit edildi?** Dosya veya içerik ve etiketi.
- **Neden eşleşti?** Kural ve arkasındaki tespitçi: parmak izi, doğrulanmış kalıp, sınıflandırıcı.
- **Kim yaptı?** Kullanıcı ve cihaz.
- **Nereye gidiyordu?** Kanal ve hedef.
- **Ne oldu?** İzin verildi, uyarıldı, gerekçe istendi, kaydedildi veya engellendi.

İkinci soru en çok zaman kazandırandır. Bir karar kendini açıklayabiliyorsa analistin onu yeniden kurması, denetçinin de ona güvenmek zorunda kalması gerekmez. "Neden eşleşti" aynı zamanda yanlış alarmları düzeltilebilir kılar; çünkü fazla geniş olan kuralı görebilirsiniz.

## İmzalı, yani düzenlenemez

Bir denetim izi ancak kimse onu sonradan düzeltemiyorsa bir şeye değer. Buna yöneticiler de, iyi niyetli kişiler de dahildir. Her Korvia olayı imzalı kanıt bırakır; denetçiye gösterdiğiniz gerçekte olandır. Denetim kaydına erişim de kaydedilir; bu, denetçinin genellikle sorduğu bir sonraki soruyu cevaplar.

Bu konuşmayı değiştirir. Artık birinden ekibinize güvenmesini istemiyorsunuz. Güvene dayanmayan bir kayıt gösteriyorsunuz.

## Kanıt da hassas veri taşır

Burada bir tuzak var. Bir veri sızıntısının kanıtı sızan veriyi içerebilir; özensiz kanıt yönetimi ikinci bir ifşa yaratır. Birkaç kural bunu denetim altında tutar.

- **Kopyayı yalnızca bir kural istediğinde tutun.** Çoğu olay dosyanın kendisine ihtiyaç duymaz. Dosyayı yalnızca politikanın gerektirdiği yerde gölge kopya olarak alın.
- **Görmeyi incelemekten ayırın.** Rol tabanlı erişim, kimin neyi göreceğini kanal, eylem ve birime göre sınırlayabilir. İçeriğe erişimi olmayan bir inceleyen rolü, birinin yakalananı okumadan sürecin işlediğini kontrol etmesini sağlar.
- **Son kullanıcının gördüğünü maskeleyin.** Mesajının durdurulduğu söylenen kişinin eşleşen değeri yeniden görmesine gerek yoktur.
- **İçeriği SIEM'in dışında tutun.** Olay üst verisi SIEM'inize gidebilir; hassas içerik gitmemelidir.
- **Saklamayı bilerek belirleyin.** Korvia olayları varsayılan olarak 400 gün, yıllık karşılaştırmaya yetecek kadar, denetim kaydını ise 24 ay saklar. Kurumunuz bu süreleri kısaltabilir; neden bu süreleri seçtiğinizi yazmak işe yarar.

## Olaylardan vakaya

Bir denetçi nadiren tek bir olay ister. Bir olayın hikâyesini ister: ne zaman başladı, inceleyen ne buldu, kim neye karar verdi ve nasıl bitti. Olayları zaman çizelgesi ve notlarla bir vakada toplamak denetçiye bu hikâyeyi, kendi ekibinize de işi devretmenin bir yolunu verir.

Dönem karşılaştırmaları da yardımcı olur. Bir politika değiştikten sonra bir olay türünün azaldığını gösterebilmek, işlerin iyileştiğini söylemekten daha güçlüdür.

## Kendi kanıtınızı sınamak için sorular

Yakın tarihli bir olayı seçin ve şunları deneyin.

- Tek bir kişi, tek bir ekranda ne olduğunu ve neden eşleştiğini söyleyebiliyor mu?
- Biri o kaydı iz bırakmadan düzenleyebilir miydi?
- Arkasındaki içeriği kim okuyabiliyor ve bu bir yerde yazılı mı?
- Kayıt ne kadar süre saklanacak ve neden bu kadar?

Bunları cevaplamak bir hafta sürüyorsa denetçi bunu fark edecektir. Birkaç dakika sürüyorsa denetim çok daha kısa bir konuşma olur.

[İncelemenin kanıtı nasıl bir arada tuttuğunu okuyun.](/platform/inceleme/)
"""),
]

os.makedirs(os.path.join(KOK, 'blog'), exist_ok=True)
for slug, baslik, kategori, sure, ozet, govde in YAZILAR:
    fm = (
        '---\n'
        f"baslik: {baslik!r}\n".replace("'", "'") +
        f'kategori: {kategori}\n'
        f'tarih: 2026-11-07\n'
        f'sure: {sure}\n'
        f'ozet: >-\n  {ozet}\n'
        '---\n'
    )
    # YAML güvenli başlık
    fm = fm.replace(f"baslik: {baslik!r}", 'baslik: "' + baslik.replace('"', '\\"') + '"')
    with open(os.path.join(KOK, 'blog', f'{slug}.mdoc'), 'w', encoding='utf-8') as f:
        f.write(fm + govde.strip() + '\n')
