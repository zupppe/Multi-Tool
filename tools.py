import os
import time
import colorama
from colorama import Fore, Back, Style

# CMD FONKSIYON
os.system("cls||clear")

# KLASÖRLER / FONKSİYONLAR
termux31 = lambda: os.system("cls||clear")
clear = lambda: os.system("cls")
sms_klasor = "erenbomb"
rat_klasor = "empyrean"
ipsorgu_klasor = "ipsorgu"
phishing_klasor = "PyPhisher"

# KOD
cihaz_soru = input(Fore.LIGHTBLUE_EX + """                          






                                Hangi Cihazı Kullanıyorsunuz? {}android{}/{}win{}/{}linux :
                                
                                
                                
                                -----> """.format(Fore.GREEN, Fore.BLUE, Fore.RED, Fore.BLUE, Fore.LIGHTMAGENTA_EX, Fore.RESET)).lower()
if cihaz_soru == ("win"):
    clear()
    os.system("title Multi Tool   by @zupppe")
    os.system("@echo off")
    print(Fore.LIGHTBLUE_EX + """
 __    __     __  __     __         ______   __        ______   ______     ______     __        
/\ "-./  \   /\ \/\ \   /\ \       /\__  _\ /\ \      /\__  _\ /\  __ \   /\  __ \   /\ \       
\ \ \-./\ \  \ \ \_\ \  \ \ \____  \/_/\ \/ \ \ \     \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  
 \ \_\ \ \_\  \ \_____\  \ \_____\    \ \_\  \ \_\       \ \_\  \ \_____\  \ \_____\  \ \_____\ 
  \/_/  \/_/   \/_____/   \/_____/     \/_/   \/_/        \/_/   \/_____/   \/_____/   \/_____/


                                                                            {}by {}@zupppe

{}[{}1{}] {}İp Logger
{}[{}2{}] {}Sms Bomber
{}[{}3{}] {}Remote Acces Tool (Rat)
{}[{}4{}] {}İp Sorgu {}# BAKIMDA #KODLANMA AŞAMASINDA
{}[{}5{}] {}Turkish Mernis Panel
                                                                                  
{}
""".format(Fore.BLUE, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.RESET))
    anamenu_soru = input("{}Hangi Toola Giriş Yapmak İstersiniz: {}".format(Fore.BLUE, Fore.RESET))
    if anamenu_soru == ("1"):
        clear()
        os.system("start https://grabify.link")
        clear()
        os.system("py multitool.py")
    if anamenu_soru == ("2"):
        clear()
        sms_soru = input("{}Önceden Sms Bomber Kurdun Mu? {}y{}/{}n{}: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.RESET)).lower()
        if sms_soru == ("n"):
            clear()
            print("""




{}          
  ____                        _             __   ___   _ _    _            _                  
 |  _ \  ___  ___ _   _  __ _| | __ _ _ __  \ \ / (_) (_) | _| | ___ _ __ (_)_   _  ___  _ __ 
 | | | |/ _ \/ __| | | |/ _` | |/ _` | '__|  \ V /| | | | |/ / |/ _ \ '_ \| | | | |/ _ \| '__|
 | |_| | (_) \__ \ |_| | (_| | | (_| | |      | | | |_| |   <| |  __/ | | | | |_| | (_) | |   
 |____/ \___/|___/\__, |\__,_|_|\__,_|_|      |_|  \__,_|_|\_\_|\___|_| |_|_|\__, |\___/|_|   
                  |___/                                                      |___/     
{}       
    """.format(Fore.LIGHTBLUE_EX, Fore.RESET))
            time.sleep(2)
            clear()

            os.system("git clone https://github.com/vHzEren/erenbomb.git")
            os.chdir(sms_klasor)
            os.system("pip install -r requirements.txt")
            os.system("py erenbomb.py")
        if sms_soru == ("y"):
            clear()
            os.chdir(sms_klasor)
            os.system("py erenbomb.py")
        if sms_soru != ("y","n"):
            clear()
            print(Fore.LIGHTRED_EX +"Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
            time.sleep(3)
            os.system("py multitool.py")
    if anamenu_soru == ("3"):
        
        clear()
        rat_sorusu = input("{}Önceden Rat Kurdun mu? {}y{}/{}n{}: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.RESET)).lower()
        if rat_sorusu == ("n"):
            clear()
            os.system("git clone https://github.com/addi00000/empyrean.git")
            os.chdir(rat_klasor)
            os.system("pip install -r requirements.txt")
            os.system("start install_python.bat")
            os.system("start build.bat")
            os.chdir("..")
            os.system("cls")
            os.system("py multitool.py")
        if rat_sorusu == ("y"):
            clear()
            os.chdir(rat_klasor)
            os.system("start build.bat")
            os.chdir("..")
            os.system("cls")
            os.system("py multitool.py")
        if rat_sorusu != ("y","n"):
            clear()
            print(Fore.LIGHTRED_EX + "Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
            time.sleep(3)
            os.system("py multitool.py")
    if anamenu_soru == ("4"):
        clear()
        ipsorusu = input("{}Önceden İp Sorgu Kurdun Mu? {}y{}/{}n{}: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.RESET)).lower()
        if ipsorusu == ("n"):
            clear()
            print("""
{}          
  ____                        _             __   ___   _ _    _            _                  
 |  _ \  ___  ___ _   _  __ _| | __ _ _ __  \ \ / (_) (_) | _| | ___ _ __ (_)_   _  ___  _ __ 
 | | | |/ _ \/ __| | | |/ _` | |/ _` | '__|  \ V /| | | | |/ / |/ _ \ '_ \| | | | |/ _ \| '__|
 | |_| | (_) \__ \ |_| | (_| | | (_| | |      | | | |_| |   <| |  __/ | | | | |_| | (_) | |   
 |____/ \___/|___/\__, |\__,_|_|\__,_|_|      |_|  \__,_|_|\_\_|\___|_| |_|_|\__, |\___/|_|   
                  |___/                                                      |___/     
{}       
    """.format(Fore.LIGHTBLUE_EX, Fore.RESET))
            time.sleep(2)
            clear()
            os.system("git clone https://github.com/vHzEren/ipsorgu.git")
            os.chdir(ipsorgu_klasor)
            os.system("pip install requests")
            clear()
            os.system("py ipsorgu.py")
        if ipsorusu == ("y"):
            clear()
            os.chdir(ipsorgu_klasor)
            os.system("py ipsorgu.py")
        if ipsorusu != ("y","n"):
            clear()
            print(Fore.LIGHTRED_EX + "Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
            time.sleep(3)
            os.system("py multitool.py")
    if anamenu_soru == ("5"):
        clear()
        print(Fore.BLUE + "Panel Sitesine Yönlendiriliyorsunuz #VPN AÇMAYI UNUTMAYIN!")
        time.sleep(5)    
        os.system("start https://nopanel.run")
        os.system("py multitool.py")
if cihaz_soru == ("android"):
    termux31()
    print("""
{}
  __  __ _   _ _   _____ ___   _____ ___   ___  _     
 |  \/  | | | | | |_   _|_ _| |_   _/ _ \ / _ \| |    
 | |\/| | | | | |   | |  | |    | || | | | | | | |    
 | |  | | |_| | |___| |  | |    | || |_| | |_| | |___ 
 |_|  |_|\___/|_____|_| |___|   |_| \___/ \___/|_____|   {}mobil için

{}[{}1{}] {}PyPhisher 
{}[{}2{}] {}Sms Bomber
{}[{}3{}] {}İp Sorgu {}# BAKIMDA #KODLANMA AŞAMASINDA
{}[{}4{}] {}Panel Sitesi {}#VPN GEREKTİRİR
                                           
    """.format(Fore.LIGHTBLUE_EX, Fore.BLUE, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX,
               Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.BLUE))
    termuxanamenu = input("{}Hangi Toola Giriş Yapmak İstersiniz: {}".format(Fore.BLUE, Fore.RESET)).lower()
    if termuxanamenu == ("1"):
        termux31()
        pyphsihersoru = input("{}Önceden hiç PyPhisher kurdunuz mu? {}y{}/{}n: {}".format(Fore.BLUE,Fore.GREEN, Fore.BLUE,Fore.RED, Fore.RESET)).lower()
        if pyphsihersoru == ("n"):
            os.system("git clone https://gitlab.com/KasRoudra/PyPhisher.git")
            os.system("pkg install git python php openssh -y")
            os.system("pip install pyphisher")
            os.system("pip install -r files/requirements.txt --break-system-packages")
            os.chdir(phishing_klasor)
            os.system("python pyphisher.py")
        if pyphsihersoru == ("y"):
            termux31()
            os.chdir(phishing_klasor)
            os.system("python pyphisher.py")
        if pyphsihersoru != ("y","n"):
            termux31()
            time.sleep(3)
            print(Fore.LIGHTRED_EX +"Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
            os.system("python3 multitool.py")
    if termuxanamenu == ("2"):
        termux31()
        smsbombersoru = input("{}Önceden hiç Sms Bomber kurdunuz mu? {}y{}/{}n: {}".format(Fore.BLUE,Fore.GREEN, Fore.BLUE,Fore.RED, Fore.RESET)).lower()
        if smsbombersoru == ("n"):
            print(Fore.LIGHTBLUE_EX + "Yüklenmesi Biraz Zaman Alabilir..")
            time.sleep(1.5)
            termux31()        
            os.system("git clone https://github.com/vHzEren/erenbomb.git")
            os.chdir(sms_klasor)
            os.system("pip install -r requirements.txt")
            os.system("python erenbomb.py")
        if smsbombersoru == ("y"):
            termux31()
            os.chdir(sms_klasor)
            os.system("python erenbomb.py")
        if smsbombersoru != ("y", "n"):
            termux31()
            print(Fore.LIGHTRED_EX +"Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
            time.sleep(3)
            os.system("python multitool.py")
    if termuxanamenu == ("3"):
        termux31()
        ipsorgusorusu_termux = input("{}Önceden hiç İp Sorgu kurdunuz mu? {}y{}/{}n: {}".format(Fore.BLUE,Fore.GREEN, Fore.BLUE,Fore.RED, Fore.RESET)).lower()
        if ipsorgusorusu_termux == ("n"):
            termux31()
            print(Fore.LIGHTBLUE_EX + "Dosyalar Yükleniyor..")
            time.sleep(1.5)
            os.system("git clone https://github.com/vHzEren/ipsorgu.git")
            os.chdir(ipsorgu_klasor)
            os.system("python ipsorgu.py")
        if ipsorgusorusu_termux == ("y"):
            termux31()
            os.chdir(ipsorgu_klasor)
            os.system("python ipsorgu.py")
        if ipsorgusorusu_termux != ("y", "n"):
            termux31()
            print(Fore.LIGHTRED_EX +"Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
            time.sleep(3)
            os.system("python multitool.py")
    if termuxanamenu == ("4"):
        termux31()
        print(Fore.BLUE +""" Panel Sitesini Tarayıcınıza Girin {}#VPN GEREKTİRİR
        {}https://nopanel.pics/login""".format(Fore.LIGHTBLUE_EX, Fore.RED + Back.WHITE))
        time.sleep(5)
if cihaz_soru == ("linux"):
    termux31()
    print("COMING SOON")
    time.sleep(5)
if cihaz_soru != ("win","android","linux"):
    os.system("cls||clear")
    print(Fore.LIGHTRED_EX +"Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
    time.sleep(3)
    os.system("python multitool.py")
