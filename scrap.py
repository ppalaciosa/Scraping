import requests
from bs4 import BeautifulSoup

u = lambda i: "http://www.admision.uni.edu.pe/resultado_cepre.php?pagina="+ str(i) +"&txt_numins=&txt_paterno=&txt_materno=&txt_nombres="
r = lambda u: requests.get(u)

def get_data_from_url (items=10):
    for k in range(1,items+1):
        url = u(k)
        req = r(url)
        soup = BeautifulSoup(req.content)
        links = soup.find_all("a")
        g_data = soup.find_all("tr", {"class": ["lista_0", "lista_1"]})

        for item in g_data:
            if "INGRESO" in item.text:
                print item.contents[1].text
                print item.contents[5].text
                print item.contents[37].text
                print item.contents[49].text

get_data_from_url()



