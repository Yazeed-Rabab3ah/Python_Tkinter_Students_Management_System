import tkinter as tk
import dataBaseHandler
from registerationForm import RegisterationForm

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Students Management System")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_lable = tk.Label(self, text="Students Management System",font=("Helvetica",16))
        title_lable.pack(side='top', fill='x')  
        self.registeration_form = RegisterationForm()
          

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()