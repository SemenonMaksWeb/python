from finctionals.BS4 import *
from finctionals.File import *
# from finctionals.db import *

# Parsing("https://www.chitai-gorod.ru/" , "html/" , "index.html")
htmlParser = ReadFile("html/index.html")
productAll = PoickElement(".product-card",htmlParser)
productAll =  productAll[0:70]
productTitle = PoickElementAllText(".product-card__title", productAll)
productPrice = PoickElementAllText(".product-price__value", productAll)
productAuthor = PoickElementAllText(".product-card__author", productAll)
productImg = PoickElementAllAtribut(".product-card__img > img", productAll, 'src')
productHref = PoickElementAllAtribut(".product-card__img", productAll, 'href')
print(productHref)
 