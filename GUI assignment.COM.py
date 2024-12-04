import tkinter as tk
from tkinter import messagebox


def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


root = tk.Tk()
root.title("Simple Calculator")


entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)


add_button = tk.Button(root, text="+", command=add)
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.grid(row=1, column=2, padx=5, pady=5)

divide_button = tk.Button(root, text="/", command=divide)
divide_button.grid(row=1, column=3, padx=5, pady=5)


result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)


root.mainloop()





































