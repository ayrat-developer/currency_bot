import requests
from bs4 import BeautifulSoup as BS

class Parse(): 
    def __init__(self, url):
        self.url = url
        self.values = []
        # Запрос и получение html
        source = requests.get(self.url)
        self.html = BS(source.text, 'lxml')

    def get_content(self):
        table = self.html.find('table', {'id': 'courses-main' })
        tbody = table.find('tbody')

        for tr in tbody.find_all('tr'):
            td = tr.find_all('td', {'class': ''})
            for value in td:
                if value.text != '':
                    self.values.append(value.text.lstrip())

        self.values = self.values[4:]
        return self.values

