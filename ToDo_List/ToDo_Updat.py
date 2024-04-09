import tkinter as tk

def record_checked_items():
    '''
    Function records the check btns that were clicked
    '''
    checked_items = ''

def insert_checkboxes(existing_items):
    '''
    This function creates the check btns from a list of items
    '''
    global checkboxes
    checkboxes = []

    for i, x in enumerate(existing_items):
        var = tk.BooleanVar()
        chk = tk.Checkbutton('',text=x,variable=var)
        chk.grid(row=i, column=0,sticky=tk.W)

