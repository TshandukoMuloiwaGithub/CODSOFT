from tkinter import *
import json
import sys
from manipulation.input_handling import *
# import time

class new_window_App(Tk):

    def __init__(self):
        super().__init__()
        open_item_limit = 7
        global user_items
        def pop_window(existing_items):
            '''
            This function returns a boolean
            return TRue when window should be popped
            '''
            pop = True
            count = 0
            for x in existing_items:
                if x['status'] == 0:
                    'if ITEM status is open'
                    count +=1
                
            if count >= open_item_limit:
                'setting pop to false if count found eightor more open items'
                pop = False
            
            return pop
        
        def user_new_list_input(user_items):
            '''
            This function should write user`s new todo list into a data file
            '''
           
            # items ={}
            items_list = []
           
            #Reading from json file to get existing items
            try:
                items_list = read_from_json()

            except:
                print("Failed to read existing tasks")
                items_list = []

            for item in user_items:
                item_no = 1
                try:
                    item_no = int(items_list[-1]['item_no']) +1
                except IndexError:
                    item_no = item_no

                items = {
                    'title': f'{item}',
                    'item_no': item_no,
                    'status': 0
                }
                items_list.append(items)
                # items = {}
            
            
            #Write new list to json
            try:
                write_to_json(items_list)
                status_label.config(text="Successfully Created New List",bg='green')
                # time.sleep(2)
                status_label.config(text="Redirecting you to the main window...",bg='green')
                # time.sleep(3)
                self.destroy()

            except TclError as t:
                print ("Error erro:",t)
                # status_label.config(text="Failed to create New List",bg='red')

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
        


        #Before setting up what to put on our window lets decide if it should even pop up our new items window
        print("First piece to run")
        existing_items = read_from_json()
        
        if not pop_window(existing_items):
            'if pop window is false, dont pop window'
            cannot_pop_window()
            
            #Execute scrit to restart program
            restart()
            sys.exit()

        # Create the main window
        self.title("New Todo List Items")
        # self.geometry('210x200')
        self.configure(bg='black')

        #Create Label alerting format
        format_text = Label(self,text="NB: Seperate items by comma/nextline.",fg='black',bg='red',font=('arial',8,'italic','bold'))
        limit_text = Label(self,text='Open items limit: 7',bg='green',fg='white',underline=-1,font=('arial',9,'bold'))
        limit_text.grid(row=1,sticky='w')
        format_text.grid(row=6)

        #Create label for instruction
        instruction_text = Label(self,text="List Items:")
        instruction_text.grid(row=2,column=0)

        # Create and place the entry widget (for user input)
        text = Text(self,width=28,height=7)
        text.grid(row=3,sticky='w')
        
        def get_open_items_no(existing):
            '''
            This function takes all existing tasks
            return total number of items with open status (0)
            '''
            open_items = []
            for x in existing:
                if x['status'] == 0:
                    open_items.append(x)
            else:
                return open_items,len(open_items)

          
        def user_text():
            '''
            This function takes what the user entered
            '''
            from manipulation import input_handling
            #Converting user input into list
            user_items = input_handling.break_it_down(text.get('1.0',END))
            
            print(user_items)
            new_items_length = len(user_items)
            open_existing_no = 0 
            for x in existing_items:
                if x['status'] == 0:
                    open_existing_no += 1

            else:
                '''
                Done counting existing open tasks
                '''
                #checking open itrm limit
                if input_handling.limit_exceeded(open_existing_no,new_items_length):
                    'if limit exceeded'
                    restart()
                else:
                    'When limit execeed is not reached'
                    user_new_list_input(user_items)
                    
                    restart()

        #Save change btn
        button = Button(self, text="Save Items", bg='green',command=user_text)
        button.grid(row=5)

        # Create and place the label widget for displaying output
        status_label = Label(self,bg='black',fg='black')
        status_label.grid(row=4)

def start():
    '''
    This function call the new window class and starts the mainloop
    '''
    new_app = new_window_App()
    new_app.mainloop()

