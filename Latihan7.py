'''
Author  : Fahman
Program : Latihan7.py
Date    : 8/7/2014
Purpose : membuat function (def)
'''

#membuat function tanpa return
#pada outputnya akan menampilkan 'none' diakhir eksekusi fungsi
def fungsi_tanpa_parameter():
	for i in range(1,5):
		print "Looping ke- ",i

def fungsi_berparameter(batas_akhir):
	for i in range(1, batas_akhir):
		print "Looping ke- ", i

print "Contoh penggunaan fungsi tanpa parameter : "
print "Hasilnya : \n", fungsi_tanpa_parameter()

print "\n\n"

print "Contoh penggunaan fungsi berparameter : "
print "Hasilnya : \n", fungsi_berparameter(10)

#membuat fungsi menggunakan return
def fungsi_non_parameter():
	temp = 0
	for i in range(1,5):
		temp = temp + i
	return temp

def fungsi_parameter(param):
	temp = 0
	for i in range(1, param):
		temp = temp + i
	return temp

print " contoh penggunaan fungsi tanpa parameter : "
print "hasil : ", fungsi_tanpa_parameter()
print "hasil : ", fungsi_tanpa_parameter()
print "hasil : ", fungsi_tanpa_parameter()
print "\n\n"
print " contoh penggunaan fungsi berparameter : "
print "hasil : ", fungsi_berparameter(15)
print "hasil : ", fungsi_berparameter(20)
print "hasil : ", fungsi_berparameter(25)

#penggunaan default argument dalam membuat function
def cek_biodata(nama, kota, umur=20):
	print "Nama :", nama;
	print "Umur :", umur;
	print "Kota :", kota;
	return;

#kalau parameter diisi semua
print "Tanpa menggunakan default argument: "
cek_biodata(nama="fahman",umur=50,kota="Jakarta")

print "\n"

#jika parameter tidak diisi semua
print "menggunakan default argument :"
cek_biodata(kota="jakarta",nama="agus")

#contoh menggunakan variable-length argument
def cetak_perolehan_nilai(nama, twitter, *scores):
	print "Nama : ", nama;
	print "Twitter : ", twitter;
	print "Score yang diperoleh : "
	i = 1
	for score in scores:
		print "nilai ke- %d : %d" %(i,score)
		i += 1

	return;

#kalau parameter diisi semua
print "Dengan adanya variable-length variabel sisa akan menjadi tuple : "
cetak_perolehan_nilai("Silvy", "@sivlysiv", 90, 80, 70, 80, 90)

'''
keyword argument pada function
'''
def cetak_biodata(names,city,age):
	print "Name : ", names;
	print "City : ", city;
	print "Age  : ", age;
	return;

# kalau pakai keyword argument : mau urutannya gimanapun input akan sesuai
print "Tanpa memakai keyword argument : " 
cetak_biodata(names="miki", city="bandung", age=50 )
print "\n"
# kalau tidak memakai keyword argument : mau urutannya gimanapun input tidak akan sesuai
print "Memakai keyword argument : "
cetak_biodata( "bandung", "miki", 50)
print "\n"
# kalau tidak memakai keyword argument : tapi urutannya sesuai maka input  akan sesuai
print "Memakai keyword argument : tapi urutannya sesuai "
cetak_biodata(  "miki", 50, "bandung")

'''
keyword length pada fucntion
'''
def cek_perolehan_nilai( nama, twitter, **data_tambahan):
   print "Nama : ", nama;
   print "Twitter : ", twitter;
   print "\n"
   print "Data Lainnya : "
   i = 1
   for data in data_tambahan:
       print "%s : %s" % (data, data_tambahan[data])
   return;

# kalau parameter diisi semua
print "Dengan adanya keyword argument, argumen tersisa akan menjadi dictionary : "
cek_perolehan_nilai("Silvy","@sivlysiv",email="silvysilvy@gmail.com", facebook="www.facebook.com/silvysil", telp="0838-1234-5678")

'''
contoh pass by value atau pass by reference
'''
print "\n\n"

def sebuah_fungsi(sebuah_list):
    sebuah_list = [1, 2, 3, 4, 5]
    print sebuah_list
    return;
    
def sebuah_fungsi_lainnya(sebuah_list):
    sebuah_list.append([10, 20, 30])
    print sebuah_list
    return;

ini_list = [10, 20, 30]
sebuah_list = [100, 200, 300]
print "apakah ini_list berubah ? "
print "1", ini_list
sebuah_fungsi(ini_list)
print "2", ini_list
print "3", ini_list
sebuah_fungsi_lainnya(ini_list)
print "4", ini_list
print "apakah sebuah_list berubah ? "
print "5", sebuah_list
sebuah_fungsi(sebuah_list)
print "6", sebuah_list
print "7", sebuah_list
sebuah_fungsi_lainnya(sebuah_list)
print "8", sebuah_list

'''
variable scope lokal & global
'''
print "\n\n"
def sebuah_fungsi():
    angka =  10
    print "di dalam sebuah_fungsi, angka bernilai : ", angka
def sebuah_fungsi_lainnya():
    global angka
    angka = 114
    print "di dalam sebuah_fungsi, angka bernilai : ", angka
    
angka = 6666
print "sebelum dipanggil sebuah_fungsi : ", angka
sebuah_fungsi()
print "sesudah dipanggil sebuah_fungsi : ", angka
print "\n\n"
print "sebelum dipanggil sebuah_fungsi_lainnya : ", angka
sebuah_fungsi_lainnya()
print "sesudah dipanggil sebuah_fungsi_lainnya : ", angka