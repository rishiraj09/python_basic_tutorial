personA = 1000  # bank balance for person A
personB = 1000  # bank balance for person B
personC = 1000  # bank balance for person C


print("Select account from the option")
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

# a -> account_from
# acount_from -> personA
# user_from -> a


# b -> account_to
# account_to -> personB
# user_to -> b
