from time import sleep
from datetime import datetime




def is_txt_file_found() -> bool:
    try:

        with open('accounts.txt') as file:
            return True
    except FileNotFoundError:
        return False
    
def remove_dublicate_accounts(path):
    try:
        with open('accounts.txt', 'r') as file:
            accounts_counter = file.readlines()
            for account in range(0, accounts_counter):
                if file.read(account) in 'accounts.txt':
                    file.read(account).removeprefix()
                else:
                    continue
    except FileNotFoundError:
        if is_txt_file_found():
            print("")
        else:
            
            print("File yaratilmoqda..")
    