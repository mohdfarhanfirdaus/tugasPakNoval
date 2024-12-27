import pymysql
#variabel cursor global
curr = any
conn = any

class MyDB:    
     def connect(self):
        con = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             database='admin',
                             )
        cur = con.cursor()
        return cur, con

class pengikut:
    def __init__(self, cursor, conn):
        self.cur = cursor
        self.conn = conn

    def cari_pengikut(self, id):
        self.cur.execute('SELECT * FROM pengikut WHERE id_pegawai ='+ id) 
        result = self.cur.fetchall()
        return result

    def tambah (self, id, nama, alamat, email):
        print('Tambah data pengikut...')
        query = 'INSERT INTO pengikut (id_pegawai, nama, alamat, email) VALUES ("' + id +'","'+ nama +'","'+alamat + '","'+email+'")';
        self.cur.execute(query)      
        self.conn.commit()
        # print('Query:', query)
        print('Proses penambahan selesai')

    def hapus(self, id):
        pass

    def update_alamat(self, id, alamat):
        pass

class Gaji:

    def hitung_pajak():
        pass

Dbase = MyDB()
curr, conn = Dbase.connect()

#buat object pengikut
pgt = pengikut(curr, conn)

# key = input('Silakan masukkan id pegawai yang dicari: ')
# hasil = pgw.cari_pegawai(key)
# print(hasil)

print('*** Silakan memilih menu (1,2) ****')
print('1. Tambah data pegawai \n2. hapus')
menu = input('Menu yang dipilih: ')

if (menu == '1'):
    print('Silakan masukkan data berikut')
    id_pgt = input('id pegawai: ')
    nama = input('nama: ')
    alamat = input('alamat: ')
    em = input('email: ')
    pgt.tambah(id_pgt, nama, alamat, em)

if (menu == '2'):
    id_hapus = input('masukkan id pegawai yang akan dihapus: ')
    pgt.hapus(id_pgt)