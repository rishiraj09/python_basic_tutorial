# Banking Project
# function to show banking operations
def options():
    print('1 - Display balance')
    print('2 - Deposit balance')
    print('3 - Withdraw balance')
    print('4 - Transfer balance')
    print('0 - Quit banking')


def select_accounts(account_from, account_to):
    withdraw_from = account_from
    deposit_to = account_to
    print(withdraw_from)
    print(deposit_to)

    # if amount > withdraw_from:
    #     return print("Inufficient balance")
    # else:
    #     withdraw_from = withdraw_from - amount
    #     deposit_to = deposit_to + amount
    #     print("New balance for " + account_from )


options()

personA = 1000  # bank balance for person A
personB = 1000  # bank balance for person B
personC = 1000  # bank balance for person C


# take input from the user in integer form to select banking option
banking_option = int(input("Enter Option: "))


while True:
    if banking_option == 1:
        print('*** Display Balance ***')
        print('Person A', personA)
        print('Person B', personB)
        print('Person c', personC)
        options()
        banking_option = int(input("Enter Option: "))

    elif banking_option == 2:
        print('*** Deposit Balance ***')
        print('a - personA')  # option to select person A
        print('b - personB')  # option to select person B

        user = input('Enter option to select person:')

        if user == 'a':
            print("Deposit Balance in Person A")
            balance = float(input('Enter amount to deposit: '))
            personA += balance
            print('New balance is :', personA)

        if user == 'b':
            print("Deposit Balance in Person B")
            balance = float(input('Enter amount to deposit: '))
            personB += balance
            print('New balance is :', personB)
        options()
        banking_option = int(input("Enter Option: "))

    elif banking_option == 3:
        print('*** Withdraw Balance ***')
        print('a - personA')  # option to select person A
        print('b - personB')  # option to select person B

        user = input('Enter option to select person:')

        if user == 'a':
            print("Withdraw Balance from Person A")
            balance = float(input('Enter amount to withdraw: '))

            if personA < balance:
                print("There is not enough balance")
            else:
                personA = personA - balance
                print('New Balance is :' + str(personA))

        if user == 'b':
            print("Withdraw Balance in Person B")
            balance = float(input('Enter amount to withdraw: '))

            if personB < balance:
                print("There is not enough balance")
            else:
                personB = personB - balance
                print('New Balance is :' + str(personB))

        options()
        banking_option = int(input("Enter Option: "))

    elif banking_option == 4:
        print("*** Transfer Balance ***")
        print("a -> PersonA")
        print("b -> PersonB")
        print("c -> PersonC")

        account_from = input("Enter user from: ")
        account_to = input("Enter user to: ")
        amount = float(input("Enter amount to be transferred:"))

        if account_from == 'a':
            user_from = 'a'
            account_from = personA
        if account_from == 'b':
            user_from = 'b'
            account_from = personB
        if account_from == 'c':
            user_from = 'c'
            account_from = personC

        if account_to == 'a':
            user_to = 'a'
            account_to = personA
        if account_to == 'b':
            user_to = 'b'
            account_to = personB
        if account_to == 'c':
            user_to = 'c'
            account_to = personC
        print(account_from)
        print(account_to)

        if amount > account_from:
            print("Insufficient balance")
        else:
            account_from = account_from - amount
            account_to = account_to + amount

            if user_from == 'a':
                personA = account_from
                acc_from = 'PersonA'
            if user_from == 'b':
                personB = account_from
                acc_from = 'PersonB'
            if user_from == 'c':
                personC = account_from
                acc_from = 'PersonC'

            if user_to == 'a':
                personA = account_to
                acc_to = 'PersonA'
            if user_to == 'b':
                personB = account_to
                acc_to = 'PersonB'
            if user_to == 'c':
                personC = account_to
                acc_to = 'PersonC'

            print("Rs."+str(amount) + " transfered from "+acc_from+" to "+acc_to)
            print(acc_from+" available balance :" + str(account_from))
            print(acc_to+" available balance :" + str(account_to))

        options()
        banking_option = int(input("Enter Option: "))

    else:
        print('Thank you for banking with us')
        break
