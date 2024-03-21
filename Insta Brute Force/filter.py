file_name = input("Fayl nomi: ")
file_name += ".txt"  

recorder_file = "filtered.txt"

try:
  
    filter_text = input("Qidirsh: ")
    
    with open(file_name, "r", encoding="utf-8", errors='replace') as file:
        satirlar = file.readlines()
    

    with open(recorder_file, "w", encoding="utf-8") as cikti:
        for satir in satirlar:
            if filter_text in satir:
                
                double_satr = satir.split(":")
                if len(double_satr) >= 3:
                    second_party = ":".join(double_satr[2:]).strip() 
                    cikti.write(second_party + "\n")
    
    print("Birinchi qism tugatildi.")

   
    base_text = "filtered.txt"

    try:
       
        with open(base_text, "r", encoding="utf-8", errors='replace') as base_text:
            satirlar = base_text.readlines()
        

        dublicates = set()
        filtered = []

        for satir in satirlar:
           
            finished_texts = satir.strip()
            if finished_texts not in dublicates:
                dublicates.add(finished_texts)
                filtered.append(satir)
        
     
        with open("filtered_2.txt", "w", encoding="utf-8") as finish_work:
            finish_work.writelines(filtered)
        
        print("Dublikat satrlar o'chirildi.")
    except FileNotFoundError:
        print("File Not Found.")
    except Exception as e:
        print("Xatolik chiqdi:", e)

except FileNotFoundError:
    print("File Not Found.")
except Exception as e:
    print("Xatolik chiqdi:", e)