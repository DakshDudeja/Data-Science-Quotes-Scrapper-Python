import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.goodreads.com/quotes/tag/{}"
url.format("love")
res=requests.get(url)
soup=BeautifulSoup(res.text)
soup
links=soup.find_all("a")
quote_divs=soup.find_all("div",attrs={"class" : "quote"})
quote_divs=quote_divs[0]
quote_divs

quoteText_div=quote_divs.find("div", attrs={"class" : "quoteText"})
quoteText_div

striped=quoteText_div.text.strip()
print(striped)

striped_li=striped.split("\n")
striped_li
quote=striped_li[0][1:-1]
author=striped_li[-1].strip()

quote
author

df=pd.DataFrame(columns=['striped'])
df.to_csv("scrap.csv", index=None)
f = open("Quotes.csv", "wb")

f.write(striped)

f.close()