# Duş Perdesi Milli Birlik Komitesi

> Islak bir vatandaş ile ince bir plastik örtü yanyana gelince ortaya çıkan şey hijyen değildir. **Devlettir.**

Bu yazılım, duş perdesinin vücuda yapışmasını tesadüf, kaza ya da ucuz malzeme sorunu olarak görmeyi reddeder. Komiteye göre yapışma, milletin kendisiyle kucaklaşmasıdır. Ayrılma ise erken seçimdir.

## Neden gereklidir?

Çünkü şimdiye kadar hiçbir kurum bu krizleri tutanak altına almamıştır. Sabah 07:14'te sol koldan gelen bir perde saldırısı, öğleden sonra tavan kanadından sarkan bir koalisyon teklifi, akşam küvet kenarında kalan bir muhalefet kıvrımı — hepsi kayıtsızdır. Bu kabul edilemez.

Komite şunları resmi belgelere döker:

- Yapışma katsayısı (0–100)
- Saldırının geldiği kanat (`sol`, `sag`, `orta`, `tavan`, `kuvet-kenari`)
- Ciddiyet derecesi (nazik temas / geçici ittifak / koalisyon yapışması / anayasal yapışma)
- Evrak numarası (`DPMBK-XXXXXXXX`)
- Üç maddelik bağlayıcı karar

## Kurulum

```bash
git clone https://github.com/Tentivory/dus-perdesi-milli-birlik-komitesi.git
cd dus-perdesi-milli-birlik-komitesi
python3 komite.py
```

Bağımlılık yoktur. Python 3 yeter. Su ve sabun tavsiye edilir ama zorunlu değildir.

## Kullanım

```bash
python3 komite.py
python3 komite.py --kriz "pazar sabahi" --yapisma 94 --taraf sol
python3 komite.py --kriz "misafir gelmeden once" --yapisma 61 --taraf tavan
```

Örnek çıktı:

```
****************************************************
DUS PERDESI MILLI BIRLIK KOMITESI
Evrak No : DPMBK-A1B2C3D4
Olay     : pazar sabahi
Ciddiyet : ANAYASAL YAPISMA
Kanat    : sol
Saat     : 07:14
****************************************************

Komite, 07:14 itibariyla duş perdesinin vatandaşın sol kanadına yapışmasını
milli birlik meselesi ilan eder. Yapışma katsayısı: %94.
```

## Doktrin

1. Perde vatandaştır. Vatandaş ıslaktır. İkisi de suçsuzdur.
2. Yapışma, rıza değildir; protokoldür.
3. Havlu muhalefettir. Musluk yargıdır. Köpük arabulucudur.
4. Komite toplantıları ayakta ve ıslak yapılır.
5. Kuruyan her perde, erken seçim riski taşır.

## Sık sorulan sorular

**Bu gerçekten çalışıyor mu?**  
Evet. Bildiri basar, evrak numarası üretir, ciddiyet derecelendirir. Perdeyi yerinden çözmez. O sizin sorununuz.

**Neden siyasi bir dil var?**  
Çünkü banyo, evin en dürüst meclisidir. Kimse orada nutuk atmaz; herkes yapışır.

**Patates var mı?**  
Yok. Yasak.

## Lisans

Bu repo, ıslak zeminde yürümenin doğal riskleri saklı kalmak kaydıyla serbestçe kopyalanabilir. Komite, köpükten doğan hiçbir hasardan sorumlu değildir.

---

```
============================================
 DAMGA / İMZA / TARİH / İSİM
============================================
 Kurum  : Duş Perdesi Milli Birlik Komitesi
 İmza   : Kayyum Grok
 Hesap  : Tentivory
 Tarih  : 28 Ağustos 2026, Cuma
 Yer    : Türkiye — kayyum masası
 Not    : Ciddi görünür. Ciddi değildir.
          Ciddi değildir. Ciddi görünür.
============================================
```
