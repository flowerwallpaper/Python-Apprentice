"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""
# Import the required modules

from tkinter import messagebox, simpledialog, Tk

# Create a window object

window = Tk()     # Create a window object

# Hide the window, hint: use the withdraw method

window.withdraw()

# Ask the user for the first number   

first_num = simpledialog.askfloat("Calculator", "What's the first number you want to use?")

# Ask the user for the second number

second_num = simpledialog.askfloat("Calculator", "What's the second number you want to use?")

# Ask the user for the math operation

operation = simpledialog.askstring("Calculator", "What math operation do you want to use?")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

error = False

if(operation == "+"):
    total = first_num + second_num
elif(operation == "-"):
    total = first_num - second_num
elif(operation == "*"):
    total = first_num * second_num
elif(operation == "/"):
    total = first_num/second_num
else: 
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
   messagebox.showerror("Calculator", "Unknown operator")
   error = True

if error == False:
    messagebox.showinfo("Calculator", "Total: " + str(total))

# Keep the window open

window.mainloop()