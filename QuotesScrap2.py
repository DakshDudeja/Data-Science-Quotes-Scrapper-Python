import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.goodreads.com/quotes/tag/{}"
def get_quotes(url):    
    res = requests.get(url)

    soup = BeautifulSoup(res.text)

    quote_divs = soup.find_all("div", attrs={"class" : "quote"})
    quotes = []
    for quote_div in quote_divs:

        quoteText_div = quote_div.find_next("div", attrs={"class" : "quoteText"})

        striped = quoteText_div.text.strip()

        striped_li = striped.split("\n")

        quote = striped_li[0][1:-1]
        author = striped_li[-1].strip()

        left_div = quote_div.find_next("div", attrs={"class" : "left"})
        left_div
        tags = [tag.text for tag in left_div.find_all("a")]
        tags

        quote_item = {
            "text" : quote,
            "author" : author,
            "tags" : tags
        }

        quotes.append(quote_item)
    
    return quotes

total = []
for i in range(1, 6):
    total.extend(get_quotes(url.format("love", i)))
    print("processed", i)
    
df = pd.DataFrame(total)
df.to_csv("scrap1.csv", index=None)
df