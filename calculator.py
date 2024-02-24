# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


def squareroot():
    global expression
    return True


def squared():
    return True


def cube():
    return True


def rootx():
    return True


# Function to update expression in the text entry box
def press(num):
    # point out the global expression variable
    global expression, expression_field

    # concatenation of string
    expression = expression_field.get() + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress(event=None):
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression
        # If no button was press it gets the string from the Entry
        if expression == "":
            total = str(eval(expression_field.get()))
        else:
            # eval function evaluate the expression
            # and str function convert the result
            # into string
            total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("290x400")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='gray',
                     command=lambda: press(1), height=3, width=7)
    button1.grid(row=3, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='gray',
                     command=lambda: press(2), height=3, width=7)
    button2.grid(row=3, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='gray',
                     command=lambda: press(3), height=3, width=7)
    button3.grid(row=3, column=2)

    spacer1 = Label(gui, text="", height=1, bg="light green")

    spacer1.grid(row=4)

    button4 = Button(gui, text=' 4 ', fg='black', bg='gray',
                     command=lambda: press(4), height=3, width=7)
    button4.grid(row=5, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='gray',
                     command=lambda: press(5), height=3, width=7)
    button5.grid(row=5, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='gray',
                     command=lambda: press(6), height=3, width=7)
    button6.grid(row=5, column=2)

    spacer2 = Label(gui, text="", height=1, bg="light green")
    spacer2.grid(row=6)

    button7 = Button(gui, text=' 7 ', fg='black', bg='gray',
                     command=lambda: press(7), height=3, width=7)
    button7.grid(row=7, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='gray',
                     command=lambda: press(8), height=3, width=7)
    button8.grid(row=7, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='gray',
                     command=lambda: press(9), height=3, width=7)
    button9.grid(row=7, column=2)

    spacer3 = Label(gui, text="", height=1, bg="light green")
    spacer3.grid(row=8)

    button0 = Button(gui, text=' 0 ', fg='black', bg='gray',
                     command=lambda: press(0), height=3, width=7)
    button0.grid(row=9, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='gray',
                  command=lambda: press("+"), height=3, width=7)
    plus.grid(row=3, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='gray',
                   command=lambda: press("-"), height=3, width=7)
    minus.grid(row=5, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='gray',
                      command=lambda: press("*"), height=3, width=7)
    multiply.grid(row=7, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='gray',
                    command=lambda: press("/"), height=3, width=7)
    divide.grid(row=9, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='gray',
                   command=equalpress, height=3, width=7)

    equal.grid(row=9, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='gray',
                   command=clear, height=3, width=7)
    clear.grid(row=9, column='1')

    spacer4 = Label(gui, text="", height=1, bg="light green")
    spacer4.grid(row=10)

    Decimal = Button(gui, text='.', fg='black', bg='gray',
                     command=lambda: press('.'), height=3, width=7)
    Decimal.grid(row=11, column=0)

    # Bind the Enter key to make the result
    gui.bind('<Return>', equalpress)
    # start the GUI
    gui.mainloop()
