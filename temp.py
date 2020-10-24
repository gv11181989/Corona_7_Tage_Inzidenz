import requests
import json
from bs4 import BeautifulSoup

URL = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
headers = {'User-Agent': 'Mozilla/5.0'} 
session = requests.Session()
page = session.get(URL , headers=headers)
bundes_array = []
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.tbody
datum = soup.find(id="wrapperContent")
print (datum)