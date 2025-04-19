import tkinter as tk
from tkinter import ttk

def create_tab_view():
    window = tk.Tk()
    window.title("Tabbed View Example")

    # Create a Notebook widget
    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True)

    # Create the first tab
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Tab 1")

    # Add content to the first tab
    label1 = tk.Label(tab1, text="This is Tab 1")
    label1.pack(pady=20)

    # Create the second tab
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Tab 2")

    # Add content to the second tab
    label2 = tk.Label(tab2, text="This is Tab 2")
    label2.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_tab_view()
    print("finish")