from bs4 import BeautifulSoup

def in_stock(text):
    soup = BeautifulSoup(text, 'html.parser')
    price_block = soup.find(id='priceblock_ourprice')
    if price_block is None:
        return False
    price = int(''.join(filter(str.isdigit, price_block.string)))
    return price < 34_000