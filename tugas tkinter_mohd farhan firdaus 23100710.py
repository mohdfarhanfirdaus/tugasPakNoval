import tkinter as tk
from tkinter import messagebox

def simpan_data():
    # Mengambil nilai dari entry
    nim = entry_nim.get()
    nama = entry_nama.get()
    prodi = entry_prodi.get()
    semester = entry_semester.get()
    ipk_sem1 = entry_ipk_sem1.get()
    ipk_sem2 = entry_ipk_sem2.get()

    # Menampilkan pesan untuk konfirmasi
    messagebox.showinfo("Data Tersimpan", f"Data Mahasiswa:\n\n"
                        f"NIM: {nim}\n"
                        f"Nama: {nama}\n"
                        f"Prodi: {prodi}\n"
                        f"Semester: {semester}\n"
                        f"IPK Semester 1: {ipk_sem1}\n"
                        f"IPK Semester 2: {ipk_sem2}")

# Membuat jendela utama
root = tk.Tk()
root.title("Form Data Mahasiswa")

# Membuat label dan entry untuk NIM
label_nim = tk.Label(root, text="NIM")
label_nim.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nim = tk.Entry(root)
entry_nim.grid(row=0, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Nama
label_nama = tk.Label(root, text="Nama")
label_nama.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Prodi
label_prodi = tk.Label(root, text="Prodi")
label_prodi.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_prodi = tk.Entry(root)
entry_prodi.grid(row=2, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Semester
label_semester = tk.Label(root, text="Semester")
label_semester.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_semester = tk.Entry(root)
entry_semester.grid(row=3, column=1, padx=10, pady=5)

# Membuat label dan entry untuk IPK Semester 1
label_ipk_sem1 = tk.Label(root, text="IPK Semester 1")
label_ipk_sem1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_ipk_sem1 = tk.Entry(root)
entry_ipk_sem1.grid(row=4, column=1, padx=10, pady=5)

# Membuat label dan entry untuk IPK Semester 2
label_ipk_sem2 = tk.Label(root, text="IPK Semester 2")
label_ipk_sem2.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_ipk_sem2 = tk.Entry(root)
entry_ipk_sem2.grid(row=5, column=1, padx=10, pady=5)

# Membuat tombol SIMPAN
button_simpan = tk.Button(root, text="SIMPAN", command=simpan_data)
button_simpan.grid(row=6, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()