from tkinter import *
import tkinter as tk
import json as j

main_window = tk.Tk()
todo = 'todo.json'
#Creating instance of TK main window
def new_todo_list(items):
    '''
    This function takes given items
    returns the items to be saved on json file
    '''
    with open(todo,'w') as j_file:
        j.dump(j_file,items)
    
def new_todo():
    '''
    Function to be executed when user clicks on new todo list
    '''

    main_window.destroy()
    new_to_do_window = tk.Tk()
    new_to_do_window.title("Create ToDo List")
    new_to_do_window.geometry("300x200")
    
    
    tk.Label(new_to_do_window ,text="Seperate items by comma or nextline",bg='red').grid(row=0,column=0)
    tk.Label(new_to_do_window,text="Enter Todo List items:").grid(row=1,column=0)
    

    #Saving user items ---- Continue
    todo_items = tk.Text(new_to_do_window,width=30,height=5).grid(row=2,column=0)
    
    tk.Button(new_to_do_window,text='Create List',bg='green',command='').grid(row=3,column=0,padx=0)    

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
    main_window.destroy()
    track_to_do_window = tk.Tk()
    track_to_do_window.title("Track ToDo List")

def quit():
    '''
    This function will only destroy the main window
    Executed when the user clicks quit
    '''
    main_window.destroy()

def start():
    """
    This function calls all the necessary function for our application
    """
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

if __name__ == "__main__":
    start()