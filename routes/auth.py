from dotenv import find_dotenv, load_dotenv, set_key
import os, hmac, bcrypt
load_dotenv()

def set_new_password(password: str):
    
    #yummy salt
    salt = bcrypt.gensalt()
    new_password = password.encode('utf-8')
    
    hashed_pswd = bcrypt.hashpw(new_password, salt).decode('utf-8')
    
    
    env_file = find_dotenv()
    set_key(env_file, "PSWD", hashed_pswd)
    load_dotenv(env_file, override=True)
    

def is_authorized(username:str, password : str) -> bool:
    
    #compare usernames
    username_in_env = os.getenv('USR', '')
    is_user_correct : bool = hmac.compare_digest(username, username_in_env)
    
    #compare passwords
    password_in_env = os.getenv('PSWD', '').encode('utf-8')
    
    is_pswd_correct : bool = bcrypt.checkpw(password.encode('utf-8'), password_in_env)
    
    return is_user_correct and is_pswd_correct
