import numpy as np

harga = np.array([5000, 7000, 3000, 12000, 4500])
print('Rata-rata harga:', harga.mean())
print('Harga tertinggi:', harga.max())
print('Harga setelah diskon 10%:', harga * 0.9)

hargaBaru = [5000, 7000, 3000]
print('Harga setelah diskon 10%:', hargaBaru * 0.9)

#Tugas Analisis 1: Bandingkan hasil harga * 0.9 di atas dengan jika harga berupa list Python
#biasa (bukan array). Apa yang terjadi bila kamu mencoba [5000,7000,3000] * 0.9? Jelaskan
#mengapa berbeda.

# HASIL : error
# Jika mencoba `[5000, 7000, 3000] * 0.9` pada *list* Python biasa, program akan mengalami **`TypeError`** karena *list* tidak bisa dikalikan dengan desimal (*float*).