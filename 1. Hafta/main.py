print("""

1) Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

a => Sayı veri tipleri: Sayı veri tipleri tam sayılar (int) ve ondalıklı sayılar (float) sayılardır.

a.1) Integer veri tipi: Integer pozitif ve negatif tam sayılardır. Bir örnek yapalım:

sayi = 5

Buradaki sayi değişkeninin değeri 5 tir. 5 Tam sayı olduğu için Integer bir değerdir.

a.2) Float veri tipi: Float ondalıklı sayılardır. Bir örnek yapalım:

sayi2 = 3.14

Buradaki sayi2 değişkeninin değeri 3.14 tür. 3.14 Ondalıklı sayı olduğu için Float bir değerdir.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

b => Metin dizileri (Stringler): String veri tipi gerçek hayatta kullandığımız yazıların aynısıdır.
Bu veri tipi her biri bir karakter olan bir dizidir.

Tek tırnak veya çift tırnak ile String veri tipini oluşturabiliriz. Örnekler:

isim = "Hasancan Yıldırım"   => # Hasancan Yıldırım
isim2 = "Hasancan Yıldırım"  => # Hasancan Yıldırım 

Burada isim ve isim2 Değişkenleri String veri tipidir. Her iki değişkende bize aynı sonucu verecektir.

Not: String veri tipleri değiştirilemezler.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

c => Boolean veri tipi: Sadece iki değerden oluşur: True (doğru) veya False (yanlış).
Bu veri tipi, karar verme yapısında ve mantıksal işlemlerde kullanılır.

print(x > 5 and y < 10)  =>  # True
print(x < 5 or y < 10)   =>  # False
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

d => Listeler (Lists) veri tipi: Python'da listeler, birden fazla veriyi depolamak için kullanılır ve farklı veri tiplerini içerebilir.
Liste elemanları, virgülle ayrılarak belirtilir ve köşeli parantezlerle tanımlanır. Örnek:

liste = ["Python","Java","C++"]  => # ['Python', 'Java', 'C++']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

e => Demetler (Tuples) veri tipi: Demetler de birden fazla veriyi depolamak için kullanılır ancak demetler değiştirilemez (immutable) veri tipleridir.
Demetler, virgülle ayrılarak belirtilir ve normal parantezlerle tanımlanır. Örnek:

sehirler = ("istanbul", "ankara", "izmir", "antalya")  => # ('istanbul', 'ankara', 'izmir', 'antalya')
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f => Sözlükler (Dictionaries): Sözlükler, bir anahtar-değer kümesidir ve verileri depolamak için kullanılır.
Sözlükler süslü parantez ile tanımlanırlar ve anahtarlar benzersiz olmalıdır. Örnek:

sözlük = {"ad": "Hasancan", "soyad": "Yıldırım", "yaş": 23, "şehir": "İstanbul"}  => # {'ad': 'Hasancan', 'soyad': 'Yıldırım', 'yaş': 23, 'şehir': 'İstanbul'}

**************************************************************************************************************************************************************************

2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
String veri tipleri:

- kurs_adi = "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"

- Sayı veri tipleri:

tamamlandi = %75

- Liste veri tipleri:

Kurslarım = ["(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium","(2022) Yazılım Geliştirici Yetiştirme Kampı - JAVA"]

*************************************************************************************************************************************************************************

3) Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

Sayfanın sağ üst köşesindeki Kurslarım, Tüm kurslar, Kariyer ve Sık Sorulan Sorular birer şart bloğudur.
Biz buralara tıkladığımızda yeni pencere açılacaktır

Örnek:

Yazılım Geliştirici Yetiştirme Kampı (JAVA & REACT) kursuna üye olmak için Programa dahil ol butonuna tıklamamız gerekir.

cevap = input("Kursa dahil olmak ister misin? 'Evet'/ 'Hayır' ")
while True:
    if(cevap == "Evet"):
        print("Kursa dahil olundu")
        break
    else:
        print("Kursa henüz dahil değilsiniz.")
        break

Bu kod sizden kursa dahil olmak isteyip istemediğiniz verisini istiyor. Eğer cevabınız Evet olursa bu kursa dahil olabileceksiniz.
Sadece 'Evet' cevabı ile kursa dahil olabilirsiniz. Cevap Evet ise döngü break ile bitiyor.
Evet harici bir cevap verirseniz döngü tekrar sonlanıyor ve kursa henüz dahil olmamış oluyorsunuz.

""")

