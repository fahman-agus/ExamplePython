'''
Author  : Fahman
Program : Latihan2.py
Date    : 8/7/2014
Purpose : Menerima Input dari keyboard menggunakan fungsi raw_input()
'''

#menggunakan function raw_input()
nama = raw_input('masukkan nama : ')
tinggi = raw_input('tinggi badan : ')
berat = raw_input('berat badan : ')

#cetak dari variable yang sudah ditampung diatas
print "Nama anda adalah ", nama
print "tinggi badan anda adalah %d cm" %int(tinggi)
print "Berat badan anda adalah %d Kg" %int(berat)

#hitung ideal ukuran sepatu
ideal = int(tinggi) % int(berat)

print "Ukuran ideal adalah %d " % (ideal)
print "Semua ukuran datanya : (tinggi : %d) (Berat : %d) (ideal : %d)" % (int(tinggi), int(berat), ideal)
