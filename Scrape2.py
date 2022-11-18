# -*- coding: utf-8 -*-
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import os
import sys
import time
from gtts import gTTS
import subprocess

# =====================================================================================
my_url = 'https://www.olx.ba/graficke-kartice/5/154'


uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()
# html parsing
page_soup = soup(page_html, "html.parser")
# grabs each product
containers = page_soup.findAll("div", {"class": "rezultatipretrage"})
#filename
filename = "index.html"
filename2 = "Graficke_Kartice.txt"
brojStranica = 25
with open(filename,'w',encoding="utf-8") as out:
  with open(filename2,'w',encoding="utf-8") as outTxt:

    for i in range(brojStranica):

        # Naslov ajtema
        title_container = page_soup.findAll("p", {"class": "na"})
        product_name = title_container[i].text
        # Cijena ajtema
        price_container = page_soup.findAll("div", {"class": "datum"})
        product_price = price_container[i].text
        # Deskripcija ajtema
        description_container = page_soup.findAll("div", {"class": "pna"})
        product_description = description_container[i].text
        # stanje ajtema
        condition_container = page_soup.findAll("span", {"class": "nko"})
        product_condition = condition_container[i].text
        # current date and time
        sttime = datetime.now().strftime('%Y.%m.%d/%H:%M:%S')
        t0 = time.time()

        print("Time released " + sttime)

        print("Ime proizvoda: " + product_name)

        print("Cijena proizvoda:" + product_price)

        print("Deskripcija: " + product_description)

        print("Stanje Proizvoda: " + product_condition)
        
         
        t1 = time.time()
        
        timef = t1-t0
        
        print("Completed in: ",timef)       
        print("--------------------------")
        
        out.write('<body style="background-color:black;"><h2 style="color:green;">'+ "SERVER-TIME: " + sttime +"</h2>"+'\n')
        out.write('<p style="color:green;">Ime proizvoda: ' + product_name +"\n"+ 'Cijena proizvoda: ' + product_price +"\n"+ 'Deskripcija: ' + product_description +"\n"+ 'Stanje Proizvoda: ' + product_condition + "</p></body>" + "\n")
        outTxt.write('Ime proizvoda: ' + product_name +"\n"+ 'Cijena proizvoda: ' + product_price +"\n"+ 'Deskripcija: ' + product_description +"\n"+ 'Stanje Proizvoda: ' + product_condition + "\n")

    out.close()
    outTxt.close()
t3 = time.time()
print("Obradjivanje teksta sacekaj bo... ")
Fajl = open('Graficke_Kartice.txt','r',encoding="utf-8")
tekst = Fajl.read()
izlaz = gTTS(text=tekst, lang='sr', slow=False)
izlaz.save("tts.mp3")
Fajl.close()
t4 = time.time()
ttsTimeFinish = t4-t3
print("TTS Obradjen za: ",ttsTimeFinish)
input("Press Enter to continue...")
import ttsOtv

