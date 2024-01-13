import tkinter as tk
value = 0
class MyClass:
    def __init__(self, value):
        self.value = value
        print(f"Instance created with value: {self.value}")

def create_instance(value):
    my_instance = MyClass(value)
    value += value

# Create the main Tkinter window
root = tk.Tk()
root.title("Create Instance Example")

# Button to create an instance based on the condition
create_button = tk.Button(root, text="Create Instance", command=create_instance(value))
create_button.pack()

# Run the Tkinter event loop
root.mainloop()