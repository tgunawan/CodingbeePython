'''Penjelasan: Proyek ini membuat model regresi linear sederhana untuk memprediksi angka berdasarkan satu fitur input. Kita akan menggunakan library scikit-learn.
Konsep ML: Regresi Linear.'''
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data sederhana
X = np.array([1, 2, 3, 4, 5,6,7]).reshape(-1, 1)
y = np.array([2,1,3,2,1,3,2])

# Membuat model regresi linear
model = LinearRegression()

# Melatih model
model.fit(X, y)

# Prediksi
x_baru = np.array([8]).reshape(-1, 1)
prediksi = model.predict(x_baru)
print(f"Prediksi untuk input 6: {prediksi[0]:.2f}")

# Visualisasi data dan garis regresi
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Garis Regresi')
plt.scatter(x_baru, prediksi, color='green', marker='x', s=100, label='Prediksi')
plt.xlabel('Input (X)')
plt.ylabel('Output (y)')
plt.title('Regresi Linear Sederhana')
plt.legend()
plt.show()