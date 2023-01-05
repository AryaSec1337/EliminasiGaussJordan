# Author Arya Alfahrezy
# Kikiwww kodeeexxx


#membuat matriks default
matriks_tersimpan = [1,1,1,1],[1,1,1,1],[1,1,1,1]

#membuat fungsi untuk menampilkan hasil
def akhir(): 
    print("X = {}".format(matriks_tersimpan[0][3]))
    print("Y = {}".format(matriks_tersimpan[1][3]))
    print("Z = {}".format(matriks_tersimpan[2][3]))
    print("Selamat, Soal terpecahkan!!!")

#membuat fungsi untuk menampilkan matriks
def tampil_matriks(matriks,bagian):
    print("========================")
    print("Matriks {}".format(bagian))
    for a in range(3):
        for b in range(4):
            print(" {} ".format(matriks[a][b]),end="")
            if b == 3:
                print("")

#Fungsi untuk merubah nilai matriks menjadi 1
def jadi_1(matriks,baris,kolom):
    print("========================")
    print("Mengubah baris {} kolom {} menjadi 1".format(baris+1,kolom+1))
    tampil_matriks(matriks,"awal")
    print("==Menghitung setiap kolom pada baris {}".format(baris+1))
    k = 1/matriks[baris][kolom]
    for a in range(4):
        hsl = k*matriks[baris][a]
        print("{} x {} = {}".format(k,matriks[baris][a],hsl))
        matriks[baris][a]=hsl
    tampil_matriks(matriks,"matriks baru")  

#Fungsi untuk merubah nilai matriks menjadi 0
def jadi_nol(matriks,baris,kolom,baris_ac):
    print("========================")
    print("Mengubah baris {} kolom {} menjadi 0".format(baris+1,kolom+1))
    tampil_matriks(matriks,"awal")
    print("==Menghitung setiap kolom pada baris {}".format(baris+1))
    b2=matriks[baris][kolom]
    k = b2-(b2+b2)
    for a in range(4):
        hsl = matriks[baris][a] + (k*matriks[baris_ac][a])
        print("{} + ({} x {}) = {}".format(matriks[baris][a],k,matriks[baris_ac][a],hsl))
        matriks[baris][a]=hsl
    tampil_matriks(matriks,"matriks baru")

#fungsi untuk urutan menghitung, berdasarkan acuan baris 1
def acuan_br1(matriks):
    jadi_nol(matriks,1,0,0);jadi_nol(matriks,2,0,0);jadi_1(matriks,1,1);jadi_nol(matriks,0,1,1);jadi_nol(matriks,2,1,1)
    jadi_1(matriks,2,2);jadi_nol(matriks,0,2,2);jadi_nol(matriks,1,2,2);akhir()

#fungsi untuk urutan menghitung, berdasarkan acuan baris 2
def acuan_br2(matriks):
    jadi_nol(matriks,0,1,1);jadi_nol(matriks,2,1,1);jadi_1(matriks,0,0)
    jadi_nol(matriks,1,0,0);jadi_nol(matriks,2,0,0);jadi_1(matriks,2,2);jadi_nol(matriks,0,2,2);jadi_nol(matriks,1,2,2);akhir()

#fungsi untuk urutan menghitung, jika tidak ada acuan
def tidak_ada_satu(matriks):
    jadi_1(matriks,0,0);jadi_nol(matriks,1,0,0);jadi_nol(matriks,2,0,0);jadi_1(matriks,1,1);jadi_nol(matriks,0,1,1)
    jadi_nol(matriks,2,1,1);jadi_1(matriks,2,2);jadi_nol(matriks,0,2,2);jadi_nol(matriks,1,2,2);akhir()

#fungsi untuk urutan menghitung, berdasarkan acuan baris 3
def acuan_br3(matriks):
    jadi_nol(matriks,0,2,2)
    jadi_nol(matriks,1,2,2)
    jadi_1(matriks,0,0)
    jadi_nol(matriks,1,0,0)
    jadi_nol(matriks,2,0,0)
    jadi_1(matriks,1,1)
    jadi_nol(matriks,0,1,1)
    jadi_nol(matriks,2,1,1)
    akhir()

def main():
    print("""
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  \033[1;36mAtut ada T-Rexx\n
    """)
    print("\033[1;31m=============================================\n")
    print("\033[1;37m Menghitung Matriks dengan Metode Gauss Jordan\n")
    print("\033[1;31m=============================================\n")
    print("\033[1;36m Code By      : Tengku Arya Saputra\n")
    print("\033[1;36m Prodi        : Teknik Informatika\n")
    print("\033[1;36m Pemrograman  : Python\n")
    print("\033[1;31m=============================================\n")
    benar = 3
    while benar == 3:
        baris = int(input("\033[1;37m Ada berapa baris matriks : "))
        kolom = int(input("Ada berapa kolom matriks : "))
        if baris != benar and kolom != 4:
            print("Inpu tidak valid maksimal baris adalah 3, dan maksimal kolom adalah 4")
        else:
            benar = 4

    for a in range(baris):
        for b in range(kolom):
            isi = int(input("Masukkan nilai baris {} kolom {} : ".format(a+1,b+1)))
            matriks_tersimpan[a][b] = isi
    if matriks_tersimpan[0][0] == 1:
        acuan_br1(matriks_tersimpan)
    elif matriks_tersimpan[1][1] == 1:
        pass
    elif matriks_tersimpan[2][2] == 1:
        acuan_br3(matriks_tersimpan)
    else:
        tidak_ada_satu(matriks_tersimpan)

if __name__=="__main__":
    main()
