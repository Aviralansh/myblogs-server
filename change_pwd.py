from routes.auth import set_new_password

new_pswd = input('New password: ')

try:

    set_new_password(new_pswd)

except Exception:
    print(Exception)