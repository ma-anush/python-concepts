import grocer1 as go
while True:
    print("1. add items")
    print("2. remove items")
    print("3. view items")
    print("4. total cost of items")
    print("5. Exit")

    choice = input("Enter your choice : ")
    if choice == "1":
        name=input("Enter a product name : ")
        price=float(input("Enter the product price : "))
        go.add_items(name,price)
    elif choice == "2":
        name = input("enter the product name ")
        go.remove_items(name)
    elif choice == "3":
        go.view_items()
    elif choice =="4":
        go.total_cost()
    elif choice =="5":
        print("thank you for Visting")
        break

    else:
        print("\nInvalid choice")
