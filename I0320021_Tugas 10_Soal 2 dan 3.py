print ("SELAMAT DATAG DI PROGRAM BIODATA ")
print ("=================================")

#Mengambil input dari user
nama = input("Nama          : ")
umur = input("Umur          : ") #Umur dalam tahun
alamat = input("Alamat        : ")
hobi = input("Hobi          :")
bulan_lahir = input
status = input ("status        : ") #Pelajar/Mahasiswa/Pekerja
nama_instansi = input ("Nama Instansi : ")
prodi = input("Program Studi : ")


#format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}\nStatus: {}\nNama Instansi: {}\nProgram Studi: {}".format(nama,umur,alamat,status,nama_instansi,prodi)
# buka file untuk ditulis
file_bio = open("biodata.txt","w")

file_bio.write(teks)

file_bio.close()


#Menyisipkan data
print ("SELAMAT DATAG DI PROGRAM BIODATA ")
print ("=================================")

#Mengambil input dari user
nama = input("Nama          : ")
umur = input("Umur          : ") # Dalam Tahun
alamat = input("Alamat        : ")
status = input ("status        : ") # Pelajar/Mahasiswa/Pekerja
nama_instansi = input ("Nama Instansi : ")
prodi = input("Program Studi : ")

#format teks
teks = "\n\nNama: {}\nUmur: {}\nAlamat: {}\nStatus: {}\nNama Instansi: {}\nProgram Studi: {}".format(nama,umur,alamat,status,nama_instansi,prodi)
# buka file untuk ditulis
file_bio = open("biodata.txt","a")

file_bio.write(teks)

file_bio.close()