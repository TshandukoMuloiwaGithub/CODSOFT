#import tkinter to use in our class
from tkinter import *
from tkinter import messagebox

class ToDoApp(Tk):
    '''
    Class that will be contain all the functions and widgets to our tikinter window
    '''
    
    def __init__(self):
        '''
        first function that gets called when this class is invoked

        '''
        super().__init__()

        self.title('ToDo List App')
        self.config(bg='black')
        self.geometry("220x200")
            

        "This section is for widgets(default ones)" 
        lbl = Label(self,text='ToDo List Management',height=2,bg='black',width=25,fg='white',font=('Arial', 12,'bold'))
        lbl.grid(row=0,column=0)

        #Buttons
        def callnewTodo():
            self.destroy()
            import ToDo_New as ToDo_New
            ToDo_New.start()
        
        btn_new = Button(self, text='New ToDo Items', foreground='darkblue',width=15,command=callnewTodo)
        btn_new.grid(row=1,column=0)

        #
        def callupdateTodo():
            '''
            This function import our update window pop up
            '''
            import ToDo_Update as ToDo_Update

        btn_update = Button(self, text='Update To-Do List', foreground='green',width='15',command=callupdateTodo)
        btn_update.grid(row=2,column=0)

        #
        def calltrackTodo():
            import Todo_Track as Todo_Track
        btn_track = Button(self, text='Track To-Do List', foreground='Red',width=15,command=calltrackTodo)
        btn_track.grid(row=3, column=0)
        
        #
        btn_close = Button(self, text='Quit', bg='black',fg='white', command=quit)

        btn_close.grid(row=6, column=0)

if __name__ =="__main__":
    '''
    This portion starts our program(calls the function that starts off our window or system running)
    '''
    app = ToDoApp()
    app.mainloop()