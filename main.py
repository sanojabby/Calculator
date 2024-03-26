import tkinter as tk

calculation=""

def add_to_calculation (symbol):     #define a function add_to_calculation that takes a symbol as an argument.
    global calculation   #This line informs the function that it should use the global variable named calculation instead of creating a new local variable with the same name
    calculation += str(symbol)   #This line appends the string representation of the symbol to the calculation variable.
    text_result.delete(1.0, "end")   #This line deletes all the content of the text_result widget.
    text_result.insert(1.0,calculation)   #This line inserts the updated calculation string at the beginning of the text_result widget.
def evaluate_calculation():
    global calculation
    try:      #This block tries to evaluate the expression stored in calculation using eval(calculation). If successful, it converts the result to a string and assigns it back to calculation.
        calculation= str(eval(calculation)) 
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)  #This line inserts the updated calculation string into the text_result widget.
    except:    #This block catches any exceptions that might occur during evaluation
        clear_field()    #If an exception occurs, it calls a function named clear_field
        text_result.insert(1,0, "error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")

    

root= tk. Tk()  #initializing a Tkinter application window. Here's how you can create a basic Tkinter window named root
root.title("Sano_calculator")
root.geometry("300x275") #This line of code sets the size of the Tkinter window to be 300 pixels wide and 275 pixels tall

text_result= tk.Text(root, height=2, width=16,font=("Arial", 24))
text_result.grid(columnspan=5)   #This line of code suggests that you are using the grid() method to organize widgets within your Tkinter window,
# and you want to place the widget named text_result in the grid layout spanning across 5 columns.

btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("arial", 14))
  #tk.Button() creates a button widget.
  #text="1" sets the text label of the button to "1".
  #command=lambda: add_to_calculation(1) associates the add_to_calculation function with the button click event, passing 1 as an argument.
  #width=5 sets the width of the button to accommodate 5 characters.
  #font=("Arial", 14) sets the font family and size for the button label.
  #btn1.grid() places the button in the grid layout. Adjust the row and column as needed.
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("arial", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("arial", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("arial", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("arial", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(5), width=5, font=("arial", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(5), width=5, font=("arial", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(5), width=5, font=("arial", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("arial", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(5), width=5, font=("arial", 14))
btn0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("arial", 14))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("arial", 14))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("arial", 14))
btn_div.grid(row=5, column=4)
btn_clear = tk.Button(root, text="c", command=clear_field, width=5, font=("arial", 14))
btn_clear.grid(row=5, column=1, columnspan=1)
btn_equal = tk.Button(root, text="=", command= evaluate_calculation, width=5, font=("arial", 14))
btn_equal.grid(row=5, column=3)


root.mainloop()