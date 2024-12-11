import os, time

list_film = [['Harry Potter', '14:00'],
             ['The Wicked', '15:00'],
             ['Narnia', '19:00']]

list_menu = [['Spicy Lobster', 90000, 'lobster', 'chili'],
             ['Spinach Salad', 50000, 'spinach', 'mayo'],
             ['Baked Escargot', 120000],
             ['Cheese Burger', 45000],
             ['Hot Dog', 45000],
             ['French Fries', 25000]]

# def film_menu():
#     os.system('cls')
#     for i in range(len(list_film)):
#         print(f'{i+1}. {list_film[i][0]:<15} {list_film[i][1]}')
#         print(' ')

# film_menu()

def menu():
    os.system('cls')
    for i in range(len(list_menu)):
        print(f'{i+1}. {list_menu[i][0]}')

    option = int(input('Choose your option please: '))
    print('list detail menu:')
    return option
    
    # if option == 1:
    #     # for i in range
    #         print(f'This is your choice{list_menu[i]}')

# simpan=menu()
# for i in range(len(list_menu[simpan-1])):
#         print(f"{list_menu[simpan-1][i]}")

for i in range(len(list_menu)):
    print(f'{"=" * 20} \nMenu {i+1} {list_menu[i][0]} \n')
    for j in range(len(list_menu[i])):
         print(f"{list_menu[i][j]}")
    