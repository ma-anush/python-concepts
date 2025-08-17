gorecery_items ={}
def add_items(name, price):
    gorecery_items[name]=price
    print(f"it is a {name} price of the productis  : {price}")

def remove_items(name):
    if name in gorecery_items:
        del gorecery_items[name]
        print(f"{name } has been removed from the list")
    else:
        print(f"{name}Invalid : that item not in the gorcery list")

def view_items():
    print("the display of the gorcery list is")
    for item,price in gorecery_items.items():
        print(f"{item}is price is {price}")
def total_cost():
    total = sum(gorecery_items.values())
    print(f"total of the product is {total}")








    
    