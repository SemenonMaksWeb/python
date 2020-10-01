from array import *
from bs4 import BeautifulSoup
 
#  Принимает Selector - что искать soup где искать
# Возвращает результат поиска
def PoickElementAll(selector ,soup):
	result_arr = []
	for index, elem in enumerate(soup):
		result  = elem.select(selector)
		if (len(result) != 0):
			result_arr.append(result[0])
	return result_arr


#  Принимает Selector - что искать soup где искать
# Возвращает результат поиска текст elementa
# Проверяет что текст сущетствует 
#убирает всё унинкоды линшие пробелы табы и тд 
def PoickElementAllText(selector ,soup):
	result_arr = []
	for index, elem in enumerate(soup):
		result  = elem.select(selector)
		if (len(result) != 0):
			if(len(result[0].text) > 1 ):
				result = result[0].text 
				result = result.split()
				result = ' '.join(result)
				result_arr.append(result)
	return result_arr

#  Принимает Selector - что искать soup где искать
# Возвращает результат поиска атрибут  elementa
def PoickElementAllAtribut(selector ,soup , nameAtr):
	result_arr = []
	for index, elem in enumerate(soup):
		result  = elem.select(selector)
		if (len(result) != 0):
			result = result[0].attrs[nameAtr] 
			result_arr.append(result)
	return result_arr




# Принимает Selector - селектор поиска ,soup-где искать
# Возвращает результат поиска
def PoickElement(selector ,soup):  
	return soup.select(selector)