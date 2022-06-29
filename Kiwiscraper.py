from email.quoprimime import quote
import requests, psycopg2, json
from bs4 import BeautifulSoup

quote_page = "https://type.fit/api/quotes"

# gets data from typefit api
def collect_quotes_data(quote_page):
    quotes = requests.get(quote_page)

    return quotes

# parses data that returns
# hashmap key: author, value: array of quotes
def parse_quote_data(quotes):
    payload = {}
    quotes_dict = json.loads(quotes.text)

    for i in quotes_dict:
        if i["author"] not in payload.keys():
            payload[i["author"]] = []
            payload[i["author"]].append(i["text"])
        else:
            payload[i["author"]].append(i["text"])

    return payload

# function that takes an author 
# makes a request to https://en.wikipedia.org/wiki/Carl_Sandburg
# finds all image srcs using bs4 
# save srcs 
# hashmap (author -> list of image srcs)
def create_img_data(payload):
    for i in payload:
        result = requests.get("https://en.wikipedia.org/wiki/{}".format(i))

    return

def create_quote_data():

    return

# save all this data in database somehow
def update_db(img_set, quote_set):
    return

def db_query(name):
    return

if __name__ == "__main__":
    create_img_data(parse_quote_data(collect_quotes_data(quote_page)))