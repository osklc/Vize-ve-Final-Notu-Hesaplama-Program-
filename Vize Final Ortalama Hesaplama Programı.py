import os

print("****Vize Final Ortalama Hesaplama Programı****")

ogrenciadı = str(input("Lüften Adınızı Giriniz:"))


while True:
    vizeyuzdesi = int(input("Vize Yüzdesini Giriniz:"))
    finalyuzdesi = int(input("Final Yüzdesini Giriniz:"))

    if vizeyuzdesi+finalyuzdesi == 100:
        break
    else:
        print("Hatalı yüzde girişi yaptınız! Toplam 100 olmalı, tekrar deneyin.")

while True:
    vizepuani = int(input("Vize Puanınızı Giriniz:"))
    finalpuani = int(input("Final Puanınızı Giriniz:"))

    if 0<= vizepuani <= 100 and 0 <= finalpuani <= 100:
        break
    else:
        print("Hatalı puan girişi yaptınız! 0-100 arasında değer girin, tekrar deneyin.")

toplampuan = vizepuani*vizeyuzdesi/100 + finalpuani*finalyuzdesi/100

if 85<=toplampuan<=100:
    harfnotu = "AA"
    print(f"Tebrikler, {toplampuan:.2f} puan ile {harfnotu} aldınız.")
elif 70<=toplampuan<85:
    harfnotu = "BA"
    print(f"Tebrikler, {toplampuan:.2f} puan ile {harfnotu} aldınız.")
elif 60<=toplampuan<70:
    harfnotu = "BB"
    print(f"Tebrikler, {toplampuan:.2f} puan ile {harfnotu} aldınız.")
elif 50<=toplampuan<60:
    harfnotu = "CB"
    print(f"Tebrikler, {toplampuan:.2f} puan ile {harfnotu} aldınız.")
elif 40<=toplampuan<50:
    harfnotu = "CC"
    print(f"Tebrikler, {toplampuan:.2f} puan ile {harfnotu} aldınız.")
elif 0<=toplampuan<40:
    harfnotu = "FF"
    print(f"Tebrikler, {toplampuan:.2f} puan ile {harfnotu} aldınız.")
else:
    print("Hatalı toplam puan hesaplandı! Lütfen puanları kontrol edin.")
    exit()


klasor = os.path.dirname(os.path.abspath(__file__))
dosya_adi = "Not_Ortalamaları_Listesi.txt"
dosya_yolu = os.path.join(klasor, dosya_adi)

with open(dosya_yolu, "a", encoding="utf-8") as dosya:
    dosya.write(f"Ad: {ogrenciadı} | Vize: {vizepuani} ({vizeyuzdesi}%) | Final: {finalpuani} ({finalyuzdesi}%) | Toplam: {toplampuan:.2f} | Harf Notu: {harfnotu}\n")