import requests
import json
from bs4 import BeautifulSoup

    
URL = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
page = requests.get(URL)
bundes_array = []
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.tbody
datum = soup.find(id="wrapperContent").find(
    class_='text').findAll('p')[0].text[7:17]
for x in range(16):
    bundesland = table.findAll('tr')[x].findAll(
        'td')[0].text.replace("\xad", "").replace("\n", "")
    Inz = table.findAll('tr')[x].findAll('td')[4].text
    zahlen = {"bundesland": bundesland, "inzidenz": Inz}
    bundes_array.append(zahlen)


def to_array():
    bundesweit = {"datum": datum, "zahlen": bundes_array}
    # print (bundesweit)
    return (bundesweit)

