import tkinter as tk
import manipulation.input_handling as handling
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

# global column_no
# column_no = 0
colors = ["red", "green", "blue", "yellow", "orange"]

def increment(count):
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
    clicked = [checkboxes_title[index] for index,clicked in enumerate(checkboxes_state) if clicked.get()]

    
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
    # global flag_colum
    checkboxes_title = []
    checkboxes_state = []
    incomplete_row = 0
    completed_row = 0
    flag_colum = False

    if (len(open_tasks) > 0): #If thereare open tasks
        flag_colum = True
        print('ey',count)
        incomplete_items_lable = tk.Label(update_window,text='ToDo Items:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=0,sticky='w')
        count = increment(count)
        flag_colum = True
        print('There is an open task, count:',count)
        for i, item in enumerate(open_tasks):
            #BooleanVar
            print(f'count for checkbtn `{item}`:',count)
            var = tk.BooleanVar()
            cbtn = tk.Checkbutton(update_window, text=item, variable=var, bg='red', state='normal')
            cbtn.grid(row=count,column=0,sticky='w')
            #lat var will contain title and state
            checkboxes_title.append(item)
            checkboxes_state.append(var)
            print('count before increment:',str(count))
            count = increment(count)
            print('count after increment:',str(count))

        else:
            incomplete_row = count
    

    if len(closed_tasks)>0:
        #Completed items
        count = increment(0)#Resetting row for hearder 
        if flag_colum:
            column_no = 1
        complete_label = tk.Label(update_window,text='Done:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=column_no,sticky='w')
        count = increment(count)

        for i, item in enumerate(closed_tasks):
            #BooleanVar
            print('op1:',count)
            print('op2:',i)
            var = tk.BooleanVar()
            cbtn = tk.Checkbutton(update_window, text=item, variable=var, bg='green', state='disabled')
            cbtn.grid(row=count,column=column_no,sticky=tk.W)
            checkboxes_title.append(item)
            checkboxes_state.append(var)
            count = increment(count)

        else:
            completed_row = count

        
    return incomplete_row, completed_row


def btn_upload(column_no):
    tk.Button(update_window,text='Save Change',bg='black',foreground='white',command=call_update).grid(row=count,column=column_no,sticky='w')


def upload_check_btns(incomplete_items,completed_items,count):
    '''
    This function takes all the items lists and place the items to there respected places
    '''
    print("one her:",count)
    # welcome = tk.Label(text='Update Tasks',bg='grey',fg='black', font=('arial',12,'bold')).grid(row=count,column=0,padx=10,sticky='e')
    # count = increment(count)

        
    return create_checkboxes(incomplete_items,completed_items,count)

    # if len(completed_items)>0:
    #     #Completed items
    #     print('flag it',flag_colum)
    #     if flag_colum:
    #         column_no = 1
    #         print('now:',column_no)
    #     print('again:',count)
    #     count = increment(0)
    #     complete_label = tk.Label(update_window,text='Done:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=column_no,sticky='w')
    #     count = increment(count)

    #     try:
    #         print('afte done label',str(count))
    #         for x in completed_items:
    #             complete_checkbox = tk.Checkbutton(update_window,text=f'{x}',bg='green',state='disabled').grid(row=count,column=column_no,sticky='w')
    #             count = increment(count)
    #         else:
    #             completed_row = count
    #     except ValueError:
    #         print("Failed to Display Completed items.")

    # # count+=1
    # return incomplete_row, completed_row

print('welcome count', count)
column_no = 0
welcome_label = tk.Label(update_window,text="Update Items",font=('Arial', 15, 'bold')).grid(row=count,column=0,sticky='w',padx=40)
count = increment(count)
print('After welcome',str(count))
incomplete_items,completed_items = get_items()

#When count is passed its in now
incomplete_row, completed_row = upload_check_btns(incomplete_items,completed_items,count)
# incomplete_row, completed_row = create_checkboxes(incomplete_items,completed_items,count)


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
    btn_upload(column_no)
    update_window.mainloop()

begin()