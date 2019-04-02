 from kutuphane import *
print("""
******************************
işlemler:

1. Kitap göster

2. kitap sorgula

3. kitap ekle

4.  kitap sil

5. baskı yükselt

çıkmak için q

******************************
""")

Kutuphane=kutuphane()
while True:
    işlem =input("işlem seç")
    if(işlem=="q"):
        print("program sonlanıyor")
        break

    elif (işlem == "1"):
        Kutuphane.kitapları_goster()
    elif (işlem == "2"):
        isim=input("hangi kitap?")
        print("kitap soruluyo")
        time.sleep(2)
        Kutuphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim=input("kitap ismi:")
        yazar=input("yazar:")
        yayınevi=input("yayınevi:")
        tür=input("türü:")
        baskı=int(input("baskı:"))

        yeni_kitap=kitap(isim,yazar,yayınevi,tür,baskı)
        print("kitap ekleniyor")
        time.sleep(2)
        Kutuphane.kitap_ekle(yeni_kitap)
        print("kitep eklendi")


    elif (işlem == "4"):
        isim= input("hangi kitap silinecek")

        cevap=input("emin misin? E/H")
        if (cevap=="E"):
            print("kitap siliniyor")
            time.sleep(2)
            Kutuphane.kitap_sil(isim)
            print("kitap silindi")


    elif (işlem == "5"):
        isim=input("hangi kitap baskısı yükselcek")
        print("baskı yükseltiliyor")
        time.sleep(2)
        Kutuphane.baskı_yukselt(isim)
        print("yükseltildi")
    else:
        print("geçersiz")

