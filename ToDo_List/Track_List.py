import tkinter as tk
# from tkinter import *
import sys
import json
import random

'''
This function will have to pop up a window prompting user to continue/Home

'''
track_window = tk.Tk()
track_window.title("Tracking your ToDo List")
track_window.configure(bg='lightblue')
# track_window.geometry('240x480')


#for checkbutton
btn_name = "check_"
todo_checkbtn_dict = {}
complete_checkbtn_dict = {}
var = tk.IntVar()

welcome_label = tk.Label(track_window,text="Tracking To-Do List",fg='darkblue',font=('Arial', 15, 'bold'),bg='darkgrey').grid(row=0,column=0,sticky='w')
#
line_label = tk.Label(track_window,text="-"*44,font=('Arial', 13, 'bold'),bg='lightblue').grid(row=1,column=0,sticky='w')

# Todo_label = tk.Label(track_window,text="To-Do Items:",font=('Arial', 15, 'bold')).grid(row=2,column=0,sticky='w')
"Need to do calculation on where to insert conpleted tasks"
# Completed_label = tk.Label(track_window,text="Completed Items",font=('Arial', 15, 'bold')).grid(row=2,column=0,sticky='w')

def insert_check_btns(todo_items,completed_items,count):
    #If todo items are there
        if len(todo_items) > 0:
            count = todo_items_checkbuttons(todo_items,count)
            
        else:
            no_todo_label = tk.Label(text='No outstanding tasks',bg='red',font=('Arial', 12, 'bold')).grid(row=count,column=1)
        # pass
        
        
        #If completed items are there
        if len(completed_items) > 0:
            countt = completed_items_checkbuttons(completed_items,count)
        else:
            no_completed_label = tk.Label(text='There are no completed tasks',bg='red',font=('Arial', 12, 'bold')).grid(row=count,column=1)

def todo_items_checkbuttons(todo_items,count):
    '''
    This function inserts checkbuttons onto our completed tasks column
    '''
    #Creating check buttons for each completed task and print label before checkbuttons
    tk.Label(track_window,text="To-Do Items:",font=('Arial', 15, 'bold'),bg='red').grid(row=2,column=0,sticky='w')
    
    for i in todo_items:
        'Iterating through list of tasks that are not completed'
        title = i['title']
        todo_checkbtn_dict[btn_name+str(i['item_no'])] = tk.Checkbutton(track_window,text=f'{title}',foreground='red',bg='darkblue').grid(row=count,column=0,sticky='w')
        count +=1
        
    else:
        #when done iterating through completed items reset count to 2
        'return 2 into count resetting it'
        return count + 2

def completed_items_checkbuttons(completed_items,count):
    '''
    This function inserts checkbuttons onto our completed tasks column
    '''
    #Creating check buttons for each completed task adn print label before checkbuttons
    tk.Label(track_window,text="-"*44,font=('Arial', 13, 'bold'),bg='lightblue').grid(row=count-1,column=0,sticky='w')
    tk.Label(track_window,text="Completed Items:",font=('Arial', 15, 'bold'),bg='green').grid(row=count,column=0,sticky='w')
    
    for i in completed_items:
        title = i['title']
        var = tk.IntVar(value=0)
        complete_checkbtn_dict[btn_name+str(i['item_no'])] =  tk.Checkbutton(track_window,text=f'{title}',font=('Arial',12, 'bold'),fg='green',bg='lightblue',state='disable',variable=var,onvalue=1,offvalue=0).grid(row=count+1,column=0,sticky='w')
        count +=1
        
    else:
        #when done iterating through completed items reset count to 2
        'return 2 into count resetting it'
        count = count
        return count
    

def restart():
    '''
    This function restarts the program
    '''
    import ToDo_List_application

def quit_func():
    '''
    This function executes when the user specifies thast they want to quit the application
    '''
    sys.exit()


def get_items():
    '''
    This function get all the items from json file
    '''
    items = []
    with open('todo.json','r') as read_file:
        items = json.load(read_file)

    completed_items = []
    todo_items = []
    count = 4

    #Getting item tittles
    for item in items:
        #Iterating through list of items
        

        if item['status'] == 1:
            'if status of item is 1(done), then append task on completed list'
            completed_items.append(item)
        
        else:
            'items whos status is not done(not 1 but 0)'
            todo_items.append(item)



    #Inserting checkbtns
    if len(completed_items) != 0 or len(todo_items) != 0:
        'if list contains elements then completed tasks are in our json file'
        #calling function to populate the Tracking window
        try:
            track_window.destroy()
            insert_check_btns(todo_items,completed_items,count)
        except ValueError:
            
            error_window = tk.Tk()
            
            error_window.title('Error Message')
            error_window.configure(bg='red',width=50)

            tk.Label(text='Return Home or Quit')
            homebtn = tk.Button(text='Home',command=restart).grid(row=count,column=3)
            quit_btn = tk.Button(text='Quit',command=quit_func).grid(row=count,column=4)
            error_window.mainloop()
            "Try to populate window"
    
get_items()
track_window.mainloop()

