import tkinter as tk

# Function to update expression in the entry
def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Function to evaluate the final expression
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Main GUI window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field
entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, insertwidth=4, bg="lightyellow", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0),  ('8', 1, 1),  ('9', 1, 2),  ('/', 1, 3),
    ('4', 2, 0),  ('5', 2, 1),  ('6', 2, 2),  ('*', 2, 3),
    ('1', 3, 0),  ('2', 3, 1),  ('3', 3, 2),  ('-', 3, 3),
    ('0', 4, 0),  ('.', 4, 1),  ('=', 4, 2),  ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="lightgreen",
                  command=equal).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=85, pady=20, font=('Arial', 14), bg="tomato",
                  command=clear).grid(row=row, column=col, columnspan=3)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="lightblue",
                  command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()


