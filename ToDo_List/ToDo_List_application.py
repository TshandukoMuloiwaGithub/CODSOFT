from tkinter import *
import tkinter as tk
import json as j
import sys



todo = 'todo.json'

def new_todo():
    '''
    Function to be executed when user clicks on new todo list
    opens another window waiting for it to complete its new items list update
    '''
    try:
        main_window.destroy()
        import create_new_todo_list
        
    except:
        print("Failed to create new todo list")
    

def Update_todo():
    '''
    Function to be executed when user clicks on update todo list
    '''

    main_window.destroy()
    update_to_do_window = tk.Tk()
    update_to_do_window.title("Update ToDo List")

def track_todo():
    '''
    Function to be executed when user clicks on track todo list
    '''
    try:
        main_window.destroy()
        import Track_List
        
    except:
        print("Failed to view todo list for Tracking")

def quit():
    '''
    This function will only destroy the main window
    Executed when the user clicks quit
    '''
    main_window.destroy()
    sys.exit()

def start():
    """
    This function calls all the necessary function for our application
    """
    global main_window
    
    main_window = tk.Tk()
    #Main window instance configurations/properties
    main_window.config(bg='lightblue')
    main_window.title("ToDo Application")
    main_window.geometry("330x210")

    #Header of our main window
    lbl = tk.Label(main_window,text='What would you like to do:',height=2,bg='grey')
    lbl.grid(row=0,column=0)

    #Buttons
    btn_new = tk.Button(main_window, text='Create To-Do List', foreground='darkblue', command=new_todo, padx=10, pady=10, border=3)
    btn_new.grid(row=4,column=3)
    #
    btn_update = tk.Button(main_window, text='Update To-Do List', foreground='green', command=Update_todo, padx=10, pady=10,border=3)
    btn_update.grid(row=5,column=3)
    #
    btn_track = tk.Button(main_window, text='Track To-Do List', foreground='Red', command=track_todo, padx=10, pady=10,border=3)
    btn_track.grid(row=6, column=3)
    #
    btn_close = tk.Button(main_window, text='Quit', bg='Red', command=quit)

    btn_close.grid(row=7, column=3, pady=0, padx=0)
    
    main_window.mainloop()

    return True

while True:
    loop = start()
    print(loop)
    if loop == '':
        print("Goodbye")
        break
