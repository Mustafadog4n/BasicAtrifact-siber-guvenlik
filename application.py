import sqlite3
from pathlib import Path

import csv
import os
from sys import modules
import socket
from datetime import datetime
import psutil


#bilgisaya kullanıcı ana dizinini alır
root_dir = Path("~").expanduser()
def chromeHistory():
    print("############# Chrome Geçmişi #################")
    connection = sqlite3.connect(root_dir /'AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                      datetime(last_visit_time/1000000-11644473600, "unixepoch") as last_visit_time, 
                      url, 
                      title, 
                      visit_count 
                    FROM urls ORDER BY last_visit_time desc""")
    urls = cursor.fetchall()
    with open('history.csv', 'w', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile)
        for url in urls:
            spamwriter.writerow(url)
    input("İşlemler Tamamlandı...")
def fileHistory():
    print("############# Dosya Geçmişi #################")
    os.chdir(root_dir /"AppData/Roaming/Microsoft/Windows/Recent")
    files = os.listdir()
    for file in files:
        print(file)
    input("İşlemler Tamamlandı...")
##running process
def RunningProcess():
    c=0
    for proc in psutil.process_iter(['pid', 'name']):
        c=c+1
        print(proc.info)
        
    print ("\nToplam Çalışan Uygulama : ", c)
    input("İşlemler tamamlandı ..")
##portscanner(port tarama)
def PortScanner():
    print("Lütfen İp Adresinizi Giriniz :")
    deger=input()

    print("----------------- PORT SCANNER -------------------")
    print("-" * 50)
    print("Taranan ip Adresi: " + deger)
    print("Tarama Zamani:" + str(datetime.now()))
    print("-" * 50)
    # will scan ports between 1 to 65,535  
    try:
        for port in range(1,100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = s.connect_ex((deger,port))
            if result ==0:
                print("Port {} Açık".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n programdan cıkıs yapılıyor !!!!")
        input("Hata alındı ..")
        #modules.exit()
    except socket.gaierror:
        print("\n ıp adresı bulunamadı !!!!")
        input("Hata alındı ..")
        #modules.exit()
    except socket.error:
        print("\ sunucu bulunamadı  !!!!")
        input("Hata alındı ..")
        #modules.exit()
    
    


while True:
    print("Lütfen Yapacağınız İslemi Seçiniz : ")
    print("1 : Chrome Gecmisini Göster ?")
    print("2 : Son Görülen Klasörleri Göster ?")
    print("3 : Çalışan Uygulamaları Göster ?")
    print("4 : Port Taraması Gerçekleştir ?")
    deger =input()
    if(deger=="1"):
        chromeHistory()
        break;   
    elif(deger=="2"):
        fileHistory()
        break; 
    elif(deger=="3"):
        RunningProcess()
        break; 
    elif(deger=="4"):
        PortScanner()
        break;      
    else:
        print("Lütfen Yapilacak İslemi Seciniz !")
    

    

