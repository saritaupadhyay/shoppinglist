def main():
	shopping_list = []
	while (True):
		print ("If you'd like to quit at any time, write 'exit'")
		item_to_add = raw_input("Enter shopping list item: ")
		if item_to_add == "exit":
			shopping_list.sort()
			print ("Here is your final shopping list: ", shopping_list)
			break
		else:
			shopping_list.append(item_to_add)
			shopping_list.sort()
			print ("Your shopping list now includes ", shopping_list)


if __name__ == '__main__':
	main()
