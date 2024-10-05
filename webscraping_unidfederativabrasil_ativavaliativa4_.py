
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

url = 'http://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o'

response = requests.get(url)

# Criando a sopa
soup = BeautifulSoup(response.text, "html.parser")

tabela = soup.find_all('table')
tabela = soup.find('span', 'mw-editsection').find_next('table')

# transformando código HTML em um objeto StringIO
tabela_io = StringIO(str(tabela))

# Transformando a tabela em um DataFrame
df = pd.read_html(tabela_io)[0]
df
