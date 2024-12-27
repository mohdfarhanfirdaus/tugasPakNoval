from koneksiDB import * 
from pegawai import *

#buat objek koneksi
dbku = MyDB()
conn_dbku, cur_dbku = dbku.connect()

#buat objek pengikut1, set connection dan cursor yang diambil nilainya dari objek dbku
tbl_pengikut = pengikut(conn=conn_dbku, cursor=cur_dbku)

#menambahkan data pada tabel pengikut
tbl_pengikut.tambah('4', 'putra', 'Batam Center', 'ptr@uib.ac.id')
