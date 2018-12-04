import requests
from bs4 import BeautifulSoup
import json

#get web page
url = 'https://www.crimemapping.com/map/location/Champaign,%20IL,%20USA?id=dHA9MCNsb2M9MjA2MjUzNyNsbmc9MzMjcGw9ODMyNzgwI2xicz0xNDo3MjU4NDg3'
print('working...')
response = requests.get(url)
print('Done.')
#parse the table 
soup = BeautifulSoup(response.text,"html.parser")
print('output:')
print(soup.prettify())

