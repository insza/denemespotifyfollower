import requests
from platform import system

from click import clear
import os, time
from pystyle import Colors, Colorate
import os
#kodu çalan etek giysin - insza
os.system('cls||clear')
print(Colorate.Horizontal(Colors.purple_to_red, ("════════════ Bu İşlem Biraz Uzun Sürebilir, Lütfen Programı Kapatmayınız! ════════════")))
time.sleep(0.6)
print(Colors.light_red, ("""\n\n_________    _________   ______          
__________________  /__________  /   ___  /______  __
_  ___/  __ \  __  /_  _ \  __  /    __  __ \_  / / /
/ /__ / /_/ / /_/ / /  __/ /_/ /     _  /_/ /  /_/ / 
\___/ \____/\__,_/  \___/\__,_/      /_.___/_\__, /  
                                            /____/      """))
print(Colors.red, ("""\n                                      __  
                                     |__| 
                                     |  | 
                                     |  | 
                                     |__|
                                       
            """))
time.sleep(0.9)
print(Colors.orange, ("""                                                
                                     ____   
                                    /    \  
                                   |   |  \ 
                                   |___|  / 
                                        \/  
            """))
time.sleep(0.9)
print(Colors.yellow, ("""                                                
                                      ______ 
                                     /  ___/ 
                                     \___ \  
                                    /____  > 
                                         \/  
            """))
time.sleep(0.9)
print(Colors.green, ("""                                                
                                    ________ 
                                    \___   / 
                                     /    /  
                                    /_____ \ 
                                          \/ 
            """))
time.sleep(0.9)
print(Colors.purple, ("""                                                
                                   _____    
                                    \__  \   
                                     / __ \_ 
                                    (____  / 
                                         \/  
            """))
time.sleep(0.9)
os.system("cls||clear")
print(Colorate.Horizontal(Colors.purple_to_red, ("════════════════════════ İşlem Tamamlanıyor.. ════════════════════════\n\n")))
f = open("./proxy/inszaproxy.txt",'wb')
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https5&country=all")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all")
 f.write(r.content)
except:
 pass#kodu çalan etek giysin - insza
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&country=all")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
 f.write(r.content)
except:
 pass
try:#kodu çalan etek giysin - insza
 r = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxyscan.io/download?type=socks4")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxyscan.io/download?type=socks5")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxyscan.io/download?type=http")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxyscan.io/download?type=https")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
 f.write(r.content)
 f.close()
except:
 f.close()
try:
 r = requests.get("https://www.socks-proxy.net/")
 part = str(r.content)
 part = part.split("<tbody>")#kodu çalan etek giysin - insza
 part = part[1].split("</tbody>")
 part = part[0].split("<tr><td>")
 proxies = ""
 for proxy in part:
  proxy = proxy.split("</td><td>")
  try:
   proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
  except:
   pass
 out_file = open("./proxy/inszaproxy.txt","a")
 out_file.write(proxies)
 out_file.close()
except:
 pass#kodu çalan etek giysin - insza
print(Colors.green, ("\n\n> Proxyler İndirildi Ve inszaproxy.txt Dosyasına Kaydedildi!\n\n"))
sayi = int(input((Colorate.Horizontal(Colors.red_to_yellow,"Herhangi Bir Rakama Basın Ve Spotify Bot Basma İşlemine Geçin!\n\n> @insza  "))))

if sayi > 0:
 os.system("python insza.py")#kodu çalan etek giysin - insza 