def in_stock(text):
    return ('We are crowded very much' not in text
            and 'For security protection, I would like cooperation' not in text
            and 'This product became out of stock' not in text)
