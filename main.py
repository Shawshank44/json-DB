import json
from os import name

filename = "data.json"

def Choices():
    print('K I N G S')
    print('Data Management System')
    print('(1) View data')
    print('(2) Add data')
    print('(3) Delete data')
    print('(4) Edit data')
    print('(5) Exit')


def View_data():
    with open(filename, 'r') as f :
        temp = json.load(f)
        i = 0
        for entry in temp:
            name = entry['name']
            begin = entry['begin']
            end = entry['end']
            print(f"Index Number : {i}")
            print(f"name of king : {name}")
            print(f"name of king : {begin}")
            print(f"name of king : {end}")
            i = i+1


def Delete_data():
    View_data()
    new_data = []
    with open(filename, 'r') as f :
        temp = json.load(f)
        data_length = len(temp)-1
    print("which Index number u want actually delete")
    delete_option = input(f'Select a number 0 to {data_length} : ')
    i = 0 
    for entry in temp:
        if i == int(delete_option): 
            pass
            i= i+1
        else:
            new_data.append(entry)
            i= i+1    
    with open (filename , 'w') as f:
        json.dump(new_data, f , indent=4 )


def Edit_data():
    View_data()
    new_data = []
    with open(filename, 'r') as f :
        temp = json.load(f)
        data_length = len(temp)-1
    print("which Index number u want actually delete")
    edit_option = input(f'Select a number 0 to {data_length} : ')
    i = 0 
    for entry in temp:
        if i == int(edit_option): 
            name = entry['name']
            begin = entry['begin']
            end = entry['end']
            print(f" Current name of king : {name}")
            name = input('What is the new name : ')
            print(f" Current reign of king : {begin}")
            begin = input('What is the new begin : ')
            print(f" Current name of king : {end}")
            end  = input('What is the new end : ')
            new_data.append({
                'name' : name,
                'begin': begin,
                'end': end
            })
            i= i+1
        else:
            new_data.append(entry)
            i= i+1    
    with open (filename , 'w') as f:
        json.dump(new_data, f , indent=4)





def Add_data():
    item_data = {}
    with open (filename , 'r') as f:
        temp = json.load(f)
    item_data['name'] = input("Enter the King : ")
    item_data['begin'] = input("Enter the Reign : ")
    item_data['end']  = input("Enter the data :  ")
    temp.append(item_data)
    with open (filename , 'w') as f:
        json.dump(temp, f , indent=4)   



while True:
    Choices()
    choices = input('Enter the choice number : ')
    if choices == '1':
        View_data()
    elif choices == '2':
        Add_data()
    elif choices == '3':
        Delete_data()
    elif choices == '4':
        Edit_data()
    elif choices == '5':
        print('Successfully Exited') 
        break
    