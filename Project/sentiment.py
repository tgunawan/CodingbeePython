'''Proyek ini bertujuan untuk mengklasifikasikan sentimen dalam kalimat pendek menjadi positif atau negatif. Kita akan menggunakan pendekatan sederhana dengan menghitung frekuensi kata-kata positif dan negatif.
Konsep AI/ML: Natural Language Processing (NLP), klasifikasi berbasis aturan sederhana.'''
def analyze_sentiment(text):
    positive_words = ["bagus", "senang", "suka", "hebat", "luar biasa"]
    negative_words = ["buruk", "sedih", "benci", "jelek", "mengecewakan"]

    positive_count = 0
    negative_count = 0

    words = text.lower().split()
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        return "Positif"
    elif negative_count > positive_count:
        return "Negatif"
    else:
        return "Netral"


teks1 = "Film ini sangat bagus dan saya suka sekali."
teks2 = "Pelayanan di restoran itu sangat buruk dan mengecewakan."
teks3 = "Cuaca hari ini biasa saja."

print(f"Sentimen '{teks1}': {analyze_sentiment(teks1)}")
print(f"Sentimen '{teks2}': {analyze_sentiment(teks2)}")
print(f"Sentimen '{teks3}': {analyze_sentiment(teks3)}")