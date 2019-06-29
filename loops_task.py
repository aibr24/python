
list_of_items = []

 
items = ""


while items!='done':
	items = input("Item (Enter 'done' when finished.): ")	
	if items=='done':	
		print("-- receipt --")
		break	
	prcs = float(input("price:"))
	quant = int(input("quantity:"))
	stuff = {}
	stuff["name"] = items
	stuff["qntt"] = quant
	stuff["price"] = prcs
	list_of_items.append(stuff)

else:
	print("-- reciepl --")

total = 0
for i in list_of_items:
 	print(i["qntt"], i["name"], i["price"])
 	total += i["qntt"]*i["price"]

print("-"*15)
print("Total: %.3f KWD" % total)