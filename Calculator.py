import tkinter as tk

root = tk.Tk()
root.title("Calculator") # Sets the window title

root.geometry("400x400" )  # Sets the size of the window
root.resizable(True,True)

# Create an entry widget for the display area
display = tk.Entry(root, font=("Arial", 16), borderwidth=2, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# List of tuples containing button labels and their grid positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and position buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), command=lambda x=text: button_click(x))
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)


for i in range(5):  # 5 rows, including the display
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

def button_click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, value)

        root.mainloop()


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def main():
    last_result = None
    while True:
        if last_result is None:
            print("Enter 'add', 'subtract', 'multiply', 'divide', or 'quit' to end")
        else:
            print("Current result is: {}".format(last_result))
            print("Enter 'add', 'subtract', 'multiply', 'divide', use 'new' for a new calculation, or 'quit' to end")
        
        user_input = input(": ").lower()

        if user_input == "quit":
            break
        elif user_input == "new":
            last_result = None
            continue

        if last_result is not None:
            print("Using current result as the first number.")
            num1 = last_result
        else:
            num1_input = input("Enter first number: ")
            try:
                num1 = float(num1_input)
            except ValueError:
                print("Invalid input, please enter a number.")
                continue
        
        num2_input = input("Enter second number: ")
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if user_input == "add":
            last_result = add(num1, num2)
        elif user_input == "subtract":
            last_result = subtract(num1, num2)
        elif user_input == "multiply":
            last_result = multiply(num1, num2)
        elif user_input == "divide":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
                continue
            last_result = result

        print("The result is", last_result)

if __name__ == "__main__":
    main()
