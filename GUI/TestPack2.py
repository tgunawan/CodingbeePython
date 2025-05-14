import tkinter as tk

def create_link_list(frame, list):
    for link in list:
        link_label=tk.Label(frame, text=link,cursor="hand2",fg="blue")
        link_label.pack(fill=tk.X)

root = tk.Tk()
root.title("Division Pack")
root.geometry("500x300")


#Top Frame
top_Frame=tk.Frame(root)
top_Frame.pack(fill=tk.X)
judul_Label=tk.Label(top_Frame, text="Window Title",fg="blue",font=("Arial",16))
judul_Label.pack(pady=10)

# Center Frame
tengah_Frame=tk.Frame(root)
tengah_Frame.pack(fill=tk.BOTH, expand=True)

# left Frame
kiri_Frame=tk.Frame(tengah_Frame)
kiri_Frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#Left Link
top_Left=tk.Frame(kiri_Frame)
top_Left.pack(fill=tk.BOTH, expand=True)
create_link_list(top_Left, ['Link1', 'Link2', 'Link3','Link4'])

#left bottom
bot_Left=tk.Frame(kiri_Frame)
bot_Left.pack(fill=tk.BOTH, expand=True)
create_link_list(top_Left, ['tautan1','tautan2'])

#right 
kanan_frame = tk.Frame(tengah_Frame)
kanan_frame.pack(fill=tk.BOTH,side=tk.RIGHT, expand=True)
kanan_Label=tk.Label(kanan_frame, text="test Title",fg="blue",font=("Arial",16))
kanan_Label.pack(fill=tk.BOTH,expand=True)

#bawah
bawah_Frame=tk.Frame(root)
bawah_Frame.pack(fill=tk.X)
footer_Label=tk.Label(bawah_Frame, text="test footer",fg="red",font=("Arial",16))
footer_Label.pack(pady=10,expand=True)





root.mainloop()