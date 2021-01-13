import requests
import datetime
from time import sleep

dolar=250
bakiye=1800
sn=open("sonislemeler.txt","w")
sn.close()
while(True):
    a=input("*****\nPara çekmek için 1'e\nYatırmak için 2'ye\nSon işlemler için 3'e\nDolar değerlerini öğrenmek için 4'e\nDolar Almak İçin 5'e\nDolar satmak için 6'ya basınız\nBakiyenizi Görmek için 7'ye basınız\nÇıkmak için 9'a basınız\n******\nSeçim:")
    if(a=="1"):
        print("Bakiyeniz:",bakiye)
        miktar=float(input("Çekmek istediğiniz Miktarı giriniz:"))
        if(float(bakiye)<float(miktar)):
             print("Bilgilendirme","Bakiyeniz: "+ str(bakiye) + " Bu miktardan fazlasını çekemezsiniz")
        else:
            bakiye=bakiye-miktar
            print("Bilgilendirme:\n","çektiğiniz para:"+str(miktar)+"\nKalan bakiyeniz:"+str(bakiye))
            islem=("{} TL Para çekildi Tarih:{}\n".format(miktar,datetime.datetime.now().strftime('%Y-%m-%d')))


            with open("sonislemeler.txt","a",encoding="UTF-8") as file:
                file.write(islem)

        sleep(2)
        print("\n")


    if(a=="2"):
        miktar=input("Yatırmak istediğiniz Miktarı giriniz")
        bakiye = int(bakiye) + int(miktar)
        print("Toplam bakiyeniz: ", str(bakiye))
        islem=" ".join([str(miktar),"TL hesabınıza yatırıldı",str(datetime.datetime.now().strftime("%Y-%m-%d")),"\n"])

        with open("sonislemeler.txt", "a", encoding="UTF-8") as file:
            file.write(islem)
        sleep(2)
        print("\n")


    if (a=="3"):

        with open("sonislemeler.txt", "r+", encoding="UTF-8") as file:
            a=file.readlines()
            for i in a:
                print(i)
        sleep(2)
        print("\n")

    if(a=="4"):
        response = requests.get("https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/usd")
        doviz = response.json()

        print("Bilgilendirme","Alış:"+doviz['BanknoteBuying'] +"\nSatış:"+doviz['BanknoteSelling']+ "\nBakiyeniz:"+str(bakiye))

        sleep(2)
        print("\n")

    if(a=="5"):
        response = requests.get("https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/usd")
        doviz = response.json()

        alinabilecek_miktar=float(bakiye)/float(doviz['BanknoteBuying'])
        almak_istenilen_miktar=input("Alabileceğiniz dolar:"+str(round(alinabilecek_miktar,2))+" Almak istediğiniz miktarı giriniz:")
        while(float(almak_istenilen_miktar)>alinabilecek_miktar):
            almak_istenilen_miktar = input("Alabilecek dolar: " + str(round(alinabilecek_miktar,2)) + "'dan fazlasını girmeyiniz. Tekrar miktar giriniz:")
        dolar=float(dolar)-float(almak_istenilen_miktar)
        bakiye = float(bakiye) - round(float(almak_istenilen_miktar) * float(doviz['BanknoteBuying']), 2)
        islem=" ".join([str(almak_istenilen_miktar),"Dolar alındı",  str(datetime.datetime.now().strftime("%Y-%m-%d"))])


        print("Kalan dolar miktarınız:", dolar)
        print("bakiyeniz", bakiye)
        with open("sonislemeler.txt", "r+", encoding="UTF-8") as file:
            file.write(islem)

        sleep(2)
        print("\n")


    if(a=="6"):
        response = requests.get("https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/usd")
        doviz = response.json()

        satilacak_milktar = input("Satabileceğiniz döviz miktarı: {}  Satmak istediğiniz miktarı giriniz:".format(dolar))
        dolar = float(dolar) - float(satilacak_milktar)
        bakiye = float(bakiye) + round(float(satilacak_milktar) * float(doviz['BanknoteSelling']), 2)
        islem=" ".join([str(satilacak_milktar),"Dolar sattınız",  str(datetime.datetime.now().strftime("%Y-%m-%d"))])


        print("Toplam dolar miktarınız:", dolar)
        print("bakiyeniz", bakiye)


        with open("sonislemeler.txt", "r+", encoding="UTF-8") as file:
            file.write(islem)

        sleep(2)
        print("\n")
    if(a=="7"):
        print("Bakiye:",bakiye)
        print("Dolar Miktarınız:",dolar)

        sleep(2)
        print("\n")

    if(a=="9"):
        break


