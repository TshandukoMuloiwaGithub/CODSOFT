import tkinter as tk
import json
import random

'''
This function will have to pop up a window prompting user to continue/Home

'''
track_window = tk.Tk()
track_window.title("Tracking your ToDo List")
track_window.configure(bg='lightblue')
track_window.geometry('300x300')

welcome_label = tk.Label(track_window,text="Below are your todo items:",font=('Arial', 15, 'bold')).grid(row=0,column=0)

def get_items():
    '''
    This function get all the items from json file
    '''
    items = []
    with open('todo.json','r') as read_file:
        items = json.load(read_file)

    items_topic = []
    items_state = []
    count = 1
    #Getting item tittles
    for item in items:
        if item['status'] == 0:
            items_topic.append(item['item'])
    #Getting item status
    for state in items:
        if item['status'] == 0:
            items_state.append(item['status'])

    colors = ["red", "green", "blue", "yellow", "orange"]
    for i in items_topic:
        color = random.choice(colors)
        checkbox = tk.Checkbutton(track_window,text=f'{i}',bg=random.choice(colors)).grid(row=count,column=0)
        
        count +=1

    
get_items()
track_window.mainloop()

