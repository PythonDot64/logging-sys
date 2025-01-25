"""This file defines functions for the excution in main.py"""

# importing

try:
    from subprocess import call
    from sys import exit as escape
    from time import sleep
    from datetime import date
    import setup_sql
    import game

except ImportError:
    print('import error')

try:
    import bcrypt # type: ignore

except ImportError:
    try:
        call('pip install bcrypt', shell=True)
    except:
        call('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py', shell=True)
        call('python get-pip.py', shell=True)
        call('pip install bcrypt', shell=True)
    finally:
        import bcrypt # type: ignore

    exit(1)

if __name__ == '__main__':
    print('Import Successful\n')


# creating the main function
def main_login() -> None:
    '''This function will take the user to login or register depending on which one they want.'''

    setup_sql.create_table()

    while True:

        is_login_account: str = input('Login or Register?: ').lower()

        if not is_login_account.isdigit() and is_login_account == 'login':
            username: str = login() # declaration on line 45
            break

        elif not is_login_account.isdigit() and is_login_account == 'register':
            username: str = register() # declaration on line 81 (nice)
            break

        print('Invalid Input, Please Try Again')

    main_menu(username=username) # declaration on line 116


# creating the login function
def login() -> str:
    '''This function will login the user to a account'''

    all_accounts: list = setup_sql.cursor.execute('SELECT * FROM Accounts_infos')

    while True:

        username: str = input('\nWhat is your username(Case Sentive)?: ')
        password: str = input('What is your password(Case Sentive)?: ')

        # turning the password into bytes, since checkpw only accept bytes
        password: bytes = password.encode('utf-8')

        # getting all the accounts in the database
        for account in all_accounts:

            # checking the accounts with checkpw to un-hash and check the password
            if username == account[0] and bcrypt.checkpw(

                password=password,
                hashed_password=account[1],

                ):

                print('\nLogin successful!')
                return username

        print('Invalid Input, Please try again')


def is_account_valid(username: str, database: list):
    if username in database:
        return False


# creating the register function
def register() -> str:
    '''This function will register a new account for the user'''

    username, password = get_new_account_info() # declaration on line 101
    date_created = date.today()

    # turning the password into bytes, since hashpw only accept bytes
    password, salt = password.encode('utf-8'), bcrypt.gensalt()

    # hashing the password
    password: bytes = bcrypt.hashpw(password=password, salt=salt)

    setup_sql.insert_data(username=username, password=password, created_date=date_created)

    print('\nAccount Created!')

    return username


# creating the get new account info function
def get_new_account_info() -> str:
    '''This function will get the username and password from user to for the
    new account's creation'''

    while True:
        username: str = input('\nWhat will be your username(Max 16 character)?: ')
        password: str = input('What will be your password(Max 16 character)?: ')

        if len(username) <= 16 and len(password) <= 16:
            return username, password

        print('Invalid Input, Please Try again')


# creating the mainMenu function
def main_menu(username) -> None:
    '''This function will create the main menu which will welcome the user
    and prompt the user which mini-game they want to play'''

    setup_sql.connection.close()

    print('connection closed')

    call('cls', shell=True)

    print(f'-------------------------date:{date.today()}----------------------------------')
    print(f'Welcome {username}\n')

    what_to_do: str = input('What do you want to do?(exit, minigames): ').lower()

    if what_to_do == 'exit':
        print('exiting', end='', flush=True)
        sleep(1)

        print('.', end='', flush=True)
        sleep(1)

        print('.', end='', flush=True)
        sleep(1)

        print('.')
        sleep(1)

        call('cls', shell=True)
        escape()
    elif what_to_do == 'minigames':
        minigame()
    else:
        escape()


def minigame() -> None:
    '''This function ask what minigame the user want to play'''

    what_minigame: str = input('What minigame do you want to play?(Rps): ')

    match what_minigame.lower():
        case 'rps':
            call('cls', shell=True)
            game.Rps.main(self=game.Rps)
        case _:
            print('Error 404: Game Not Found')
            minigame()
