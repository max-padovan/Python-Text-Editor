import tkinter as tk

def change_font():
    # Get the selected text
    selected_text = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)

    # Configure a new tag with the desired font
    text_widget.tag_configure("new_font", font=("Helvetica", 12, "bold"))

    # Apply the tag to the selected text
    text_widget.tag_add("new_font", tk.SEL_FIRST, tk.SEL_LAST)

# Create the Tkinter window
root = tk.Tk()
root.title("Change Font Example")

# Create a Text widget
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

# Insert some sample text
text_widget.insert(tk.END, "This is some sample text.")

# Create a button to change the font of the selected text
button = tk.Button(root, text="Change Font", command=change_font)
button.pack()

# Run the Tkinter event loop
root.mainloop()