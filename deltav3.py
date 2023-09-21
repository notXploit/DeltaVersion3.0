import tkinter
from tkinter import ttk
import math
from tkinter import messagebox

startmen = tkinter.Tk()
startmen.title('Delta Math Version 3.0 By Yasser Ski')
startmen.geometry('600x300')
startmen.resizable(width=False, height=False)
def info():
    infomen = tkinter.Tk()
    infomen.title('information')
    infomen.geometry('400x300')
    infomen.resizable(width=False,height=False)
    labeltextinfo = 'Are you struggling with math problems involving delta (Δ)? Look no further! Introducing the DeltaMath Calculator, a handy app developed by a self-taught Algerian enthusiast.\nI built this app from scratch, relying on the power of self-education through online resources and the assistance of AI tools like ChatGPT. Its a testament to what passion and determination can achieve.\nWith the DeltaMath Calculator, you can effortlessly solve delta-related math problems. Its user-friendly and designed to simplify your math journey. Give it a try, and I hope you find it helpful! Your support means the world to me.'
    tkinter.Label(infomen,text=labeltextinfo,wraplength=200).pack()
    infomen.mainloop()
contact = ttk.Button(startmen,text='information',command=info)
contact.place(x=260,y=250)
def validate_input(P):
    if P == "" or P == "-":
        return True
    try:
        float(P)
        return True
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return False
label = tkinter.Label(startmen, text="Enter A, B and C Numbers:")
Atext = tkinter.Label(startmen,text='A :')
Btext = tkinter.Label(startmen,text='B :')
Ctext = tkinter.Label(startmen,text='C :')
Atext.place(x=200,y=48)
Btext.place(x=200,y=100)
Ctext.place(x=200,y=164)
label.pack(padx=20, pady=10)
validation = startmen.register(validate_input)
entrya = tkinter.Entry(startmen, validate="key", validatecommand=(validation, "%P"))
entryb = tkinter.Entry(startmen, validate="key", validatecommand=(validation, "%P"))
entryc = tkinter.Entry(startmen, validate="key", validatecommand=(validation, "%P"))
entrya.pack(padx=20, pady=10)
entryb.pack(padx=20,pady=20)
entryc.pack(padx=20,pady=25)


def calculate():
    try:
        input_value1 = float(entrya.get())
        input_value2 = float(entryb.get())
        input_value3 = float(entryc.get())

        result = input_value2 * input_value2 - 4 * input_value1 * input_value3

        messagebox.showinfo("Result",f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in all fields.")

calculate_button = ttk.Button(startmen, text="Calculate Delta", command=calculate)
calculate_button.place(x=60,y=220)
def x1calc():
    try:
        input_value1 = float(entrya.get())
        input_value2 = float(entryb.get())
        input_value3 = float(entryc.get())
        delta = input_value2 * input_value2 - 4 * input_value1 * input_value3
        if delta > 0:
            x1 =  (-input_value2 + math.sqrt(delta)) / (2*input_value1)
            messagebox.showinfo("X1",f"Delta > 0 so X1 is: {x1}")
        elif delta < 0:
            messagebox.showinfo("X1","Delta < 0 No Solutions")
        elif delta == 0:
            x1 = (-input_value2) / (2*input_value1)
            messagebox.showinfo("X1",f"Delta = 0 so X1 is: {x1}")
        else:
            messagebox.showinfo('Unexpected','Unexpected Error')
    except:
        messagebox.showerror('Invalid Input','Please enter valid numbers in all fields.')

x1button = ttk.Button(startmen,text='Calculate X1',command=x1calc)
x1button.place(x=260,y=220)

def x2calc():
    try:
        input_value1 = float(entrya.get())
        input_value2 = float(entryb.get())
        input_value3 = float(entryc.get())
        delta = input_value2 * input_value2 - 4 * input_value1 * input_value3
        if delta > 0:
            x2 = (-input_value2 - math.sqrt(delta)) / (2*input_value1)
            messagebox.showinfo('X2',f'Delta > 0 X2 is: {x2}')
        elif delta < 0:
            messagebox.showinfo('No Solutions','Delta < 0 No Solutions')
        elif delta == 0:
            x2 = (-input_value2) / (2*input_value1)
            messagebox.showinfo('X2',f'Delta = 0 so X2 is: {x2}')
        else:
            messagebox.showerror('Unexpected','Unexpected Error')
    except:
        messagebox.showerror('Invalid Input','Please enter valid numbers in all fields.')

x2button = ttk.Button(startmen,text='Calculate X2',command=x2calc)
x2button.place(x=450,y=220)




startmen.mainloop()