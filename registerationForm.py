import tkinter as tk
from tkinter import messagebox  
from dataBaseHandler import DataBaseHandler
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        self.visualize_btn = tk.Button(self, text="Visualize Gender Distribution", command=self.visualize_gender_distribution)
        self.visualize_btn.pack(pady=10)

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
                 

                
                self.name_entry.delete(0, 'end')
                self.email_entry.delete(0, 'end')
                self.age_spinbox.delete(0, 'end')
                self.age_spinbox.insert(0, '10')  
                self.gender_var.set('') 

            except Exception as e:
                messagebox.showerror('Error', f'Failed to register student: {e}')
        else:
            messagebox.showwarning('Input Error', 'All fields are required!')   

    def visualize_gender_distribution(self):
        """Fetch gender data and visualize it using a pie chart."""
        male_count, female_count = DataBaseHandler.get_gender_distribution()

        if male_count is None or female_count is None:
            messagebox.showerror("Error", "Failed to fetch gender data from the database.")
            return

        if male_count == 0 and female_count == 0:
            messagebox.showwarning("No Data", "No students registered yet.")
            return

        
        chart_window = tk.Toplevel(self)
        chart_window.title("Gender Distribution")
        chart_window.geometry("500x400")

        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        
        labels = ['Male', 'Female']
        sizes = [male_count, female_count]
        colors = ['blue', 'pink']

        
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title("Student Gender Distribution")

        
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.get_tk_widget().pack()
        canvas.draw()
