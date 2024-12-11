import tkinter as tk


# Create a root window
root = tk.Tk()

# Create a label widget
label = tk.Label(root, text="Hello, world!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click me!")
button.pack()
#button["command"] = lambda: print("Hello, world!")


# Start the mainloop
root.mainloop()
