from tkinter import *
import json
import random

'''
This function will have to pop up a window prompting user to continue/Home

'''

track_window = Tk()
track_window.title("Tracking your ToDo List")
track_window.configure(bg='blue')
# track_window.geometry('550x300')
count = 0
incomplete_row = 0
completed_row = 0
column_no = 0
colors = ["red", "green", "blue", "yellow", "orange"]

def increment(count):
    return count  + 1

def call_update():
    track_window.destroy()
    import update_window
    

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


def btn_upload():
    Button(track_window,text='Update',bg='black',foreground='white',command=call_update).grid(row=count,column=column_no,sticky='w')

def upload_check_btns(incomplete_items,completed_items,count):
    '''
    This function takes all the items lists and place the items to there respected places
    '''    
    if len(incomplete_items) > 0:
        #Incomple Items
        flag_colum = True
        incomplete_row = 0
        incomplete_items_lable = Label(track_window,text='ToDo Items:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=0,sticky='w')
        count = increment(count)

        try:

            for i in incomplete_items:
                checkboxOn = IntVar() 
                checkbox = Checkbutton(track_window,text=f'{i}',bg='red',variable=checkboxOn,state='active').grid(row=count,column=0,sticky='w')
                count = increment(count)#keep increasing the count to match the row wwe are on
            else:
                incomplete_row = count
            
        except ValueError:
            print("Failed to Display your Incomplete items")
    

    if len(completed_items)>0:
        #Completed items
        if flag_colum:
            column_no = 2

        count = increment(0)
        complete_label = Label(track_window,text='Done:',bg='black',foreground='gold',font=('Arial',15,'italic')).grid(row=count,column=column_no,sticky='w')
        count = increment(count)

        try:

            for x in completed_items:
                complete_checkbox = Checkbutton(track_window,text=f'{x}',bg=random.choice(colors),state='disabled').grid(row=count,column=column_no,sticky='w')
                count = increment(count)
            else:
                completed_row = count
        except ValueError:
            print("Failed to Display Completed items.")

    # count+=1
    return incomplete_row, completed_row


welcome_label = Label(track_window,text="Track Items",font=('Arial', 15, 'bold')).grid(row=count,column=1,sticky='w',padx=10)
count = increment(count)

incomplete_itmes,completed_items = get_items()
#When count is passed its in now
incomplete_row, completed_row = upload_check_btns(incomplete_itmes,completed_items,count)

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


btn_upload()
track_window.mainloop()

