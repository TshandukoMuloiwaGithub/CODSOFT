import tkinter as tk
import manipulation.input_handling as handling
import manipulation.messages as msgs

import json
import random

'''
This function will have to pop up a window prompting user to continue/Home

'''

update_window = tk.Tk()
update_window.title("Update ToDo List")
update_window.configure(bg='blue')
# update_window.geometry('550x300')
count = 0


def increment(count):
    '''
    This function takes in an integer increment it
    Returns your integer incremented
    '''
    return count  + 1


def save_change(json_data, clicked):
    '''
    This function checks which of the boxes were click
    '''
    final_json_data = []
    for x in json_data:
        title = x['title']
        item_no = x['item_no']
        status = x['status']

        if title in clicked:
            if x['status'] == 0:
                status = 1
                update_dict = {
                    'title' : f'{title}',
                    'item_no' : f'{item_no}',
                    'status' : status
                }
                final_json_data.append(update_dict)
            
        else:
            final_json_data.append(x)

    return final_json_data

def call_update():
    ''
    
    final_json_data = []
    print(checkboxes_title)
    print(checkboxes_state)
    update_window.destroy()
    clicked = [checkboxes_title[index] for index,clicked in enumerate(checkboxes_state) if clicked.get()]


    if len(clicked) > 0:
        for Items_count,i in enumerate(clicked):
            print(f'Item_no {Items_count}:',i)
            
        else:
            try:
                Items_count +=1 
                msgs.custom_message_box('Congrats',f'You marked {Items_count} items as done.','green')
            
            except UnboundLocalError as ul:
                print('Error:',str(ul))

            finally:
                handling.restart()
    else:
        'If the are no changes made display error msg'
        msgs.custom_message_box('Empty Error',f'Sorry, you need changes to save changes','red')
    
    handling.restart()
     
def get_items():
    '''
    This function get all the items from json file
    returning completed and incompleted items
    '''
    items = []
    with open('todo.json','r') as read_file:
        items = json.load(read_file)

    incomplete = []
    complete = []
    #Getting item tittles
    
    for item in items:
        if item['status'] == 0:
            #If status reads 0 that means the item has not been completed
            incomplete.append(item['title'])
        else:
            complete.append(item['title'])
    else:
        return incomplete,complete

def create_checkboxes(open_tasks,closed_tasks,count):
    '''
    This function uses two list to create two different columns
    '''
    global checkboxes_title
    global checkboxes_state
    global update_items

    update_items = []
    checkboxes_title = []
    checkboxes_state = []

    incomplete_row = 0
    completed_row = 0
    flag_colum = False

    if (len(open_tasks) > 0): 
        'If thereare any open task'

        #Flag colum taken
        flag_colum = True

        incomplete_items_lable = tk.Label(update_window,text='ToDo Items:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=0,sticky='w')
        count = increment(count)

        for i, item in enumerate(open_tasks):
            
            #BooleanVar
            var = tk.BooleanVar()
            cbtn = tk.Checkbutton(update_window, text=item, variable=var, bg='red', state='normal')
            cbtn.grid(row=count,column=0,sticky='w')
            
            #Save after each task checkbtn is created
            checkboxes_title.append(item)
            checkboxes_state.append(var)
            
            #Increment count to place the next btn at a diff pos 
            count = increment(count)

        else:
            'Assign the next pos to incomplete row'
            incomplete_row = count
    

    if len(closed_tasks)>0:
        'If closed tasks exist'
        count = increment(0)#Resetting row for hearder 
        
        if flag_colum:
            column_no = 1
        
        complete_label = tk.Label(update_window,text='Done:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=column_no,sticky='w')
        count = increment(count)

        for i, item in enumerate(closed_tasks):
            #BooleanVar
            var = tk.BooleanVar()
            cbtn = tk.Checkbutton(update_window, text=item, variable=var, bg='black',font=('A'), state='disabled')
            cbtn.grid(row=count,column=column_no,sticky=tk.W)
            
            checkboxes_title.append(item)
            checkboxes_state.append(var)
            count = increment(count)

        else:
            completed_row = count

        
    return incomplete_row, completed_row


def btn_upload(column_no=''):
    '''
    Function takes in an integer
    Function parameter decides what and column the save change btn should be
    '''
    
    try:
        tk.Button(update_window,text='Save Change',bg='black',foreground='white',command=call_update).grid(row=count,column='0',sticky='w')
    
    except ValueError as ve:
        column_no = int(column_no)
        btn_upload(column_no)


def upload_check_btns(incomplete_items,completed_items,count):
    '''
    This function takes all the items lists and place the items to there respected places
    '''
        
    return create_checkboxes(incomplete_items,completed_items,count)

welcome_label = tk.Label(update_window,text="Update Items",font=('Arial', 15, 'bold')).grid(row=count,column=0,sticky='w',padx=40)
count = increment(count)
incomplete_items,completed_items = get_items()

#When count is passed its in now
incomplete_row, completed_row = upload_check_btns(incomplete_items,completed_items,count)

#Deciding which column`s count
if incomplete_row > completed_row:
    #if incompleted rows are more the we use it as the count
    count = incomplete_row

elif incomplete_row < completed_row:
    #if ompleted rows are more the we use it as the count
    count = completed_row
else:
    #count can me either we will use incompleted rows as count
    count = incomplete_row

def begin():
    btn_upload('0')
    update_window.mainloop()

begin()