import pyautogui as auto
import time

print("Otomatik Mesaj Gönderici Uygulama")
mesaj = input("Göndermek İstediğiniz Mesajı Giriniz :")
tekrar = int(input("Kaç Adet Göndermek İstiyorsunuz :"))
mesaj_bekleme = int(input("Kaç Saniye Aralıkla Göndermek İstiyorsunuz Örn: 3 : "))


time.sleep(6)

for i in range(tekrar):
    auto.write(mesaj)
    auto.press("enter")
    print(f"{i+1}. mesaj gönderildi")
    time.sleep(mesaj_bekleme)