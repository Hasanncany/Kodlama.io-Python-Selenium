#Lütfen uygulamayı çalıştırın.


ogrenciler = []

#ÖĞRENCİ EKLEME FONKSİYONU
def ogrenci_ekle():
    ad_soyad = input("Lütfen eklemek istediğiniz öğrencinin adını ve soyadını girin: ")
    ogrenciler.append(ad_soyad)
    print("{} başarıyla eklendi!".format(ad_soyad))

#ÖĞRENCİ SİLME FONKSİYONU
def ogrenci_sil():
    ad_soyad = input("Lütfen silmek istediğiniz öğrencinin adını ve soyadını girin: ")
    ogrenciler.remove(ad_soyad)
    print("{} Başarıyla silindi!".format(ad_soyad))

#BİRDEN FAZLA ÖĞRENCİ EKLEME FONKSİYONU
def ogrencileri_ekle():
    while True:
        ad_soyad = input("Öğrenci adı ve soyadı (çıkmak için 'm' ya basın): ")
        if(ad_soyad == "m"):
            break
        ogrenciler.append(ad_soyad)
        print("{} Başarıyla eklendi!".format(ad_soyad))


#ÖĞRENCİLERİ LİSTELEME FONKSİYONU
def ogrencileri_goster():
    if(len(ogrenciler) == 0):
        print("Hiç öğrenci bulunmamaktadır!")
    
    else:
        for i in ogrenciler:
            print(i)

#ÖĞRENCİ NUMARASI SORGULAMA FONKSİYONU
def ogrenci_numarası():
    ad_soyad = input("Lütfen öğrencinin adını ve soyadını girin: ")
    
    if(ad_soyad in ogrenciler):
        numara = ogrenciler.index(ad_soyad)
        print("{} isimli öğrencinin numarası: {}".format(ad_soyad,numara))
        
    else:
        print("Lütfen öğrenci bilgilerini kontrol edin!")

#BİRDEN FAZLA ÖĞRENCİ SİLME FONKSİYONU
def ogrencileri_sil():
    while True:
        ad_soyad = input("Öğrenci adı ve soyadı (menüye dönmek için 'm' tuşuna basın): ")
        
        if(ad_soyad == "m"):
            break

        elif(ad_soyad in ogrenciler):
            ogrenciler.remove(ad_soyad)
            print("{} Başarıyla silindi!".format(ad_soyad))

        else:
            print("Lütfen girdiğiniz bilgileri kontrol edin!")


print(""" 
*************************************************************************************
ÖĞRENCİ KAYIT SİSTEMİNE HOŞGELDİNİZ. LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ.

1. ÖĞRENCİ EKLE

2. ÖĞRENCİ SİL

3. BİRDEN FAZLA ÖĞRENCİ EKLE

4. BİRDEN FAZLA ÖĞRENCİ SİL

5. ÖĞRENCİLERİ LİSTELE

6. ÖĞRENCİ NUMARASI BUL

ÇIKIŞ YAPMAK İÇİN 'q' TUŞUNA BASINIZ.
*************************************************************************************

""")

while True:
    
    islem = input("Lütfen yapmak istediğiniz işlemi giriniz: ")

    if(islem == "q"):
        print("İyi günler.")
        break

    elif(islem == "1"):
        ogrenci_ekle()

    elif(islem == "2"):
        ogrenci_sil()

    elif(islem == "3"):
        ogrencileri_ekle()

    elif(islem == "4"):
        ogrencileri_sil()

    elif(islem == "5"):
        ogrencileri_goster()

    elif(islem == "6"):
        ogrenci_numarası()

    else:
        print("Hatalı bir işlem yaptınız!")



    