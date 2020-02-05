def mysterious_func(num):
    '''Takes a number 'num' and returns some other number.
    at some cases this function raises ValueError. 
    '''
    # assert num % 3 == 0, f'{num} must divide by 3.'

    if num % 3 != 0:
        raise ValueError(f'{num} must divide by 3.')
    return int(num / 3)

def check_password(password):
    if password != 'admin123':
        raise ValueError('Wrong password')


def authenticate():
    with open('password_history.txt', 'w') as history:
        while True:
            try:
                password = input('Password: ')
                check_password(password)
            except ValueError as e:
                print(e)
                passed = False
            else:
                print('Welcome!')
                passed = True
                return
            finally:
                history.write(f'{password} (passed={passed})\n')


mysterious_func(4)
# authenticate()

