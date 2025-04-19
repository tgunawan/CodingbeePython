# ==========Library==========
import os
import time

#===========Variable==========
text_money = "Your money"
money = 3000
parm = ()
choice = ()

buy_product = ['Buy Product', 'ATM', 'Quit']
product = ['Cracked egg', 'Jar of Fart', 'Rotten Apple', 'Mouse tail', 'Smelly Candle']
price = [300, 1000, 800, 600, 500]

#==========Function==========
def shop():
    print("Welcome to Titah's Shop!")
    for i in range(len(buy_product)):
        print(f'{i+1}. {buy_product[i]}')
    print(f'=====< {text_money} >=====')
    print(f'=====<    {money}    >=====')
    parm=int(input("Input your choice: "))

    if parm == 1:
        print('=' * 36)
        while money > (money - item in price):
            print(f'|{i+1}. {product[i]:<20}| {price[i]:<8}|')
        print('=' * 36)
        print(f'===========< {text_money} >===========')
        print(f'===========<    {money - price[0]}    >===========')
        choice=int(input("Input your choice please: "))
        # if choice == 1:
        #    print('=' * 36)
        #    for i in range(len(product)):
        #     print(f'|{i+1}. {product[i]:<20}| {price[i]:<8}|')
        #     print('=' * 36)
        #     print(f'===========< {text_money} >===========')
        #     print(f'===========<    {money - price[0]}    >===========')
    elif parm == 2:
        print('Welcome to ATM \nHow Much money you want to withdraw?')
    elif parm ==3:
        print('Terima kasih telah menggunakan jasa kami')
    else:
     print('Error')

def shop2(pilihan):
    global money
    if pilihan == 1:
        while True:
            display()
            option=int(input("Input your choice please: "))
            if money>= price[option-1]:
                print(f"You bought {product[option-1]}")
                money-=price[option-1]
                print('=' * 36)
                print(f'===========< {text_money} >===========')
                print(f'===========<    {money}    >===========')
                time.sleep(2)
                buy_again=input('Mau belanja lagi(yes/no)? ').lower()
                if buy_again == 'no':
                    time.sleep(1)
                    menu()
                else:
                    continue
            else:
                input("You don't have enough money")
                menu()
    elif pilihan == 2:
        print('Welcome to ATM \nHow Much money you want to withdraw?')
    elif pilihan ==3:
        print('Terima kasih telah menggunakan jasa kami')
    else:
     print('Error')

# shop()
def menu():
    os.system("cls")
    jawab=int(input("""
    1. Buy Product
    2. ATM
    3. Quit
    Input your choice: """))
    shop2(jawab)

def display():
    os.system("cls")
    print(f'{text_money} Rp. {money}')
    print('=' * 36)
    for i in range(len(product)):
        print(f'|{i+1}. {product[i]:<20}|{price[i]:^10}|')
    print('=' * 36)

#==========Program==========
menu()





#==========End==========
