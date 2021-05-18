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
teks = "\nNama: {}\nUmur: {}\nAlamat: {}\nStatus: {}\nNama Instansi: {}\nProgram Studi: {}".format(nama,umur,alamat,status,nama_instansi,prodi)
# buka file untuk ditulis
file_bio = open("biodata.txt","a")

file_bio.write(teks)

file_bio.close()