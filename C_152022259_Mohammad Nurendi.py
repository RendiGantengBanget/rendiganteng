import pandas as pd

data = {
    "Nama": ["John", "Jane", "Bob", "Alice"],
    "Usia": [25, 35, 30, 28],
    "Gaji": [50000, 60000, 70000, 55000],
}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
df["Gaji Setelah Peningkatan"] = df["Gaji"].apply(lambda x: x * 1.05)
print("DataFrame setelah perubahan:")
print(df)


# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nRingkasan perubahan:")
for index, row in df.iterrows():
    print(
        f"{row['Nama']} ({row['Usia']} tahun): Gaji sebelumnya {row['Gaji']} -> Gaji setelah peningkatan {row['Gaji Setelah Peningkatan']}"
    )


# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

for index, row in df.iterrows():
    if row["Usia"] > 30:
        df.at[index, "Gaji Setelah Peningkatan"] = (
            row["Gaji Setelah Peningkatan"] * 1.02
        )

# Menampilkan DataFrame yang sudah diperbarui
print("\nDataFrame setelah evaluasi:")
print(df)


# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

print("\nRingkasan hasil:")
for index, row in df.iterrows():
    print(
        f"{row['Nama']} ({row['Usia']} tahun): Gaji sebelumnya {row['Gaji']} -> Gaji setelah peningkatan {row['Gaji Setelah Peningkatan']}"
    )

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
