# task 1

shoppingList = ["eggs", "milk", "bread"]

def shopping():
    newItem = input("What to add to the list? ")
    shoppingList.append(newItem)
    return
shopping()

# task 2

def stopShopping():
    removeItem = input("What to remove from the list? ")
    shoppingList.remove(removeItem)
    return
stopShopping()

# task 3

i = 1
for entry in shoppingList:
    print(str(i) + " ", entry)
    i += 1

