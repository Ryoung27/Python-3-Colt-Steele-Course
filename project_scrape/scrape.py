#http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from time import sleep


all_quotes = []
base_url="http://quotes.toscrape.com"
url = "/page/1"

while url:

    res = requests.get(f"{base_url}{url}")
    print(f"Now Scraping")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            "text":quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })

    next_btn = soup.find(class_="next")
    url = next_btn.find("a")['href'] if next_btn else None
    sleep(2)

print(all_quotes)

quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote: ")
print(quote["text"])
guess = ''

while guess.lower() != quote["author"].lower()
    guess = input(f"Who said this quote? Guess remaining {remaining_guesses}")
    remaining_guess -= 1
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint: The author was born on {birth_date} {birth_place}.")
    elif remaining_guesses == 2:
        print(f"Here's a hint: The authors first name starts with {quote["author"][0]}")

print("After while loop")