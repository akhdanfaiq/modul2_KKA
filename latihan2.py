import pandas as pd

data_kantin = {
'menu': ['Nasi Goreng', 'Es Teh', 'Mie Ayam', 'Es Teh', None],
'harga': [12000, 4000, 10000, 4000, 8000],
'terjual': [23, 40, None, 35, 18]
}
df = pd.DataFrame(data_kantin)
print(df)

#Tugas Analisis 2: Amati tabel yang dihasilkan. Kolom mana yang terlihat memiliki data kosong
#(None)? Menurutmu apa risikonya jika data ini langsung dianalisis tanpa dibersihkan?

#HASIL
#Berdasarkan tabel yang dihasilkan, kolom yang memiliki data kosong adalah: Kolom terjual pada baris indeks 2, Kolom menu pada baris indeks 4,
#Risiko Jika Data Langsung Dianalisis Tanpa Dibersihkan
#Perhitungan Statistik Menjadi Tidak Akurat / Bias#
#Error Saat Pemrosesan Data atau Pembuatan Laporan
#Duplikasi Data Memicu Double Counting