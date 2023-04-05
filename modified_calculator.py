import tkinter as tk


# Function to display entry
def display_entry():
    global equation
    equation = tk.StringVar()

    entry_field = tk.Entry(window, textvariable=equation, width=15, font=('Arial', 20, 'bold'))
    entry_field.grid(columnspan=4, ipadx=20, pady=10)

# Function to display button
def display_button():
    column1, column2, column3, column4 = 0, 0, 0, 0
    for button in range(1, 18):
        create_button = tk.Button(window, text=str(button), foreground="yellow", bg="black", height=1, width=9)
        if button < 5:
            if button == 4:
                create_button.config(text="+", command= lambda: click("+"))
            else:
                create_button.config(text=str(button), command=lambda button_text = str(button): click(button_text))
            create_button.grid(row=1, column= column1)
            column1 += 1
        elif button >= 5 and button <= 8:
            if button == 8:
                create_button.config(text="-", command= lambda: click("-"))
            else:
                create_button.config(text=str(button - 1),  command=lambda button_text = str(button - 1): click(button_text))      
            create_button.grid(row=2, column = column2)
            column2 += 1
        elif button >= 9 and button <= 12:
            if button == 12:
                create_button.config(text="*", command= lambda: click("*"))
            else:
                create_button.config(text=str(button - 2), command=lambda button_text = str(button - 2): click(button_text)) 
            create_button.grid(row=3, column = column3)
            column3 += 1
        elif button >= 13 and button <= 16:

            if button == 13:
                create_button.config(text="0", command=lambda : click('0'))
            elif button == 14:
                create_button.config(text="C", command=clear_screen)
            elif button == 15:
                create_button.config(text="=", command= equals_to)
            elif button == 16:
                create_button.config(text="/", command= lambda: click("/"))
            create_button.grid(row=4, column = column4)
            column4 += 1
        elif button == 17:
            create_button.config(text=".", command= lambda: click("."))
            create_button.grid(row=5, column = 0)    

# Function to get clicked event
def click(event):
    global expression
    expression += event
    equation.set(expression)
    

# Function to clear screen
def clear_screen():
    global expression
    expression = ""
    equation.set(expression)

    

# Function to get result
def equals_to():
    global expression

    try:
        total = str(eval(expression))
        equation.set(total)
    except Exception:
        equation.set("Syntax Error")
        expression = ""

if __name__=='__main__':
    window = tk.Tk()
    window.geometry('292x185')
    window.resizable(0, 0)
    
    #Global Variable 
    expression = "" 
    
    display_entry()
    display_button()
    

    window.mainloop()