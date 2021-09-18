# msft alternative probing URL: https://www.xbox.com/ja-jp/configure/942j774tp9jn
def in_stock(text):
    return text.count('在庫なし') < 2
