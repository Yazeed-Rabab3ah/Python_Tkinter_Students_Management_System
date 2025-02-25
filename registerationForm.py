import tkinter as tk
from tkinter import messagebox  
from dataBaseHandler import DataBaseHandler

class RegisterationForm(tk.Frame):
    def __init__(self, parent, refresh_callback):
        super().__init__(parent, padx=10, pady=10)
        self.refresh_callback = refresh_callback

        tk.Label(self, text='Full Name').pack(fill='x')
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(fill='x')

        tk.Label(self, text='Email').pack(fill='x')
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(fill='x')

        tk.Label(self, text='Age').pack(fill='x')
        self.age_spinbox = tk.Spinbox(self, from_=10, to=100)
        self.age_spinbox.pack(fill='x')

        tk.Label(self, text='Gender').pack(fill='x')
        self.gender_var = tk.StringVar(value='')  
        tk.Radiobutton(self, text='Male', variable=self.gender_var, value='Male').pack(anchor='w')
        tk.Radiobutton(self, text='Female', variable=self.gender_var, value='Female').pack(anchor='w')

        self.submit_button = tk.Button(self, text='Submit', command=self.submit_form)
        self.submit_button.pack(fill='x') 

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_spinbox.get()
        gender = self.gender_var.get()

        if name and email and age and gender:
            try:
                DataBaseHandler.insert_student(name, email, int(age), gender)  
                self.refresh_callback()
                messagebox.showinfo('Success', 'Student registered successfully!') 
                 

                # ✅ Reset Form
                self.name_entry.delete(0, 'end')
                self.email_entry.delete(0, 'end')
                self.age_spinbox.delete(0, 'end')
                self.age_spinbox.insert(0, '10')  
                self.gender_var.set('') 

            except Exception as e:
                messagebox.showerror('Error', f'Failed to register student: {e}')
        else:
            messagebox.showwarning('Input Error', 'All fields are required!')  # ✅ Show warning if fields are empty
