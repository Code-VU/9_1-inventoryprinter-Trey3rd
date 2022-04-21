stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    stuffcount = 0
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
        stuffcount = stuffcount + inventory[key]
    print("Total number of items:", stuffcount)
##displayInventory(stuff)