import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
quotes = soup.find_all("h3")

for q in quotes:
    print(q.text)
