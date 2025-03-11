import wget
from time import sleep
from os import system

def soru():
    soru1 = input("Bilgisayarınız hangi bit değerine sahip 32/64: ")
    system("cls")
    if soru1 == ("64"):
        wget.download("https://github.com/git-for-windows/git/releases/download/v2.47.0.windows.2/Git-2.47.0.2-64-bit.exe")
        system("cls")
    elif soru1 == ("32"):
        wget.download("https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/Git-2.47.1-32-bit.exe")
        system("")
    else:
        print("Lütfen Bit Değerinizi *32* veya *64* olarak giriniz..")
        sleep(5)
        system("cls")
        soru()
soru()
system("cls")
print(("Lütden Bekleyiniz Dosya Hazırlanıylor.."))
sleep(5)
system("start Git-2.47.0.2-64-bit.exe")
os.remove(kurulum.bat)
cls