'''Proyek ini membuat sistem rekomendasi sederhana berdasarkan preferensi pengguna. Jika pengguna menyukai item tertentu, sistem akan merekomendasikan item lain yang serupa (berdasarkan aturan yang kita tentukan).
Konsep AI: Sistem berbasis aturan, knowledge representation.'''
def rekomendasi_film(film_disukai):
    rekomendasi = {
        "Avatar": ["Titanic", "The Avengers", "Dune"],
        "Titanic": ["Avatar", "The Notebook", "Romeo + Juliet"],
        "The Avengers": ["Iron Man", "Captain America", "Thor"],
        "Dune": ["Blade Runner 2049", "Arrival", "Interstellar"]
    }

    if film_disukai in rekomendasi:
        return rekomendasi[film_disukai]
    else:
        return "Film tidak ditemukan dalam database rekomendasi."

# Contoh penggunaan
film_pilihan = "Avatar"
rekomendasi = rekomendasi_film(film_pilihan)
print(f"Jika Anda menyukai '{film_pilihan}', Anda mungkin juga menyukai: {rekomendasi}")

film_pilihan = "Spiderman"
rekomendasi = rekomendasi_film(film_pilihan)
print(f"Jika Anda menyukai '{film_pilihan}', Anda mungkin juga menyukai: {rekomendasi}")