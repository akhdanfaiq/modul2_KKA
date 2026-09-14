import pandas as pd
df = pd.read_csv("data_kantin.csv")

laris = df[df['terjual'] > 20] # filtering
urut = df.sort_values(by='terjual', ascending=False) # sorting
df['total_pendapatan'] = df['harga'] * df['terjual'] # kolom turunan
ringkasan = df.groupby('menu')['total_pendapatan'].sum() # agregasi
print(ringkasan)

# Tugas Analisis 6: Dari hasil groupby di atas, menu apa yang menghasilkan total_pendapatan
# tertinggi? Bagaimana informasi ini bisa membantu pengambilan keputusan di kantin sekolah?

#HASIL
# Menu yang menghasilkan total pendapatan tertinggi dapat ditentukan dari nilai terbesar pada hasil output print(ringkasan) di terminal. Informasi ini sangat berguna bagi pengelola kantin untuk membuat keputusan strategis, seperti memprioritaskan stok bahan baku menu terlaris agar tidak kehabisan, menargetkan promosi pada menu favorit, serta mengevaluasi atau mengganti menu yang kurang diminati guna memaksimalkan keuntungan operasional kantin.