from platform import system
from turtle import title

from click import clear
from follow_bot import spotify
import threading, os, time
from pystyle import Colors, Colorate

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
sayi = int(input((Colorate.Horizontal(Colors.blue_to_cyan,"[1] Proxy Toplansın!\n\n[2] Proxy Toplanmasın!\n\n> @insza  "))))

if sayi == 1:
 os.system("python proxytopla.py")
if sayi == 2:
 os.system("python insza.py")