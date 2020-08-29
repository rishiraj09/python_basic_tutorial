# Banking Project
# function to show banking operations
def options():
    print('1 - Display balance')
    print('2 - Deposit balance')
    print('3 - Withdraw balance')
    print('4 - Transfer balance')
    print('0 - Quit Banking')


options()

personA = 1000  # bank balance for person A
personB = 1000  # bank balance for person B


# take input from the user in integer form to select banking option
banking_option = int(input('Enter Option:'))
while True:
    if banking_option == 1:
        print('**** Display Balance ****')
        print('Person A', str(personA))
        print('Person B', str(personB))
        options()
        banking_option = int(input("Enter Option: "))

    elif banking_option == 2:
        print('**** Deposit Balance ****')
        print('a - personA')  # option to select person A
        print('b - personB')  # option to select person B
        print('q - Quit banking')

        user = input('Enter option to select Person:')

        if user == 'a':
            print("Deposit Balance in Person A")
            balance = float(input('Enter amount to deposit: '))
            personA = personA + balance
            print('New Balance is :', str(personA))

        if user == 'b':
            print("Deposit Balance in Person B")
            balance = float(input('Enter amount to deposit: '))
            personB = personB + balance
            print('New Balance is :', str(personB))

        options()
        banking_option = int(input("Enter Option: "))

    else:
        print('Thank You for Banking with us.')
        break
