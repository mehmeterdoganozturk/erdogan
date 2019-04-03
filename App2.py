from SnmpConnections import SnmpProtocol
from QueryExecuter import querytrigger
from Backbone import Backbone
from Switch import Switch
from Client import Client
from Helper import Helper


soru1 = "Bina Seçiniz:\n\n"
dbclass = querytrigger()

sql = "SELECT backbone.id as id, backbone.ip as ip, bina.ad as binaad,bina.id as binaid FROM backbone INNER JOIN bina ON (backbone.binaid = bina.id) WHERE backbone.switchkontrol = 1 ORDER BY backbone.id ASC"
records = dbclass.simpleselectquery(sql)
binalist = []
if(len(records) > 0):
    for record in records:
        soru1 = soru1+str(record[0])+". "+record[2]+" - "+record[1]+"\n"
        binalist.append()
    soru1 = soru1+"\nçıkmak için q"
    print(soru1)

while True:
    binaid =input("Bina Seç")
    if(işlem=="q"):
        print("program sonlanıyor")
        break
    elif (binaid in)
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

