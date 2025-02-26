import tkinter as tk
import dataBaseHandler
from registerationForm import RegisterationForm
from student_listing import StudentListing

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Students Management System")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_lable = tk.Label(self, text="EduMate",font=("Helvetica",16))
        title_lable.pack(side='top', fill='x')  
        self.registeration_form = RegisterationForm(self, self.refresh_listing)
        self.registeration_form.pack(side='left', fill='y', padx=10, pady=10)

        self.student_listing = StudentListing(self)
        self.student_listing.pack(side='right', fill='both', expand=True, padx=10, pady=10)

    def refresh_listing(self):
        self.student_listing.load_students()      

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()