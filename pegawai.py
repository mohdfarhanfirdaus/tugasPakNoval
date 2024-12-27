
class pengikut:
    def __init__(self, conn, cursor):
        self.cur = cursor
        self.conn = conn

    def cari_pengikut(self, id):
        self.cur.execute('SELECT * FROM pengikut WHERE id_pegawai ='+ id) 
        result = self.cur.fetchall()
        return result

    def tambah (self, id, nama, alamat, email):
        print('Menambahkan data pengikut...')
        query = 'INSERT INTO pengikut (id_pegawai, nama, alamat, email) VALUES ("' + id +'","'+ nama +'","'+alamat + '","'+email+'")';
        self.cur.execute(query)      
        self.conn.commit()
        # print('Query:', query)
        print('Proses penambahan selesai')

    def hapus(self, id):
        print('Menghapus data pengikut...')
        query = 'DELETE FROM pengikut WHERE id_pegawai'
        self.cur.execute(query, (id,))
        self.conn.commit()
        print('Proses penghapusan selesai')
        # print('Query:', query)
        pass
    
    def update_alamat(self, id, alamat):
        print('Memperbarui alamat pengikut...')
        query = 'UPDATE Pegawai SET (id_pegawai, alamat,) VALUES ("' + id +'","'+ alamat + '",)'
        self.cur.execute(query, (alamat, id))
        self.conn.commit()
        print('Proses pembaruan alamat selesai')
         # print('Query:', query)
        pass
