
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class PlaylistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Playlist Musik")
        self.root.geometry("700x450")

        self.playlist_files = {
            "pop": "playlist_pop.txt",
            "rock": "playlist_rock.txt"
        }

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Selamat Datang di Playlist Musik", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.root, text="Playlist Pop", width=20, command=self.show_pop_playlist).pack(pady=10)
        tk.Button(self.root, text="Playlist Rock", width=20, command=self.show_rock_playlist).pack(pady=10)
        tk.Button(self.root, text="Semua Playlist", width=20, command=self.show_all_playlists).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def load_playlist(self, genre):
        filename = self.playlist_files[genre]
        if not os.path.exists(filename):
            with open(filename, 'w'): pass
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def save_song(self, genre, song_name):
        filename = self.playlist_files[genre]
        with open(filename, 'a') as f:
            f.write(song_name + "\n")

    def remove_song(self, genre, song_name):
        filename = self.playlist_files[genre]
        with open(filename, 'r') as f:
            songs = [line.strip() for line in f.readlines()]
        songs = [s for s in songs if s != song_name]
        with open(filename, 'w') as f:
            for s in songs:
                f.write(s + "\n")

    def create_playlist_frame(self, genre):
        self.clear_frame()
        tk.Label(self.root, text=f"Playlist {genre.capitalize()}", font=("Helvetica", 14)).pack(pady=10)

        listbox = tk.Listbox(self.root, width=50)
        listbox.pack(pady=10)

        for song in self.load_playlist(genre):
            listbox.insert(tk.END, song)

        def add_song():
            song = simpledialog.askstring("Tambah Lagu", "Masukkan judul lagu:")
            if song:
                self.save_song(genre, song)
                listbox.insert(tk.END, song)
                messagebox.showinfo("Berhasil", f"Lagu '{song}' ditambahkan ke playlist {genre.capitalize()}.")

        tk.Button(self.root, text="Tambah Lagu", command=add_song).pack(pady=10)
        tk.Button(self.root, text="Kembali", command=self.create_main_menu).pack(pady=5)

    def show_pop_playlist(self):
        self.create_playlist_frame("pop")

    def show_rock_playlist(self):
        self.create_playlist_frame("rock")

    def show_all_playlists(self):
        self.clear_frame()

        tk.Label(self.root, text="Semua Playlist", font=("Helvetica", 14)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH, padx=10)

        # Frame untuk Pop
        pop_frame = tk.Frame(frame)
        pop_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

        tk.Label(pop_frame, text="Playlist Pop").pack()
        pop_listbox = tk.Listbox(pop_frame, width=30)
        pop_listbox.pack(pady=5)
        for song in self.load_playlist("pop"):
            pop_listbox.insert(tk.END, song)

        # Frame tombol di tengah
        middle_frame = tk.Frame(frame)
        middle_frame.pack(side=tk.LEFT, padx=5, pady=5)

        def move_song():
            selected_pop = pop_listbox.curselection()
            selected_rock = rock_listbox.curselection()

            if selected_pop:
                song = pop_listbox.get(selected_pop)
                self.remove_song("pop", song)
                self.save_song("rock", song)
                messagebox.showinfo("Dipindahkan", f"Lagu '{song}' dipindah ke Playlist Rock.")
            elif selected_rock:
                song = rock_listbox.get(selected_rock)
                self.remove_song("rock", song)
                self.save_song("pop", song)
                messagebox.showinfo("Dipindahkan", f"Lagu '{song}' dipindah ke Playlist Pop.")
            else:
                messagebox.showwarning("Tidak Ada Pilihan", "Pilih satu lagu untuk dipindahkan.")

            self.show_all_playlists()  # Refresh tampilan

        move_btn = tk.Button(middle_frame, text="⏩\nPindahkan Lagu\n⏪", command=move_song)
        move_btn.pack(pady=50)

        # Frame untuk Rock
        rock_frame = tk.Frame(frame)
        rock_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

        tk.Label(rock_frame, text="Playlist Rock").pack()
        rock_listbox = tk.Listbox(rock_frame, width=30)
        rock_listbox.pack(pady=5)
        for song in self.load_playlist("rock"):
            rock_listbox.insert(tk.END, song)

        tk.Button(self.root, text="Kembali", command=self.create_main_menu).pack(pady=10)

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = PlaylistApp(root)
    root.mainloop()
