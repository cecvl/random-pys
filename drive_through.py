menu_items = ['cheeseburger','fries','soda','ice cream','cookie']
print("Welcome to the Drive Through!")
def welcome():
    print("Select an Item: ")
    for i in range(len(menu_items)):
        print(f"{i+1}) {menu_items[i]}")

welcome()
choice = int(input("Enter choice: "))
user_choices = []
user_choices.append(menu_items[choice-1])

def user_input():
    response = input("Would you like to add another item? Y or N : ")
    if response == "Y" or response == "y":
        welcome()
        choice = int(input("Enter choice: "))
        user_choices.append(menu_items[choice-1])
        print("You ordered: ")
        print(user_choices)
    elif response == "N" or response == "n":
        print("You ordered: ")
        print(user_choices)
        print("Thank you for your order!")
    else :
        print("Invalid choice")
        user_input()

user_input()        

