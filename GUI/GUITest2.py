import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("My Window")

    # Create the main frame
    main_frame = tk.Frame(window, borderwidth=2, relief="groove")
    main_frame.pack(fill="both", expand=True)

    # Create the top frame for the headline
    top_frame = tk.Frame(main_frame, borderwidth=2, relief="groove")
    top_frame.pack(fill="x")
    headline_label = tk.Label(top_frame, text="Main Headline", font=("Arial", 16))
    headline_label.pack(pady=10)

    # Create the center frame
    center_frame = tk.Frame(main_frame, borderwidth=2, relief="groove")
    center_frame.pack(fill="both", expand=True)

    # Left frame for the link list
    left_frame = tk.Frame(center_frame, borderwidth=2, relief="groove", width=200)
    left_frame.pack(side="left", fill="y")

    # Top half of the left frame
    top_left_frame = tk.Frame(left_frame, borderwidth=2, relief="groove")
    top_left_frame.pack(fill="both", expand=True)
    link_label1 = tk.Label(top_left_frame, text="Link 1", font=("Arial", 12))
    link_label1.pack(pady=5)
    # ... add more link labels as needed

    # Bottom half of the left frame
    bottom_left_frame = tk.Frame(left_frame, borderwidth=2, relief="groove")
    bottom_left_frame.pack(fill="both", expand=True)
    link_label2 = tk.Label(bottom_left_frame, text="Link 2", font=("Arial", 12))
    link_label2.pack(pady=5)
    # ... add more link labels as needed

    # Right frame for the main page
    right_frame = tk.Frame(center_frame, borderwidth=2, relief="groove")
    right_frame.pack(side="right", fill="both", expand=True)
    main_page_label = tk.Label(right_frame, text="Main Page Content", font=("Arial", 12))
    main_page_label.pack(fill="both", expand=True)

    # Bottom frame for the footer
    bottom_frame = tk.Frame(main_frame, borderwidth=2, relief="groove")
    bottom_frame.pack(fill="x")
    footer_label = tk.Label(bottom_frame, text="Created by Your Name", font=("Arial", 10))
    footer_label.pack(pady=5)

    window.mainloop()

