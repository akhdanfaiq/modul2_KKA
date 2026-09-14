import pandas as pd
df = pd.read_csv('data_kantin.csv')


print(df.head()) # 5 baris pertama
print(df.info()) # tipe data & jumlah non-null tiap kolom
print(df.describe()) # statistik ringkas kolom numerik
print(df.shape) # jumlah (baris, kolom)

#Tugas Analisis 3: Dari hasil df.info(), kolom mana yang jumlah non-null-nya lebih sedikit dari
#jumlah baris total? Apa artinya

#HASIL
#Berdasarkan data data_kantin.csv, kolom yang jumlah non-null-nya lebih sedikit dari jumlah baris total adalah menu dan terjual. #Artinya, terdapat data kosong (NaN/None) pada kedua kolom tersebut sehingga data perlu dibersihkan sebelum dianalisis.