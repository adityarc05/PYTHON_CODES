bill = 0

menu_dict = {'pizza': 250, 'pasta' : 200, 'burger' : 230, 'fries' : 150, 'cocktail' : 350, 'coffee' : 100, 'stop':0}
def menu_2():
    print("MENU")
    print("Pizza : ", menu_dict['pizza'])
    print("Pasta : ", menu_dict['pasta'])
    print("Burger : ", menu_dict['burger'])
    print("Fries : ", menu_dict['fries'])
    print("Cocktail (sex on the beach) : ", menu_dict['cocktail'])
    print("Coffee : ", menu_dict['coffee'])

print(menu_2())

cho = input("Do you wanna order (Yes/No): ")
cho_1 = cho.lower()

if cho_1 == 'yes':
    while True:
        item = input("Enter the item and enter stop to exit :")
        item_2 = item.lower()
        if item_2 == 'stop':
            break
        if item_2 not in menu_dict:
            print("Item not in menu")
            print(menu_2())
        else:
              
            qua = int(input("Enter the quantity :"))
            bill += (menu_dict[item_2])*qua
    print(bill)
    print("Thank You")

else:
    print("Thank You")

