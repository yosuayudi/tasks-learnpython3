#TUGAS 3
#BUAT PERHITUNGAN RUMUS VOLUME PERSEGI PANJANG MENGGUNAKAN PYTHON, MASING-MASING NILAI VARIABEL DIINPUTKAN COMMAND KEMUDIAN KETIKA KODE DIEKSEKUSI MAKA AKAN MENAMPILKAN HASIL DARI PERHITUNGAN TADI
# RUMUS VOLUME = PANJANG X LEBAR X TINGGI
# BUAT VARIABEL SESUAI YANG DIBUTUHKAN DALAM VARIABEL TERSEBUT
print('Program menghitung volume')
p = int(input('masukan panjang : '))
l = int(input('masukan lebar : '))
t = int(input('masukan tinggi : '))

def volume(p,l,t):
    V = p * l * t
    return V

print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{} \nMempunyai volume:{}'.format(p,l,t, volume(p,l,t)))
