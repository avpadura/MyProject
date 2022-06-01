import requests
from bs4 import BeautifulSoup

"""Enter url"""

url = 'https:.......'

def new_data():
    data = requests.get(url)
    print(data)

new_data()

"""If the responce is 200, that's ok"""