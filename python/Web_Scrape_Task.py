import requests
import time
from bs4 import BeautifulSoup


'''use BS to scrape mubasher.com
show user a list of companies
user picks
show user stock info after scraping the page related to the company'''


list_ = ["NAPESCO", "CBK", "NBK"]

print("Speed Stock Info Getter")

time.sleep(0.5)

ls_print = print("Choices of listed companies: \n1. NAPESCO \n2. CBK \n3. NBK")

list_num = input("Please Pick The Number Corresponding To Your Choice \nOR 'end' to Exit: ")

print("\n\n\n")

while list_num != "end":
	if list_num.isnumeric():
		list_num = int(list_num)- 1
	Upick = print("\tViewing "+ list_[int(list_num)])
	
	
	site = requests.get("https://english.mubasher.info/markets/BK/stocks/%s" % list_[int(list_num)])
	src = site.content
	soup = BeautifulSoup(src, 'lxml')
	print()
	
	
	Closing = soup.find("div", class_="market-summary__last-price")
	print("Closing Price: " + Closing.text)
	print()
	
	'''Through all divs with class "summary block row" find the spans
	Then for all 'things' in span make a list: <span[is tag] class="blablabla">Volume[is thing]</span[end tag]>
	Then check things in list for "name" and print things'''

	dig = soup.div
	for things in dig.find_all('div', class_='market-summary__block-row'):
		spn = things.find_all('span')
		row = [i.text for i in spn]
		#print(row)
		for i in row:
			if "Volume" in row:
				print(i)
				print()
			elif "Turnover" in row:
				print(i)
				print()

	for things in dig.find_all('div', class_='stock-overview__text-and-value-item'):
		spans = things.find_all('span')
		things_in_spans = [i.text for i in spans]
		for i in things_in_spans:
			if 'Current Total Shares' in things_in_spans:
				print(i)
				print()
			elif 'Company Capital' in things_in_spans:
				print(i)
				print()
	

	print()
	list_num = input("-----Pick Another Number\n-----OR 'end' to Exit: ")
	print("\n\n")

print("Thanks For Using Speed Stock")










'''Through all divs with class "summary block row" find the spans
	Then for all spans make a list of things in spans: <span[is tag] class="blablabla">Volume[is thing]</span[end tag]>
	Then check everything[i] in list for "name" and print thing[i]'''