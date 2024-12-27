class PesawatLionAir:
    def __init__(self, nomor_pesawat, kapasitas_penumpang, tujuan, status_penerbangan):
        self.nomor_pesawat = nomor_pesawat  # Variabel untuk menyimpan nomor pesawat
        self.kapasitas_penumpang = kapasitas_penumpang  # Variabel untuk menyimpan kapasitas penumpang
        self.tujuan = tujuan  # Variabel untuk menyimpan tujuan penerbangan
        self.status_penerbangan = status_penerbangan  # Variabel untuk menyimpan status penerbangan (contoh: 'Terbang', 'Mendarat', 'Siap')
        self.jumlah_penumpang = 0  # Variabel untuk melacak jumlah penumpang saat ini

    # Method untuk menambahkan penumpang ke dalam pesawat
    def tambah_penumpang(self, jumlah):
        if self.jumlah_penumpang + jumlah <= self.kapasitas_penumpang:
            self.jumlah_penumpang += jumlah
            print(f"{jumlah} penumpang berhasil ditambahkan. Total penumpang: {self.jumlah_penumpang}")
        else:
            print(f"Tidak bisa menambahkan {jumlah} penumpang. Kapasitas pesawat sudah penuh.")

    # Method untuk mengubah tujuan penerbangan
    def ubah_tujuan(self, tujuan_baru):
        self.tujuan = tujuan_baru
        print(f"Tujuan penerbangan diubah menjadi {self.tujuan}")

    # Method untuk mengubah status penerbangan
    def ubah_status(self, status_baru):
        self.status_penerbangan = status_baru
        print(f"Status penerbangan diubah menjadi {self.status_penerbangan}")

    # Method untuk menampilkan informasi pesawat
    def info_pesawat(self):
        print(f"Pesawat {self.nomor_pesawat} - Tujuan: {self.tujuan} - Status: {self.status_penerbangan} - Penumpang: {self.jumlah_penumpang}/{self.kapasitas_penumpang}")

# Contoh penggunaan class
pesawat1 = PesawatLionAir("JT123", 180, "Jakarta - Surabaya", "Siap")
pesawat1.info_pesawat()
pesawat1.tambah_penumpang(150)
pesawat1.ubah_status("Terbang")
pesawat1.info_pesawat()
pesawat1.ubah_tujuan("Jakarta - Bali")
pesawat1.tambah_penumpang(40)  # Melebihi kapasitas
pesawat1.ubah_status("Mendarat")
pesawat1.info_pesawat()
