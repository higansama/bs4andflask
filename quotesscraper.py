from bs4 import BeautifulSoup
import requests

def ScrapingQuotes():
    source = requests.get("https://quotes.toscrape.com/").text
    soup = BeautifulSoup(source, "html.parser")
    listQuotes = []
    for data in soup.find_all("div", {"class": "quote"}):
        quote = data.find("span", {"class": "text"}).text
        cleanQuote = quote[1:]
        cleanQuote = quote[:-1]
        listQuotes.append(cleanQuote)
    return listQuotes


ScrapingQuotes()