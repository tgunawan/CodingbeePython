import tkinter as tk

def create_link_list(frame, links):
    for link in links:
        link_label = tk.Label(frame, text=link, cursor="hand2", fg="blue")
        link_label.pack(fill=tk.X)

root = tk.Tk()
root.title("My Window")

# Top Frame (Headline)
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X)
headline_label = tk.Label(top_frame, text="My Window Title", font=("Arial", 16))
headline_label.pack(pady=10)

# Center Frame (Main Content)
center_frame = tk.Frame(root)
center_frame.pack(fill=tk.BOTH, expand=True)

# Left Frame (Link List)
left_frame = tk.Frame(center_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Top Left Links
top_left_frame = tk.Frame(left_frame)
top_left_frame.pack(fill=tk.BOTH, expand=True)
create_link_list(top_left_frame, ["Link 1", "Link 2", "Link 3"])

# Bottom Left Links
bottom_left_frame = tk.Frame(left_frame)
bottom_left_frame.pack(fill=tk.BOTH, expand=True)
create_link_list(bottom_left_frame, ["Link 4", "Link 5", "Link 6"])

# Right Frame (Main Content)
right_frame = tk.Frame(center_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
# Add your main content here, e.g., labels, text boxes, buttons
main_content_label = tk.Label(right_frame, text="Main Content")
main_content_label.pack(fill=tk.BOTH, expand=True)

# Bottom Frame (Footer)
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X)
footer_label = tk.Label(bottom_frame, text="Created by Your Name")
footer_label.pack(pady=10)

root.mainloop()