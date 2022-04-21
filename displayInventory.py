stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    stuffcount = 0
    print("Inventory:")
    for key in stuff:
        print (stuff[key], key)
        stuffcount = stuffcount + stuff[key]
    print("Total number of items:", stuffcount)
displayInventory(stuff)