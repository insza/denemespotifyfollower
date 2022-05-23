from platform import system
from turtle import colormode

from click import clear
from colorama import colorama_text
from follow_bot import spotify
import threading, os, time
from pystyle import Colors, Colorate
from turtle import title
import os, time

import os

os.system('cls||clear')






lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
line = print(Colorate.Horizontal(Colors.green_to_blue, ("                              ╚╦══════════════════════════════════╦═════════════════════╦╝")))
print(Colorate.Horizontal(Colors.green_to_blue, ("""                                                         
                       
                                  ,--,                                                   
                                ,--.'|         ,---,                   ,----,            
                                |  |,      ,-+-. /  | .--.--.        .'   .`|            
                                `--'_     ,--.'|'   |/  /    '    .'   .'  .' ,--.--.    
                                ,' ,'|   |   |  ,"' |  :  /`./  ,---, '   ./ /       \   
                                '  | |   |   | /  | |  :  ;_    ;   | .'  / .--.  .-. |  
                                |  | :   |   | |  | |\  \    `. `---' /  ;--,\__\/: . .  
                                '  : |__ |   | |  |/  `----.   \  /  /  / .`|," .--.; |  
                                |  | '.'||   | |--'  /  /`--'  /./__;     .'/  /  ,.  |  
                                ;  :    ;|   |/     '--'.     / ;   |  .'  ;  :   .'   \ 
                                |  ,   / '---'        `--'---'  `---'      |  ,     .-./ 
                                ---`-'                                     `--`---'     
                                                                                                                                                                 """)))
v2 = print(Colorate.Horizontal(Colors.green_to_blue, ("                              ╚╦══════════════════════════════════╦═════════════════════╦╝")))
spotify_profile = str(input(Colorate.Horizontal(Colors.green_to_white,  ("\n\nSpotify Link: "))))
threads = int(input((Colorate.Horizontal(Colors.white_to_green, "\nHız(100 önerilir) : "))))

def load_proxies():
    if not os.path.exists("./proxy/inszaproxy.txt"):
        print(Colorate.Horizontal(Colors.red_to_white, ("\nProxy Dosyası Bulunamadı!")))
        time.sleep(10)
        os._exit(0)
    with open("./proxy/inszaproxy.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print(Colorate.Horizontal(Colors.red_to_white, ("\nProxy Dosyasında Proxy Yok!")))
            time.sleep(10)
            os._exit(0)

print(Colors.green, ("\n[1] Proxy VAR(önerilir)"))
print(Colors.red, ("\n[2] Proxy YOK"))
print(Colors.gray, ("\n[UYARI] PROXYLER HTTPS & HTTP OLMAK ZORUNDADIR! "))
option = int(input(Colorate.Horizontal(Colors.purple_to_red, ("\n> @insza "))))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print(Colorate.Horizontal(Colors.green_to_white, ("[BAŞARILI] Takip Edildi! {}".format(counter))))
    else:
        safe_print(Colorate.Horizontal(Colors.red_to_white, (f"[BAŞARISIZ] Hata! {error}")))
            
while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0
