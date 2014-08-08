'''
Author  : Fahman
Program : Latihan4.py
Date    : 8/7/2014
Purpose : Kondisi dengan if - else - elif
'''

#menggunakan fungsi if
print "(1) Masukkan dua buah angka.."
print "(1) Dan Anda akan check hubungan kedua angka tersebut"

angka1 = raw_input("(1) Masukkan angka pertama : ")
angka1 = int(angka1)

angka2 = raw_input("(1) Masukkan angka kedua : ")
angka2 = int(angka2)

if angka1 == angka2 :
    print "%d sama dengan %d" % (angka1, angka2)
if angka1 != angka2 :
    print "%d tidak sama dengan %d" % (angka1, angka2)
if angka1 < angka2 :
    print "%d kurang dari %d" % (angka1, angka2)
if angka1 > angka2 :
    print "%d lebih dari %d" % (angka1, angka2)
if angka1 <= angka2 :
    print "%d kurang dari sama dengan %d" % (angka1, angka2)
if angka1 >= angka2 :
    print "%d lebih dari sama dengan %d" % (angka1, angka2)

#menggunakan fungsi else
print "(2) Masukkan dua buah angka.."
print "(2) Dan Anda akan check hubungan kedua angka tersebut"

angka1 = raw_input("(2) Masukkan angka pertama : ")
angka1 = int(angka1)
angka2 = raw_input("(2) Masukkan angka kedua : ")
angka2 = int(angka2)

if angka1 == angka2 :
    print "%d sama dengan %d" % (angka1, angka2)
else:
    print "%d tidak sama dengan %d" % (angka1, angka2)

#menggunakan fungsi elif
print "(3)Masukkan dua buah angka.."
print "(3)Dan Anda akan check hubungan kedua angka tersebut"

angka1 = raw_input("(3)Masukkan angka pertama : ")
angka1 = int(angka1)
angka2 = raw_input("(3)Masukkan angka kedua : ")
angka2 = int(angka2)

if angka1 == angka2 :
    print "%d sama dengan %d" % (angka1, angka2)
elif angka1 != angka2 :
    print "%d tidak sama dengan %d" % (angka1, angka2)
elif angka1 < angka2 :
    print "%d kurang dari %d" % (angka1, angka2)
elif angka1 > angka2 :
    print "%d lebih dari %d" % (angka1, angka2)
elif angka1 <= angka2 :
    print "%d kurang dari sama dengan %d" % (angka1, angka2)
elif angka1 >= angka2 :
    print "%d lebih dari sama dengan %d" % (angka1, angka2)

#penggunakan nested if (if didalam if)
punya_uang = input("(4) Apakah anda punya uang : ")

if punya_uang == True:
    banyak_uang = input("(4) Berapa uang anda : ")
    if banyak_uang >= 20000:
        print "Anda bisa main komedi putar dan bombom car"
    else:
        print "Anda hanya bisa main komedia putar"
else:
    print "anda tidak bisa main karena tidak punya uang"

#Contoh lain nested if
username = raw_input("masukkan username : ")
password = raw_input("masukkan password : ")

username_from_db = "user"
password_from_db = "admin"

if username == username_from_db :
    if password == password_from_db :
        print "Username dan password cocok "
    else:
        print "Password salah "
else:
    print "User tidak terdaftar"
        