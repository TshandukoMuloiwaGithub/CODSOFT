import tkinter as tk
import json
import os
import time
from input_manipulation import new_list_input

def user_new_list_input():
    '''
    This function should write user`s new todo list into a data file
    '''
    user_input = entry.get()

    #Get entered items as a list
    user_input_as_list = new_list_input.break_it_down(user_input)
    items ={}
    items_list = []

    #Reading from json file to get existing items
    try:
        items_list = read_from_json()
    except:
        print("Failed to read existing tasks")
        items_list = []

    for item in user_input_as_list:
        items = {
            'item': f'{item}',
            'status': 0
        }
        items_list.append(items)
        items = {}
    
    
    #Write new list to json
    try:
        write_to_json(items_list)
        status_label.config(text="Successfully Created New List",bg='green')
        time.sleep(2)
        status_label.config(text="Redirecting you to the main window...",bg='green')
        time.sleep(3)
        root.destroy()

    except:
        status_label.config(text="Failed to create New List",bg='red')

    
def read_from_json():
    '''
    Read json content to avoid overriding the existing info
    '''
    with open('todo.json','r') as json_file:
        ''
        items_list = json.load(json_file)

    return  items_list

#Try to write or staore entered into a data file
def write_to_json(items_list):
    '''
    This function takes the items given by the user and writes them into ajson file
    '''
    try:
        with open("todo.json",'w') as json_file:
        #appending a new dictionary to the list of dictionaries
        
            json.dump(items_list,json_file,indent=2)
            status_label.config(text='Done deal')
            
    except FileNotFoundError as e:
        print('An error occured.')
        print('Error message:',str(e))


# Create the main window
root = tk.Tk()
root.title("New Todo List")
root.geometry('250x250')
root.configure(bg='black')

#Create Label alerting format
format_text = tk.Label(root,text="Seperate items by comma.",bg='red')
format_text.pack()

#Create label for instruction
instruction_text = tk.Label(root,text="List Items:")
instruction_text.pack()

# Create and place the entry widget (for user input)
entry = tk.Entry(root, width=30)
entry.pack(padx=0,pady=20)


# Create and place the button widget
button = tk.Button(root, text="Create List", bg='green',command=user_new_list_input)
button.pack(padx=1)

# Create and place the label widget for displaying output
status_label = tk.Label(root,text='')
status_label.pack(pady=10)

# Start the main event loop
root.mainloop()
