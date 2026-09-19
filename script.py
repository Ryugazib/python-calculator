angka_pertama = input ('masukkan angka pertama: ')
angka_kedua = input ('masukkan angka kedua: ')
operasi_bilangan = input ('oprasi bilangan kali, bagi, tambah, kurang: ')

if operasi_bilangan == 'kali':
    print (int(angka_pertama) * int(angka_kedua))

elif operasi_bilangan == 'bagi':
    if float(angka_kedua) == 0:
        print ('tidak bisa melakukan pembagian dengan 0.')
    else:
        print (float(angka_pertama) / float(angka_kedua))

elif operasi_bilangan == 'tambah':
    print (int(angka_pertama) + int(angka_kedua))

elif operasi_bilangan == 'kurang':
    print (int(angka_pertama) - int(angka_kedua))
else:
    print ('maaf operasi bilangan tidak sesuai.')
