from tkinter import *

# Define functions for performing operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 / num2

def mod(num1, num2):
    return num1%num2


def calculate():
    try:
        # Get the numbers and operator from the input fields
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_entry.get()

        # Perform the operation based on the selected operator
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "%":
            result = mod(num1, num2)
        
        else:
            result = "Invalid operator"

        # Display the result in the result label
        calculate_button.config(text="Result: " + str(result))
    except ValueError:
        calculate_button.config(text="Error: Invalid input")

# Create the main new
new=Tk()
new.title("To-Do-List")
new.geometry("925x500+300+200")
new.state("zoomed")
new.configure(bg="white")
wel=Label(new,text="Calculator",bg='white',fg='blue',font=('Fort',40,'bold'))
wel.place(x=550,y=50)

# Create the input fields
num1_label =Label(new, text="Number 1:",bg='white',fg='blue',font=('Fort',25,'bold'))
num1_label.place(x=200,y=150)

num1_entry =Entry(new, width=10,border=3,font=('Fort',20,'bold'))
num1_entry.place(x=450,y=160,width=400,height=30)

operator_label =Label(new, text="Operator:",bg='white',fg='blue',font=('Fort',25,'bold'))
operator_label.place(x=200,y=350)

operator_entry =Entry(new, width=10,border=3,font=('Fort',20,'bold'))
operator_entry.place(x=450,y=360,width=400,height=30)


num2_label = Label(new, text="Number 2:",bg='white',fg='blue',font=('Fort',25,'bold'))
num2_label.place(x=200,y=250)

num2_entry =Entry(new, width=10,border=3,font=('Fort',20,'bold'))
num2_entry.place(x=450,y=260,width=400,height=30)

# Create the calculate button
calculate_button =Button(new, text="Result", border=0,command=calculate,bg='white',fg='blue',font=('Fort',25,'bold'))
calculate_button.place(x=450,y=460)

# Create the result label
##result_label =Label(new, text="Result:",bg='white',fg='blue',font=('Fort',25,'bold'))
##result_label.place(x=450,y=460)

# Start the main loop
new.mainloop()
