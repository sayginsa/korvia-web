"""İçerik üreticisi için ortak yardımcılar. Çıktı: Keystatic'in okuduğu YAML dosyaları."""
import os
import yaml

KOK = os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'content')


class _D(yaml.SafeDumper):
    pass


def _str(d, s):
    if '\n' in s:
        return d.represent_scalar('tag:yaml.org,2002:str', s, style='|')
    return d.represent_scalar('tag:yaml.org,2002:str', s)


_D.add_representer(str, _str)


def yaz(yol, veri):
    tam = os.path.join(KOK, yol)
    os.makedirs(os.path.dirname(tam), exist_ok=True)
    with open(tam, 'w', encoding='utf-8') as f:
        yaml.dump(veri, f, Dumper=_D, allow_unicode=True, sort_keys=False, width=10000)


def _l(etiket='', url=''):
    return {'etiket': etiket, 'url': url}


def B(_tur, **v):
    return {'discriminant': _tur, 'value': v}


def senaryo(baslik, veri, kullanici, hedef, politika, karar, kararNotu):
    return B('senaryo', baslik=baslik, veri=veri, kullanici=kullanici, hedef=hedef,
             politika=politika, karar=karar, kararNotu=kararNotu)


def metin(baslik, govde, eyebrow=''):
    return B('metin', eyebrow=eyebrow, baslik=baslik, govde=govde.strip())


def _liste(ogeler):
    return [{'baslik': b, 'metin': m} for b, m in ogeler]


def adimlar(baslik, ogeler):
    return B('adimlar', baslik=baslik, ogeler=_liste(ogeler))


def kartlar(baslik, ogeler, eyebrow='', aciklama=''):
    return B('kartlar', eyebrow=eyebrow, baslik=baslik, aciklama=aciklama, ogeler=_liste(ogeler))


def tablo(baslik, sutunlar, satirlar, aciklama=''):
    return B('tablo', baslik=baslik, aciklama=aciklama, sutunlar=list(sutunlar),
             satirlar=[{'hucreler': list(s)} for s in satirlar])


def karar(baslik, aciklama, izle, uyar, kaydet, engelle):
    return B('karar', baslik=baslik, aciklama=aciklama, izle=izle, uyar=uyar, kaydet=kaydet, engelle=engelle)


def maskeleme(baslik, once, sonra, not_=''):
    return B('maskeleme', baslik=baslik, once=once, sonra=sonra, **{'not': not_})


def notkutu(baslik, metin_, etiket='', url=''):
    return B('not', baslik=baslik, metin=metin_, link=_l(etiket, url))


def sss(baslik, ogeler):
    return B('sss', baslik=baslik, ogeler=[{'soru': s, 'cevap': c} for s, c in ogeler])


MEVZUAT = {
    'kvkk': ('KVKK', '6698 sayılı Kanun: veri güvenliğine ilişkin yükümlülükler (md. 12), veri envanteri ve ihlal bildirimi.'),
    'bddk': ('BDDK Bilgi Sistemleri Yönetmeliği', 'Bankalarda bilgi güvenliği, erişim yönetimi ve iz kayıtları.'),
    'spk': ('SPK Bilgi Sistemleri Yönetimi Tebliği', 'VII-128.9: sermaye piyasası kurumlarında bilgi güvenliği ve iz kayıtları.'),
    'cbigr': ('Bilgi ve İletişim Güvenliği Rehberi', 'Cumhurbaşkanlığı rehberi: kritik verinin sınıflandırılması, korunması ve kayıt yönetimi.'),
    'pci': ('PCI DSS', 'Kart verisinin saklanması ve hareket hâlinde korunması.'),
    'iso': ('ISO/IEC 27001', 'Sınıflandırma, etiketleme ve bilgi aktarımı kontrolleri.'),
    'saglik': ('Kişisel Sağlık Verileri Yönetmeliği', 'Özel nitelikli sağlık verisine erişim, aktarım ve kayıt.'),
    'gdpr': ('GDPR', 'AB\'deki kişilerin verisini işleyen kurumlar için işleme güvenliği ve kayıtlar.'),
}


def mevzuat(*anahtarlar, baslik='Hangi mevzuata dokunur?'):
    return B('mevzuat', baslik=baslik, ogeler=[{'baslik': MEVZUAT[a][0], 'metin': MEVZUAT[a][1]} for a in anahtarlar])


def ilgili(*slugler, baslik='İlgili sayfalar'):
    return B('ilgili', baslik=baslik, sayfalar=list(slugler))


def form(tur, baslik, aciklama, secenekBasligi='', secenekler=(), mesajEtiketi='Mesajınız', gonderEtiketi='Gönderin'):
    return B('form', tur=tur, baslik=baslik, aciklama=aciklama, secenekBasligi=secenekBasligi,
             secenekler=list(secenekler), mesajEtiketi=mesajEtiketi, gonderEtiketi=gonderEtiketi)


def sayfa(slug, kimlik, yol, bolum, sira, menuAciklama, eyebrow, baslik, ozet, bloklar,
          cta=('Demo planlayın', '/demo/'), seoBaslik=None, seoAciklama=None):
    yaz(f'sayfalar/{slug}.yaml', {
        'kimlik': kimlik,
        'yol': yol,
        'bolum': bolum,
        'sira': sira,
        'menuAciklama': menuAciklama,
        'seoBaslik': seoBaslik or f'{kimlik} | Korvia',
        'seoAciklama': seoAciklama or ozet.split('\n')[0][:158],
        'eyebrow': eyebrow,
        'baslik': baslik,
        'ozet': ozet.strip(),
        'cta': _l(*cta) if cta else _l(),
        'bloklar': bloklar,
    })


# Tüm sayfalarda tekrar eden kurulum cümlesi
KURULUM_ACIKLAMA = 'Kurum içi, özel bulut, internetten yalıtılmış ağ veya yönetilen hizmet.'
