'''
Author  : Fahman
Program : Latihan5.py
Date    : 8/7/2014
Purpose : Perulangan menggunakan fungsi 'for' dan 'while'
'''

#Perulangan menggunakan for
#for digunakan dalam list [n] kali
for i in [1,2,3,4,5]:
    print 'ini adalah pengulangan ke - ', i

for makanan in ["Rawon","Nasi Kuning","Soto Madura","Kupat Tahu","Kerak Telor", "Rendang Batoko", "Pempek Selam", "Ayam Betutu"] :
    print makanan, " adalah makanan khas nusantara"

'''
Menggunakan fungsi 'range'
Range ini menghasilkan deret angka dengan parameter (start, stop, step). Start adalah batasawal dari list,
stop adalah batas akhir dari  list, step  adalah jarak antar angka yang dihasilkan oleh  range.  Ada beberapa kasus 
penting yang perlu diperhatikan saat menggunakan range

# kasus - 1 : jika step tidak disertakan maka step akan diisi 1 secara default
print range(1, 10)
# kasus - 2 : jika step disertakan maka step akan sesuai dengan angka yang diisikan
print range(1, 10, 2)
print range(1, 10, 3)
print range(1, 10, 4)
print range(1, 10, 5)
# kasus - 3 : jika step melebihi stop maka list hanya akan berisi start
print range(1, 10, 11)
# kasus - 4 : jika start lebih besar nilainya daripada stop maka list akan kosong
print range(10, 1)
# kasus - 5 : jika start lebih besar nilainya daripada stop dan
# jika step melebihi stop maka list akan kosong
print range(10, 1, 2)
print range(10, 1, 11)
# kasus - 6 : jika start lebih besar daripada stop dan step bernilai minus 
# dan jika start dikurangi step menghasilkan angka positif
# maka list akan berisi deret angka menurun
print range(10, 1, -1)
# kasus - 7 : jika start lebih besar daripada stop dan step bernilai minus 
# dan jika start dikurangi step bernilai minus maka list hanya akan berisi start
print range(10, 1, -11)
# kasus - 8 : jika step bernilai 0 maka akan terjadi error
print range(1, 10, 0)
# kasus - 9 : jika start lebih besar daripada stop dan step bernilai 0 maka akan terjadi error
print range(10, 1, 0)
'''

#perulangan menggunakan fungsi 'range' ke-1
for a in range(1,10):
    print 'tes ke - ', a

#perulangan menggunakan fungsi 'range' ke-2
for k in range(0,10):
    for l in range(0,k+1):
        if l == k:
            print "*"
        else:
            print "^",
    print ""

#perulangan menggunakan fungsi 'range' ke-3
#menampilkan bilangan prima (bilangan yang bisa dibagi 1 dan bilangan itu sendiri)
for i in range(1, 20):
    count_zero_remainder = 0
    for j in range(1, i+1):
        num_remainder = i % j
        
        #print num_remainder,
        if num_remainder == 0:
            count_zero_remainder = count_zero_remainder + 1
    
    if count_zero_remainder == 2:
        print i, " adalah bilangan prima"
    else:
        print i, " bukanlah bilangan prima"

#perulangan menggunakan fungsi 'while' ke-1
angka = 0
while(angka < 10):
    print "saya sudah maju sejauh ", angka," meter"
    angka += 1


#perulangan menggunakan fungsi 'while' ke-2
tanya = True
while tanya:
    temp = raw_input("masukan angka kurang dari 10: ")
    angka = int(temp)
    if angka < 10:
        if tanya == False:
            hasil = "Salah"
            print "Hasilnya : ", hasil
    else :
        if tanya == True:
            hasil = "Benar"
            print "Hasilnya : ", hasil

#perulangan menggunakan fungsi 'while' ke-3
i = 1
jml_angka = 0
while i <= 10:
    print 'loop ke - %d : %d + %d' % (i, jml_angka, i)
    jml_angka = jml_angka + i
    i += 1
print 'total angka yang dijumlahkan : ', jml_angka
    
