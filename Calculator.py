import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Error: Invalid operation"

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Error: Invalid input")

window = tk.Tk()
window.title("Calculator")
#window.config(bg="grey")

#input field
label1 = tk.Label(window, text="Enter first number:")
label1.grid(row=0, column=1,pady=5,columnspan=1)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=3,pady=5,columnspan=1)

#input field
label2 = tk.Label(window, text="Enter second number:")
label2.grid(row=1, column=1,columnspan=1)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=3,columnspan=1)

# Operation selection
operator = tk.StringVar(value=" ")
operations = ["+" , "-" , "*" , "/"]
for i, op in enumerate(operations):
    tk.Radiobutton(window, text=op, variable=operator, value=op,indicatoron=0,width=3, selectcolor="light blue").grid(row=3, column=i+1,padx=3,pady=3,sticky="s")
#calculate button
calculate_button = tk.Button(window, text="Calculate",activebackground="light green", command=calculate)
calculate_button.grid(row=4, column=1, columnspan=4)

#result display
result_label = tk.Label(window, text="Result:",fg="red")
result_label.grid(row=5, column=1, columnspan=4)

window.mainloop()
