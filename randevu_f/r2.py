import datetime

class Ders:
    def __init__(self, ders_adi, ogretmen, ogrenci, tarih, sure):
        self.ders_adi = ders_adi
        self.ogretmen = ogretmen
        self.ogrenci = ogrenci
        self.tarih = tarih
        self.sure = sure

    def __str__(self):
        return f"Ders: {self.ders_adi}, Öğretmen: {self.ogretmen}, Öğrenci: {self.ogrenci}, Tarih: {self.tarih}, Süre: {self.sure} saat"

class OzelDersTakip:
    def __init__(self):
        self.dersler = []

    def ders_ekle(self, ders):
        self.dersler.append(ders)
        print(f"{ders} eklendi.")

    def ders_sil(self, ders_adi):
        for ders in self.dersler:
            if ders.ders_adi == ders_adi:
                self.dersler.remove(ders)
                print(f"{ders} silindi.")
                return
        print(f"{ders_adi} bulunamadı.")

    def dersleri_listele(self):
        if not self.dersler:
            print("Kayıtlı ders bulunmamaktadır.")
        for ders in self.dersler:
            print(ders)

    def ders_bul(self, ders_adi):
        for ders in self.dersler:
            if ders.ders_adi == ders_adi:
                print(ders)
                return
        print(f"{ders_adi} bulunamadı.")

# Kullanıcıdan bilgi alarak ders ekleme
def ders_ekle_kullanici():
    ders_adi = input("Ders Adı: ")
    ogretmen = input("Öğretmen: ")
    ogrenci = input("Öğrenci: ")
    tarih = input("Tarih (YYYY-MM-DD): ")
    sure = int(input("Süre (saat): "))

    tarih = datetime.datetime.strptime(tarih, "%Y:%m-%d")
    ders = Ders(ders_adi, ogretmen, ogrenci, tarih, sure)
    return ders

if __name__ == "__main__":
    takip_programi = OzelDersTakip()

    while True:
        print("\n1. Ders Ekle")
        print("2. Ders Sil")
        print("3. Dersleri Listele")
        print("4. Ders Bul")
        print("5. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            ders = ders_ekle_kullanici()
            takip_programi.ders_ekle(ders)
        elif secim == "2":
            ders_adi = input("Silinecek Ders Adı: ")
            takip_programi.ders_sil(ders_adi)
        elif secim == "3":
            takip_programi.dersleri_listele()
        elif secim == "4":
            ders_adi = input("Bulunacak Ders Adı: ")
            takip_programi.ders_bul(ders_adi)
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")
