from tkinter import *

def click(event):
    global expression
 
    # concatenation of string
    expression = expression + str(event)
 
    # update the expression by using set method
    equation.set(expression)

def clear_screen():
    global expression
    expression = ""
    equation.set("")

def equals_to():
    global expression
    try: 
        # global expression
        total = str(eval(expression))
 
        equation.set(total)
        expression = ""
    except:
 
        equation.set("Syntax Error ")
        expression = ""

if __name__=='__main__':
    window = Tk()
    window.geometry('270x190')
    window.resizable(0, 0)

    #Global string variable
    expression = ""

    equation = StringVar()
    operation_field = Entry(window, textvariable=equation,width=15, font=("Arial", 20, "bold"))
    operation_field.grid(columnspan=4, ipadx=20, pady=10)

    button1 = Button(window, text=' 1 ', fg='white', bg='black',
                    command=lambda: click(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(window, text=' 2 ', fg='white', bg='black',
                    command=lambda: click(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(window, text=' 3 ', fg='white', bg='black',
                    command=lambda: click(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(window, text=' 4 ', fg='white', bg='black',
                    command=lambda: click(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(window, text=' 5 ', fg='white', bg='black',
                    command=lambda: click(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(window, text=' 6 ', fg='white', bg='black',
                    command=lambda: click(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(window, text=' 7 ', fg='white', bg='black',
                    command=lambda: click(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(window, text=' 8 ', fg='white', bg='black',
                    command=lambda: click(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(window, text=' 9 ', fg='white', bg='black',
                    command=lambda: click(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(window, text=' 0 ', fg='white', bg='black',
                    command=lambda: click(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(window, text=' + ', fg='white', bg='black',
                command=lambda: click("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(window, text=' - ', fg='white', bg='black',
                command=lambda: click("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(window, text=' * ', fg='white', bg='black',
                    command=lambda: click("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(window, text=' / ', fg='white', bg='black',
                    command=lambda: click("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(window, text=' = ', fg='white', bg='black',
                command=equals_to, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(window, text='Clear', fg='white', bg='black',
                command=clear_screen, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(window, text='.', fg='white', bg='black',
                    command=lambda: click('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)

    window.mainloop()