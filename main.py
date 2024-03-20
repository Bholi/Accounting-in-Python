credentials = [
    {
        'username': 'Ram',
        'password': 'ram'
    },
    {
        'username': 'Sita',
        'password': 'sita'
    },
]
accounts = [
    {
        'username': 'Ram',
        'amount': 1000
    },
    {
        'username': 'Sita',
        'amount': 500
    }
]
count = 0
username = input('Enter your name : ')
password = input('Enter your password : ')
for i in credentials:
    if i['username'] == username and i['password'] == password:
        print('Login Successful !')
        a = input('Do you want to deposit, withdraw or view balance : ')
        if a == 'deposit':
            amount = int(input('Enter the amount to deposit : '))
            for a in accounts:
                if a['username'] == username:
                    a['amount'] += amount
                    print(a['amount'])
        elif a == 'withdraw':
            amount = int(input('Enter the amount to withdraw : '))
            for a in accounts:
                if a['username'] == username:
                    if a['amount'] < amount:
                        print('Insufficient Balance')
                    else:
                        a['amount'] -= amount
                        print(a['amount'])
        elif a == 'view balance':
            for a in accounts:
                if a['username'] == username:
                    print(a['amount'])
    else:
        count += 1

if count == 2:
    print('Invalid credentials')
