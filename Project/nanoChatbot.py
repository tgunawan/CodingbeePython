'''Proyek ini membuat chatbot sederhana yang merespons pertanyaan atau input pengguna berdasarkan aturan atau pola yang telah ditentukan.
Konsep AI: Natural Language Processing (NLP), sistem berbasis aturan, pattern matching.'''
def chatbot(input_pengguna):
    input_lower = input_pengguna.lower()

    if "halo" in input_lower or "hai" in input_lower:
        return "Halo! Ada yang bisa saya bantu?"
    elif "apa kabar" in input_lower:
        return "Kabar baik! Bagaimana dengan Anda?"
    elif "terima kasih" in input_lower:
        return "Sama-sama!"
    elif "siapa nama kamu" in input_lower:
        return "Saya adalah chatbot sederhana."
    elif "selamat tinggal" in input_lower or "sampai jumpa" in input_lower:
        return "Sampai jumpa! Semoga hari Anda menyenangkan!"
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda."

# Contoh interaksi
print(chatbot("Halo"))
print(chatbot("Apa kabar?"))
print(chatbot("Terima kasih banyak!"))
print(chatbot("Siapa nama kamu?"))
print(chatbot("Bagaimana cuaca hari ini?"))
print(chatbot("Selamat tinggal."))

while True:
    user_input = input("Anda: ")
    response = chatbot(user_input)
    print("Chatbot:", response)
    if "selamat tinggal" in user_input.lower():
        break