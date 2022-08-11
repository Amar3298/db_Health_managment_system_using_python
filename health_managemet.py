"""
Health Management 
Author:- Amar Raut
email:- rautamar2001@gmail.com
Tracks our daily exercise and diet
"""
def getDate():
    import datetime
    return datetime.datetime.now()

def display_existing_user():
    with open("./text_files/user.txt") as f:
        list_user = f.readlines()
        for user in list_user:
            print(list_user.index(user),user[:-1])
    return list_user

def add_user():
    name_user = input("Enter the name of user:- ")
    name_user = name_user.capitalize()
    with open("./text_files/user.txt","a") as f:
        f.write(f"\n{name_user}")
global mode;
mode = "a"
def user_input_for_user_ui():
    new_user = input("Do you want to add user: ")
    new_user = new_user.upper()
    if(new_user=="Y"):
        add_user()
    user_list_wirte  = display_existing_user()
    user_input_for_operation = int(input("Enter the id no for operation:- "))
    operation_to_perform_r_w = input("Enter operation read/write(R/W): ")
    operation_to_perform_r_w = operation_to_perform_r_w.upper()
    exercise_diet = input("Exercise|Diet(E/D): ")
    exercise_diet = exercise_diet.upper()
    operation_to_pass = "exercise"
    if(exercise_diet=="E"):
        operation_to_pass = "exercise"
    elif(exercise_diet=="D"):
        operation_to_pass = "diet"
    chech_var_name = f"{user_list_wirte[user_input_for_operation][:-1]}_{operation_to_pass}.txt\n"
    check_file_name(chech_var_name)
    if(operation_to_perform_r_w=="W"):
        write_data_file(user_list_wirte[user_input_for_operation][:-1],operation_to_pass)
    elif(operation_to_perform_r_w=="R"):
        reading_data_file(user_list_wirte[user_input_for_operation][:-1],operation_to_pass)
        

def write_data_file(name_user,operation_e_w_db):
    write_data = input("Enter the information: ")
    with open(f"./text_files/{name_user}_{operation_e_w_db}.txt",f"{mode}") as f:
        f.write(f"[{getDate()}]:{write_data}\n")

def reading_data_file(name_user,operation_e_w_db):
    with open(f"./text_files/{name_user}_{operation_e_w_db}.txt") as f:
        print(f.read())

    
def check_file_name(check_C):
    list_db = []
    f = open("./text_files/files_present.txt")
    text_list = f.readlines()
    for i in range(len(text_list)):
        list_db.append(text_list[i])
    if(check_C not in text_list):                     
        global mode;
        mode = "w"
    f.close()

    with open("./text_files/files_present.txt","a") as f:
        if check_C not in list_db:
            f.write(check_C)                        


while True:
    user_input_for_user_ui() 
    check_break = input("Do you want to do any operations(Y/N): ")
    check_break = check_break.upper()
    if(check_break=="N"):
        break
