import sqlite3
import requests
from bs4 import BeautifulSoup

#REQUEST URL
response = requests.get("http://books.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
print(books)
for book in books:
    print(book.find("h3").find("a")["title"])
    # print(book.select(".price_color"))
