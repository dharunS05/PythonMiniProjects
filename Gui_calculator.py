#-------------------------------
# Tkinter based calculator
#-------------------------------

#import tkinter library
import tkinter as tk

#create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x440")
root.resizable(False,False)

# -------------------------------
# Step 1: Create an Entry widget
# -------------------------------

entry = tk.Entry(root,width=18,font=('Arial',22),borderwidth=3,relief='solid',justify='right')
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

# -------------------------------
# Step 2: Define button functions
# -------------------------------
def click_button(value):
    entry.insert(tk.END,value)

def clear_entry():
    entry.delete(0,tk.END)

def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(tk.END,'Error')

# -------------------------------
# Keyboard support function
# -------------------------------

def key_event(event):
    key = event.keysym

    if key in "0123456789":
        click_button(key)
    elif key in ("plus", "minus", "asterisk", "slash", "period"):
        # Convert operator names to symbols
        mapping = {
            "plus": "+",
            "minus": "-",
            "asterisk": "*",
            "slash": "/",
            "period": "."
        }
        click_button(mapping[key])
    elif key == 'Return':
        calculate()
    elif key == "BackSpace":
        backspace()
    elif key == 'Escape':
        clear_entry()

root.bind('<Key>',key_event)

# -------------------------------
# Step 3: Create calculator buttons
# -------------------------------

# List of button labels arranged like a calculator layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# -------------------------------
# Step 4: Add buttons to the window
# -------------------------------
for (text,row,col) in buttons:
    if text == '=':
        tk.Button(root,text=text,width=5,height=2,font=('Arial',15),
                  command=calculate).grid(row=row,column=col,padx=5,pady=5)
    else:
        tk.Button(root,text=text,width=5,height=2,font=('Arial',15),
                  command=lambda val = text:click_button(val) ).grid(row=row,column=col,padx=5,pady=5)
        
# -------------------------------
# Step 5: Add a clear button
# -------------------------------
tk.Button(root,text='C',width=23,height=2, font=('Arial', 15),
          command=clear_entry).grid(row=5,column=0,columnspan=4,padx=5,pady=5)

# -------------------------------
# Step 6: Run the application loop
# -------------------------------
root.mainloop()

