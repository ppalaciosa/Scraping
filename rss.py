#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

url = "http://elcomercio.feedsportal.com/rss/politica.xml"
r = requests.get(url)

sx = BeautifulSoup(r.content, 'xml')

# XML parsing
items = sx.find_all("item")

noticias = []

# elem - Cada una de las noticias
for elem in items:
    # Indice
    k = items.index(elem)

    # Titular
    titular = elem.contents[0].text

    # Fecha de la noticia
    fecha = elem.contents[3].text

    # Nota breve
    nota = BeautifulSoup((elem.contents[2].text)).text
    
    noticias.append({"titular": titular, "fecha": fecha, "nota": nota})

# Abriendo archivo para escritura
out_file = open("noticias.json","w")
# Grabando con indentado 4
json.dump(noticias, out_file, indent=4)      
# Cerrando el archivo
out_file.close()

#soup.find_all("item")[2].contents[3].text
#Out[100]: u'Fri, 17 Jul 2015 23:53:00 GMT'

#BeautifulSoup( soup.find_all("item")[2].contents[0].text).text
# u'Humala: "Respaldo a Nadine y la felicito por defenderse"'

#BeautifulSoup( soup_xml.find_all("item")[2].contents[2].text).text 
# u'El mandatario reiter\xf3 su respaldo a Nadine Heredia y lament\xf3 que ofensas contra ella provengan "de otras mujeres"'

