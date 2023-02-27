import csv 
from datetime import datetime
# Defining variables
options = ['View current balance', 'Record a debit (withdraw)', 'Record a credit (deposit)', 'Exit']
client_input = ''
global cur_bal 
cols = ['id', 'location', 'datetime', 'category', 'price', 'balance', 'description']
count = 0
count +=1

# defining Welcome function
def greeting():
    print('~~~ Welcome to your Checkbook! ~~~\n')
    print()

# defining menu options function
def show_menu():
    for i in range(0, len(options)):
        print(f'{i + 1} ) {options[i]}')
        print()

# defining a function asking if the user wants to do another transaction or not
def want_cont():
    consumer_cont = input('Would you like to go to the main menu? \n\nY / N\n\n')
    if consumer_cont.lower()[0] == 'y':
        print()
        print('Transaction recorded. Redirecting you to the main menu.')
    elif consumer_cont.lower()[0] == 'n':
        print()
        end_checkbook()
        store_balance()
        exit()
    else: 
        print('Invalid response.')

#defining main menu options and their funcs
def menu_opts():
    while True:
        print('What would you like to do?\n\nPlease input the corresponding number for any of the following actions:\n\n')
        show_menu()
        client_input = input('Your choice: ')
        if client_input.isdigit() == True:
            client_input = int(client_input)
            
            # if client wants to check current balance
            if client_input == 1:
                display_currentbalance()
                print()

            # if client wants to make a withdraw
            if client_input == 2:
                new_bal_after_trans()
                print()
                want_cont()
                print()  

            
            # if client wants to make a desposit
            if client_input == 3:
                new_bal_after_depo()
                print()
                want_cont()
            
            #if client wants to quit the checkbook
            if client_input == 4:
                print()
                end_checkbook()
                store_balance()
                exit()

            if int(client_input) > 4:
                print('Invalid input. Redirecting you.\n\n')
            
        else:
            print('Invalid input. Redirecting you.\n\n')

# defining a function that takes the current balance and subtracts the price

def new_bal_after_trans():
    global cur_bal
    '''with open('transactions.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writerow(
            {
                'id': print(count),
                'location': input('Location of transaction: '),
                'datetime': datetime.now(),
                'category': input('Category of transaction: '),
                'price': input('Price of transaction: $')
                if isfloat(client_debit) == True:
                    break
                if isint(client_debit) == True:
                    break
                else:
                    print('Invalid response'),
                'balance': print('$ ', (cur_bal - float(client_debit.strip('$').replace(',', '')))),
                'description': input('Description of transaction: ')
            }
        )'''
    client_debit = input('Withdraw amount: $')
    print()
    if isfloat(client_debit) == True:
       float_bal = client_debit.strip('$').replace(',', '')
       float_bal = float(float_bal)
       float_bal = round(float_bal, 2)       
       cur_bal = cur_bal - float_bal
       print('Withdraw successful.\n\nYour new balance: $', cur_bal)
       return cur_bal
       
    if isint(client_debit) == True:
        float_bal = client_debit.strip('$').replace(',', '')
        float_bal = float(float_bal)
        float_bal = round(float_bal, 2)
        cur_bal = cur_bal - float_bal
        print('Withdraw successful.\n\nYour new balance: $', cur_bal)
        return cur_bal

# defining a function that takes the current balance and adds the deposit amount

def new_bal_after_depo():
    global cur_bal
    '''with open('transactions.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writerow(
            {
                'id': print(count),
                'location': input('Location of transaction: '),
                'datetime': datetime.now(),
                'category': input('Category of transaction: '),
                'price': input('Price of transaction: $')
                if isfloat(client_credit) == True:
                    break
                if isint(client_credit) == True:
                    break
                else:
                    print('Invalid response'),
                'balance': print('$ ', (cur_bal + float(client_credit.strip('$').replace(',', '')))),
                'description': input('Description of transaction: ')
            }
        )'''
    client_credit = input('Deposit amount: $')
    print()
    if isfloat(client_credit) == True:
       float_bal = client_credit.strip('$').replace(',', '')
       float_bal = float(float_bal)
       float_bal = round(float_bal, 2)
       cur_bal = cur_bal + float_bal
       print('Withdraw successful.\n\nYour new balance: $', cur_bal)
       return cur_bal
       
    if isint(client_credit) == True:
        float_bal = client_credit.strip('$').replace(',', '')
        float_bal = float(float_bal)
        float_bal = round(float_bal, 2)
        cur_bal = cur_bal + float_bal
        print('Withdraw successful.\n\nYour new balance: $', cur_bal)
        return cur_bal

# defining a function to return the current balance

def display_currentbalance():
    global cur_bal
    print('Your current balance: $', cur_bal)

# defining a function to exit the checkbook

def end_checkbook():
    global cur_bal
    print('Your current balance: $', cur_bal, '\n\nYou have exited the checkbook.\n\nThank you for your business.')
    return cur_bal

# defining a function that checks if the price is a float type
def isfloat(price):
    try:
        float(price.strip('$').replace(',',''))
        return True
    except ValueError:
        return False

#defining a function checking if the price is an int
def isint(price):
    try:
        int(price.strip('$').replace(',',''))
        return True
    except ValueError:
        return False

def read_balance():
    global cur_bal
    with open('transactions.csv', 'r') as f:
        cur_bal = f.read()
        print(cur_bal)
        return cur_bal

# defining stored balance
def get_balance():
    global current_balance
    with open('balance.txt', 'r') as f:
        current_balance = f.read()
    print('previously recorded balance: ', current_balance)

#defining a function that asks user for initial balance
def initial_bal():
    global cur_bal
    global current_balance
    cur_bal = current_balance
    print()
    cur_bal = cur_bal.strip('$').replace(',', '')
    cur_bal = float(cur_bal)
    print("Your current balance is: $", cur_bal)
    print()
    return cur_bal

def store_balance():
    global cur_bal
    cur_bal = str(cur_bal)
    with open('balance.txt', 'w') as f:
        f.write(cur_bal)