import requests
from bs4 import BeautifulSoup


url = lambda i: "http://www.admision.uni.edu.pe/resultado_cepre.php?pagina="+ str(i) +"&txt_numins=&txt_paterno=&txt_materno=&txt_nombres="

r = requests.get(url)
# Loading...
# "r.content" => raw content


soup = BeautifulSoup(r.content)
# Converting into something usable
# "print soup.prettify()" => Displays content cleaned up

links = soup.find_all("a")
# Picks all the "a" tags obtained by request.get

#for link in links:
   # if "http" in link.get("href"): # Filter only href with http
#       print "'%s' %s" %(link.get("href"), link.text) #text: tag content

g_data = soup.find_all("tr", {"class": ["lista_0", "lista_1"]})

for item in g_data:
    if "INGRESO" in item.text:
        print item.contents[1].text # prints a list. It's good to check its elements. 
        print item.contents[5].text
        print item.contents[37].text
        print item.contents[49].text
