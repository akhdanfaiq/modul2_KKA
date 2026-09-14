import pandas as pd
df = pd.read_csv("data_kantin.csv")

print(df.duplicated().sum()) # jumlah baris duplikat
df = df.drop_duplicates()
df['harga'] = df['harga'].astype(int) # memastikan tipe data harga adalah integer
print(df.dtypes)

#Tugas Analisis 5: Setelah drop_duplicates(), berapa jumlah baris dataset sekarang dibanding
#sebelumnya? Mengapa penting memastikan tipe data (dtypes) sudah benar sebelum data
#dianalisis lebih lanjut?

#HASIL
# Jumlah baris dataset sekarang berkurang sesuai dengan jumlah baris duplikat yang terdeteksi pada perintah print(df.duplicated().sum()). Memastikan tipe data (dtypes) sudah benar sangat penting sebelum analisis dilakukan agar operasi matematika seperti kalkulasi total harga tidak menghasilkan error atau salah kaprah—misalnya teks "1000" yang digabung, bukan dijumlahkan secara numerik—sekaligus menjaga efisiensi penggunaan memori program.