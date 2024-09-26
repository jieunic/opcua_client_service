## program trial for paralel iteration
# kode = [99, 98, 78]
# nilai = [10, 20, 30]

# for i, (k, v) in enumerate(zip(kode, nilai)):
#     print(f"Kode {k} memiliki nilai {v}")


# from datetime import datetime, date

# # Mendapatkan time stamp saat ini
# get_time = datetime.now()
# time_str = get_time.strftime("%Y-%m-%d %H:%M:%S")

# print("Time stamp saat ini:", time_str)

# import pandas as pd

# df = pd.read_excel("svcEngine/bin/dataset/dataset.xlsx")
# node_ids = df['NODE_ID'].tolist()

# print(node_ids)
# def baca_file_excel(nama_file):
#     try:
#         # Membaca file Excel
#         df = pd.read_excel(nama_file, dtype=str)
#         data_dict = df.to_dict(orient='records')
#         for row in data_dict:
#             print(row['NODE_ID'])
    
#     except FileNotFoundError:
#         print(f"File '{nama_file}' tidak ditemukan.")
#     except Exception as e:
#         print(f"Terjadi kesalahan: {str(e)}")

# if __name__ == "__main__":
#     nama_file_excel = "svcEngine/bin/dataset/dataset.xlsx"  # Ganti dengan nama file Excel Anda
#     baca_file_excel(nama_file_excel)

# import pandas as pd
# import ast

# # Baca file Excel
# df = pd.read_excel("svcEngine/bin/dataset/dataset.xlsx")

# # Fungsi untuk mengonversi string ke list
# def extract_list_from_string(string):
#     try:
#         # Menghapus karakter yang tidak perlu dan mengonversi string menjadi list
#         return ast.literal_eval(string)
#     except (ValueError, SyntaxError):
#         return []

# # Ambil kolom INDEX_LIST_VALUE dan konversi ke list
# index_list_values = df['INDEX_LIST_VALUE'].apply(extract_list_from_string)

# # Konversi ke list Python
# result_list = index_list_values.tolist()

# # Tampilkan hasil
# for item in result_list:
#     print(item)


# import pandas as pd

# # Membaca file Excel
# df = pd.read_excel("svcEngine/bin/dataset/dataset.xlsx")

# # Fungsi untuk memisahkan nilai di kolom INDEX_LIST_VALUE
# def split_index_list_value(cell_value):
#     # # Menghapus tanda kurung dan spasi kosong
#     clean_value = cell_value.strip("'").replace(' ', '')
#     # Memisahkan nilai berdasarkan koma
#     return cell_value.split(',')

# # Menerapkan fungsi ke kolom INDEX_LIST_VALUE
# df['INDEX_LIST_VALUE'] = df['INDEX_LIST_VALUE'].apply(split_index_list_value)

# # Menampilkan hasil
# print(df)


# import time

# def is_all_zero(val):
#     return all(v == 0.00 for v in val)

# def is_any_non_zero(val):
#     return any(v > 0 for v in val)

# val = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

# if isinstance(val, list):
#     if is_all_zero(val):
#         time.sleep(2)
#         count = 0
#         while True:
#             time.sleep(1)
#             count += 1
#             if is_any_non_zero(val):
#                 print(count)
#                 break


import time

# Variabel untuk menyimpan waktu saat input True pertama diterima
first_true_time = None

while True:
    # Menerima input dari pengguna
    user_input = input("Masukkan 'True' atau 'False': ").strip().lower()

    if user_input == 'true':
        current_time = time.time()

        if first_true_time is None:
            # Merekam waktu saat menerima True pertama kali
            first_true_time = current_time
            print(f"True pertama diterima pada {time.strftime('%M:%S', time.localtime(first_true_time))}")
        else:
            # Menghitung jarak waktu antara True pertama dan kedua
            time_diff = current_time - first_true_time
            print(f"True kedua diterima. Jarak waktu: {time_diff:.2f} detik")
            break
    elif user_input == 'false':
        print("False diterima, menunggu input 'True'...")
    else:
        print("Input tidak valid, masukkan 'True' atau 'False'!")