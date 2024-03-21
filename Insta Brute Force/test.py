from datetime import datetime



def test_connection() -> bool:
    import requests
    try:
        get = requests.get("https://www.google.com/")
        return True
    except requests.exceptions.ConnectionError:
        return False

def is_there_main_function() -> bool:
    try:
        with open('main.py', 'r') as file:
            return True
    except FileNotFoundError:
        return False     

def is_there_filter_function() -> bool:
    try:
        with open('filter.py', 'r') as file:
            return True
    except FileNotFoundError:
        return False

def get_account_file() -> bool:
    """test uchun"""
    import os
    
    with open('test_accounts.txt', 'w') as file:
        file.write("username:password")
    
    try:
        with open('test_accounts.txt', 'r') as f:
            return True
    except FileNotFoundError:
        return False

def get_account_from_file() -> bool:
    import os
    success = 0
    total_success = 1
    with open("test_accounts.txt", 'r') as f:
        users = f.readlines()
        
        user_name = 'username'
        user_password = 'password1'
        for user in users:
            parts = user.strip().split(":")
            username, password = parts
            print(f'Test username: {username} // Test password: {password}')
            if username == user_name and password == user_password:
                success += 1
            

    if success == total_success:
        os.remove('test_accounts.txt')
        print("[+]********** Test file deleted✅🧹 **********[+]")
        return True
    else:
        return False        



    # total_tests = {
    #     '1':'Internet ishlamayapti. Kabel yoki wifi tarmog\'ini tekshiring.',
    #     '2':'Asosiy funksiya fayli mavjud emas! Bunda dastur ishlamayadi',
    #     '3':'Filter fayli mavjud emas! Bu dasturning ishlashiga ta\'sir qilmaydi',
    #     '4':'Test akkounts fayli mavjud emas yoki o\'chirilgan',
    #     '5':'Fayldan ma\'lumot o\'qib bo\'lmadi yoki mavjud emas.'
    # }

  
           
    

        
            

    # os.remove('test_ids.txt')
    # print("Deleted test_ids.txt file success✅")
    # os.remove('errors.txt')
    # print("Deleted errors.txt file success✅")


    






def main_console():
    from time import sleep
    accept = 0
    errors = []
    total_test = 5
    error = 0

    print("[+]********** Starting test... **********[+]")
    sleep(2)
    print("[+]********** Developer: Asadbek Abdubannopov **********[+]")
    sleep(2)
    if test_connection():
        print("[+]********** Internet >>>>>>>> working **********[+]")
        accept += 1
        sleep(2)
    else:
        print("[+]********** Internet >>>>>>>> not working **********[+]")
        print("Warning! Agarda siz bu yozuvni ko'rgan bo'lsangiz sizda internet aloqasi mavjud emas! Bunda dastur ishlamaydi..")
        sleep(2)
        error += 1
        errors.append("Internet ishlamayapti. Kabel yoki wifi tarmog\'ini tekshiring.")

    if is_there_main_function():
        print("[+]********** Function file >>>>>>>> working **********[+]")
        accept += 1
        sleep(2)
    else:
        print("[+]********** Function file >>>>>>>> not found **********[+]")
        sleep(2)
        error += 1
        errors.append("Asosiy funksiya fayli mavjud emas! Bunda dastur ishlamayadi")
       

    if is_there_filter_function():
        print("[+]********** Filter function file >>>>>>>> working **********[+]")
        accept += 1
        sleep(2)
        
    else:
        print("[+]********** Filter function file >>>>>>>> not found **********[+]")
        sleep(2)
        error += 1
        errors.append("Filter fayli mavjud emas! Bu dasturning ishlashiga ta\'sir qilmaydi")
      
    
    if get_account_file():
        print("[+]********** Accounts file >>>>>>>> working **********[+]")
        accept += 1
        sleep(2)

        
    else:
        print("[+]********** Accounts file >>>>>>>> not found **********[+]")
        sleep(2)
        error += 1
        errors.append("Test akkounts fayli mavjud emas yoki o\'chirilgan")
        


    if get_account_from_file():
        print("[+]********** File reading test passed >>>>>>>> working.. **********[+]")
        accept += 1
        sleep(2)
    else:
        print("[+]********** File reading test error >>>>>>>> TestError **********[+]")
        error += 1
        errors.append("Fayldan ma\'lumot o\'qib bo\'lmadi yoki mavjud emas.")
        sleep(2)
        



    if accept == 5:
        print("[+]********** Insta Brute Force >>>>>>>> working 100% **********[+]")
    else:
        print("Warning! Sizda nosozliklar aniqlandi. Dastur to'liq ishlamasligi mumkin💻")
        print(f"[+]********** Nosozliklar soni >>>>>>>> {error} **********[+]")
        sleep(3)
        javob = input("Nosozlik haqida ma'lumot olish Yes[Y]/No[N] ")
        if javob == 'Y':
             for i in range(0, len(errors)):
                 print(f"ID: {i} / {errors[i]}")
                 
             print(f"🛠️Test finished")
             sleep(3)
        else:

            print(f"🛠️Test finished")




main_console()