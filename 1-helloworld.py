#TUGAS 1
#BUAT OUTPUT YANG MENAMPILKAN TULISAN HELLO WORLD DIBAWAH
print('Program menghitung volume')
p = int(input('masukan panjang : '))
l = int(input('masukan lebar : '))
t = int(input('masukan tinggi : '))

def volume(p,l,t):
    V = p * l * t
    return V

print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{} \nMempunyai volume:{}'.format(p,l,t, volume(p,l,t)))
