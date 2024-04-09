from . import messages
import json
import string
import os
import sys
import re
import subprocess
current_directory = os.path.dirname(os.path.abspath(__file__))
script_name = 'restart_todo.sh'
open_item_limit = 7
special_characters = re.compile('[@_!$%^&*<>?/\|}{~:]#''')

def restart():
    '''
    When called this function executes a script restarting our application
    '''
    
    target_file = os.getcwd()+"/ToDo_List/ToDoApplication.py"
    #Allows what to use to call for target file    
    subprocess.call(['python3', target_file])

def read_json():
    ''''
    This function reads all the existing data into a list of dicts
    REturn dictionary list
    '''
    items = []
    with open('todo.json','r') as read_file:
            items = json.load(read_file)

    return items

def write_to_json(items_list,status_label=''):
    '''
    This function takes the items given by the user and writes them into ajson file
    '''
    print('was here')
    try:
        with open("todo.json",'w') as json_file:
        #appending a new dictionary to the list of dictionaries       
            json.dump(items_list,json_file,indent=2)
                            
    except FileNotFoundError as e:
        print('An error occured.')
        print('Error message:',str(e))


def break_it_down(user_string):
    """
    This function break down user new string into a list of items
    returns a list of items
    """

    #Getting rid of nextlines(replacing nextlines for commas)
    user_string = user_string.replace('\n',',')
    clean_items = []

    #splitting user input into list avoiding empty strings as well
    user_as_list = [x.strip() for x in user_string.split(',') if x!='']

    #Limitng user`s input from using special characters 
    user_as_list = [x.strip() for x in user_as_list if not len(x) == 0 and not x in ['!#$^%&*_+?:}{><~!|\/''']]
    
    'Probably redundant brb'
    user_as_list = list_empty_element_pop([x.strip() for x in user_as_list if not special_characters.search(x)])

    #Eliminating unwanted characters
    clean_items = user_as_list
    return clean_items
    
def cannot_pop_window():
    
    messages.custom_message_box('Open tasks limit','Open Task Limit Reached','red')

def list_empty_element_pop(lst):
    '''
    Delete emplete elements in list returning a list
    '''
    new_lst = []
    empty=''
    print('Before the list_empty_element_pop:\n',lst)
    for t,x in enumerate(lst):

        if special_characters.search(x) and lst[t] == empty:
            'then they are aligned'
            continue
        else:
            new_lst.append(x)
    else:
        return new_lst

def limit_exceeded(existing_length,new_items_length):
    '''
    This function check if lenghth of open items with be exceeded 
    return TRue if exceeded
    '''
    
    if existing_length + new_items_length > open_item_limit:
        'if there is room for more items'
        messages.custom_message_box('Exceeding limit',f'Room left: {open_item_limit - existing_length}','grey')
        return True
    elif existing_length + new_items_length == open_item_limit:
        messages.custom_message_box('limit reached',"Open ToDo items limit reached!!!",'green')
        return False
    else:
        new_total_open = existing_length + new_items_length
        messages.custom_message_box('New ToDo Items',f'Open Task room left: {open_item_limit - new_total_open}','green')
        return False

