from tkinter import *

class calculatorApp(Tk):
    def __init__(self):
        super().__init__()

        window_width = "300"
        window_height = "200"

        self.title('Mathlator App')
        self.geometry(window_width+'x'+window_height)
        self.configure(bg='grey')

        user_query = Text(height=2,width=8)
        label1 = Label(text="Enter your math problem:", background='red')
        label1.grid(row=0,column=0,sticky='w')
        user_query.grid(row=1,column=0,sticky='nswe')
        def calculate():
            print('What to calculate:',user_query.get('1.0',END))
        btn = Button(text='Solve',bg='green',command=calculate).grid(row=4,column=0,sticky='w')
if __name__ == "__main__":
    'call class'
    app = calculatorApp()
    app.mainloop()