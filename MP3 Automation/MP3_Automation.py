import random
class MP3_Calar():

    with open("sarki_listesi", "r+", encoding="utf-8") as file:
        icerik = file.readlines()
        sarki_liste = []
        for ic in icerik:
            sarki_liste.append(f"{ic.strip()}, ")

    def __init__(self):
        self.calisma = True
        self.ses_seviyesi = 5
        self.ana_calan = self.icerik[2]

    def secim_ekrani(self):
        print('*'*50)
        secim = int(input(f'''MP3 çalara hosgeldiniz.
Şarkı listemiz = {self.sarki_liste}
Ses seviyesi = {self.ses_seviyesi}
Su an calan sarki = {self.ana_calan}

1) Sarki sec
2) Ses arttir
3) Ses azalt
4) Rastgele sarki sec
5) Sarki ekle
6) Sarki sil
7) Kapat

Seçiminizi giriniz: '''))

        if secim < 1 or secim > 7:
            secim = int(input("1-7 arasında belirtilen seceneklerden birini gir: "))
        return secim

    def ana_menu(self):
        secim = self.secim_ekrani()

        if secim == 1:
            self.sarki_sec()
        elif secim == 2:
            self.ses_arttir()
        elif secim == 3:
            self.ses_azalt()
        elif secim == 4:
            self.rastgele_sarki_sec()
        elif secim == 5:
            self.sarki_ekle()
        elif secim == 6:
            self.sarki_sil()
        else:
            self.calisma = False

    def sarki_sec(self):
        with open("sarki_listesi", "r", encoding="utf-8") as file:
            icerik2 = file.readlines()
            for index,value in enumerate(icerik2):
                print(f"{index}) {value}",end="")

        sarki_istegi = int(input("\nSecmek istediğiniz sarkının indexini giriniz: "))
        if sarki_istegi < 0 or sarki_istegi > index:
            sarki_istegi = int(input("Belirtilen seceneklerden birini gir: "))

        self.ana_calan = self.icerik[sarki_istegi]
        print("Yeni çalan şarkı: ",self.ana_calan)


    def ses_arttir(self):
        print(f"Şu anki ses seviyesi: {self.ses_seviyesi}")
        ses_arttirma_seviye = int(input("Sesi ne kadar arttırmak istiyorsunuz? "))
        while ses_arttirma_seviye < 0:
            ses_arttirma_seviye = int(input("Lütfen 0'dan büyük bir değer giriniz: "))
        while ses_arttirma_seviye > 10:
            ses_arttirma_seviye = int(input("Bu seviye kulağınıza zararlıdır. Lütfen 10'dan kücük bir değer giriniz: "))
        else:
            if self.ses_seviyesi == 10:
                pass
            else:
                self.ses_seviyesi += ses_arttirma_seviye
                print("Yeni ses seviyesi: ",self.ses_seviyesi)

    def ses_azalt(self):
        print(f"Şu anki ses seviyesi: {self.ses_seviyesi}")
        ses_azaltma_seviye = int(input("Sesi ne kadar azaltmak istiyorsunuz? "))
        while ses_azaltma_seviye < 0:
            ses_azaltma_seviye = int(input("Lütfen 0'dan büyük bir değer giriniz: "))
        while ses_azaltma_seviye > self.ses_seviyesi:
            ses_azaltma_seviye = int(input("Lütfen ses seviyesinden daha fazla bir değer girmeyiniz: "))
        else:
            self.ses_seviyesi -= ses_azaltma_seviye
            print("Yeni ses seviyesi: ", self.ses_seviyesi)

    def rastgele_sarki_sec(self):
        rastgele_sayi = random.randint(0,len(self.icerik))
        self.ana_calan = self.icerik[rastgele_sayi]
        print("Rastgele açılan şarkı: ",self.ana_calan)

    def sarki_ekle(self):
        eklemek_istedigin_sarki = input("Şarkı adı: ")
        with open("sarki_listesi", "a", encoding="utf-8") as dosya:
            dosya.write(f"\n{eklemek_istedigin_sarki}")

        print(f"İstediğiniz şarkı olan {eklemek_istedigin_sarki} şarkı listenize eklendi! Listeyi tekrardan görmek için sistemi kapatıp açınız.")

    def sarki_sil(self):
        with open("sarki_listesi","r",encoding="utf-8") as file:
            icerik3 = file.readlines()
            for index,value in enumerate(icerik3):
                print(f"{index}) {value}",end="")

        if len(icerik3) == 0:
            raise Exception("MP3'ünüzde şarkı bulunmadığından silme işlemi gerçekleştiremezsiniz!")

        silmek_istediginiz_sarki = int(input("\nSilmek istediğiniz şarkının indexi: "))

        while silmek_istediginiz_sarki < 0 or silmek_istediginiz_sarki > index:
            silmek_istediginiz_sarki = int(input(f"Lütfen 0-{index} aralığında bir değer giriniz."))

        icerik3.pop(silmek_istediginiz_sarki)

        with open("sarki_listesi","w",encoding="utf-8") as file:
            file.writelines(icerik3)

        print(f"Silmek istediğiniz şarkı başarıyla silindi. Listeyi tekrardan görmek için sistemi kapatıp açınız.")


sarkilar = MP3_Calar()


class Calisma_durumu():
    while sarkilar.calisma:
        sarkilar.ana_menu()