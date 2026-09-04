from routes.auth import set_new_password

try:
    new_pswd = input('New password: ')
    cnf_pswd = input('Confirm password: ')

    if new_pswd == cnf_pswd:                    
        set_new_password(new_pswd)
        print("new pswd confirmed")
    else:
        print('new pswd not equal to confirm pswd')
        print('exiting...')
        exit(1)
    
except Exception:
    print(Exception)