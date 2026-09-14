import pandas as pd
df = pd.read_csv("data_kantin.csv")


print(df.isnull().sum()) # jumlah data kosong tiap kolom
df['terjual'] = df['terjual'].fillna(0) # isi kekosongan dengan 0
df = df.dropna(subset=['menu']) # hapus baris jika kolom menu kosong

#Tugas Analisis 4: Mengapa pada contoh di atas kolom terjual diisi (fillna) sedangkan baris
#dengan menu kosong justru dihapus (dropna)? Diskusikan alasan logisnya.

#HASIL
#Kolom terjual diisi dengan 0 karena data kosong dapat dianggap sebagai tidak ada barang yang terjual. Sedangkan baris dengan kolom menu kosong dihapus karena nama menu merupakan informasi penting untuk mengetahui data tersebut. Jika menu kosong, data menjadi tidak jelas dan kurang berguna untuk analisis.