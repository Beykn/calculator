import tkinter as tk
from tkinter import messagebox

result = 0.0
current_operator = None

def add(a):
    global result
    result += a
    return result

def subtract(a):
    global result
    result -= a
    return result

def multiply(a):
    global result
    result *= a
    return result

def divide(a):
    global result
    if a != 0:
        result /= a
        return result
    else:
        messagebox.showerror("Error", "Division Error: Cannot divide by 0")
        return "ERROR"

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def perform_operation():
    global result, current_operator
    try:
        number = float(entry.get())  
        if current_operator in operations:
            result = operations[current_operator](number) 
            entry.delete(0, tk.END) 
            if result.is_integer():
                entry.insert(0, str(int(result)))
            else:
                entry.insert(0, str(result))
        else:
            messagebox.showerror("Error", "Invalid operation!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def set_operator(operator):
    global current_operator, result
    try:
        
        number = float(entry.get())  
        if result == 0.0:
            result = number  
        current_operator = operator  
        entry.delete(0, tk.END)  
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Sonucu sıfırla
def reset_result():
    global result, current_operator
    result = 0.0
    current_operator = None
    entry.delete(0, tk.END)
    
    
def delete_last_character():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text)-1, tk.END)
        

window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("300x430")


entry = tk.Entry(window, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5, padx=10, pady=10)

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('.', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3),
    ('AC', 6, 0), ('C', 6, 1)
]

for (text, row, col) in buttons:
    if text in '0123456789': 
        tk.Button(window, text=text, font=("Arial", 14), command=lambda t=text: entry.insert(tk.END, t)).grid(
            row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5
        )
    elif text == 'C': 
        tk.Button(window, text=text, font=("Arial", 14), command=delete_last_character).grid(
            row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5
        )
    elif text == 'AC': 
        tk.Button(window, text=text, font=("Arial", 14), command=reset_result).grid(
            row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5
        )
    elif text == '=':  
        tk.Button(window, text=text, font=("Arial", 14), command=perform_operation).grid(
            row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5
        )
    elif text == '.':
        tk.Button(window,text=text,font=("Arial", 14), command=lambda t=text: entry.insert(tk.END, t)).grid(
            row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)
    else: 
        tk.Button(window, text=text, font=("Arial", 14), command=lambda t=text: set_operator(t)).grid(
            row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5
        )

window.mainloop()
