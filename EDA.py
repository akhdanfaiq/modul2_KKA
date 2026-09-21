# ==========================================
# PROYEK AKHIR: EDA STARTER PROJECT
# ==========================================

import pandas as pd
import numpy as np

# ------------------------------------------
# 1. DATA LOADING & INSPECTION
# ------------------------------------------
# Memuat dataset
file_path = 'dataset_nilai_akademik_siswa - dataset_nilai_akademik_siswa.csv'
df = pd.read_csv(file_path)

print("=== 1. DATA LOADING & INSPECTION ===")
print("\n--- 5 Data Teratas (head) ---")
print(df.head())

print("\n--- Informasi Dataset (info) ---")
df.info()

print("\n--- Ukuran Data (shape) ---")
print(f"Jumlah baris: {df.shape[0]}, Jumlah kolom: {df.shape[1]}")

print("\n--- Ringkasan Statistik Awal (describe) ---")
print(df.describe(include='all'))


# ------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------
print("\n=== 2. DATA CLEANING ===")

df_clean = df.copy()

# A. Menangani Duplikat
jumlah_duplikat = df_clean.duplicated().sum()
print(f"Jumlah data duplikat ditemukan: {jumlah_duplikat}")
# Alasan: Data duplikat dihapus agar tidak menyebabkan bias pada perhitungan statistik.
df_clean = df_clean.drop_duplicates()

# B. Membersihkan dan Mengonversi Tipe Data Kolom 'nilai'
# Menghapus teks 'poin' dan mengonversi ke numerik
df_clean['nilai'] = df_clean['nilai'].astype(str).str.replace(' poin', '', regex=False)
df_clean['nilai'] = pd.to_numeric(df_clean['nilai'], errors='coerce')

# Menangani Outlier/Data Tidak Valid (misal: nilai > 100 seperti 999)
# Alasan: Nilai di atas 100 adalah kesalahan input data sehingga diubah menjadi NaN sebelum diimputasi.
df_clean.loc[df_clean['nilai'] > 100, 'nilai'] = np.nan

# C. Menangani Missing Value (Nilai Hilang)
# Imputasi missing value kolom 'nilai' dengan nilai Median
# Alasan: Median dipilih agar tidak terpengaruh oleh nilai ekstrem/outlier.
median_nilai = df_clean['nilai'].median()
df_clean['nilai'] = df_clean['nilai'].fillna(median_nilai)

# Imputasi missing value kolom 'guru_pengampu'
# Alasan: Diisi dengan label kategorikal 'Belum Terdata' agar informasi baris tidak hilang.
df_clean['guru_pengampu'] = df_clean['guru_pengampu'].fillna('Belum Terdata')

# D. Standarisasi Teks
df_clean['jenis_ujian'] = df_clean['jenis_ujian'].str.upper()

print("\n--- Cek Missing Value Setelah Cleaning ---")
print(df_clean.isnull().sum())


# ------------------------------------------
# 3. DATA MANIPULATION
# ------------------------------------------
print("\n=== 3. DATA MANIPULATION ===")

# A. Kolom Turunan (Predikat Nilai & Status Kelulusan)
# Menambahkan kategori status kelulusan berdasarkan KKM = 70
df_clean['status_kelulusan'] = df_clean['nilai'].apply(lambda x: 'Lulus' if x >= 70 else 'Remidi')

# B. Filtering
# Menyaring data siswa yang perlu mengikuti remidi (nilai < 70)
df_remidi = df_clean[df_clean['status_kelulusan'] == 'Remidi']
print("\n--- Contoh Hasil Filtering (Siswa Remidi - Top 5) ---")
print(df_remidi[['id_siswa', 'nama', 'kelas', 'mata_pelajaran', 'nilai']].head())

# C. Sorting
# Mengurutkan seluruh data berdasarkan nilai tertinggi ke terendah
df_sorted = df_clean.sort_values(by='nilai', ascending=False)
print("\n--- Contoh Hasil Sorting (Nilai Tertinggi - Top 5) ---")
print(df_sorted[['nama', 'kelas', 'mata_pelajaran', 'nilai']].head())

# D. Groupby / Agregasi
# Menghitung rata-rata nilai, nilai minimum, maksimum, dan jumlah siswa per mata pelajaran
df_groupby = df_clean.groupby('mata_pelajaran').agg(
    rata_rata_nilai=('nilai', 'mean'),
    nilai_tertinggi=('nilai', 'max'),
    nilai_terendah=('nilai', 'min'),
    jumlah_ujian=('nilai', 'count')
).reset_index()

print("\n--- Hasil Groupby (Agregasi per Mata Pelajaran) ---")
print(df_groupby)


# ------------------------------------------
# 4. EXPORT DATASET BERSIH
# ------------------------------------------
df_clean.to_csv('dataset_bersih.csv', index=False)
print("\nDataset bersih berhasil disimpan ke file 'dataset_bersih.csv'.")