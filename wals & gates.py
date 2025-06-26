# Penjelasan dasar
'''
bayangkan kita berada di dalam sebuah gedung besar yang memiliki:
* beberapa ruangan kosong (belum diketahui jaraknya ke mana-mana),
* beberapa tembok (tidak bisa dilewati),
* Dan beberapa gerbang (tempat keluar-masuk).

tugas kita adalah:
untuk setiap ruangan kosong, isi dengan angka berapa langkah tercepat (jarak terpendek) menuju gerbang terdekat.


analogi sederhana:
Bayangkan kamu berada di sebuah mall besar. Banyak ruangan kosong, dan ada beberapa pintu keluar (gerbang).

Tugas kamu adalah:
* Menentukan berapa langkah tercepat untuk keluar dari posisi mana pun kamu berada.
* Tapi kamu tidak bisa menembus dinding (tembok).

agar adil dan cepat, kita membunyikan alarm dari semua pintu keluar secara bersamaan, dan gelombangnya menyebar ke semua arah. Siapapun yang mendengar alarm pertama kali, itu berarti itu adalah jalur tercepat ke pintu.


Algoritma Breadth-First Search (BFS):
untuk menyelesaikan masalah ini, kita menggunakan algoritma Breadth-First Search (BFS), yaitu algoritma yang menyebar dari titik awal ke semua arah, selangkah demi selangkah.

Kenapa BFS?
* Karena BFS selalu menemukan jalur terpendek saat menyebar.
* Kita bisa memproses semua gerbang secara bersamaan.
* Setiap langkah akan mengisi tetangganya dengan jarak +1.

Struktur Data yang Digunakan:
* INF : nilai besar (2147483647) untuk menandai ruangan kosong.
* -1 : tembok, tidak bisa dilewati.
* 0 : gerbang, titik awal BFS.
* deque : struktur antrian untuk BFS.

Kesimpulan:
* Masalah ini nyata di banyak game, robotik, dan aplikasi pemetaan ruangan.
* Dengan BFS, kita bisa menyebar secara adil dan efisien dari semua titik gerbang.
* Implementasi Python ini mudah dimengerti jika kita pahami analoginya sebagai penyebaran suara alarm dari pintu keluar.

'''
# implementasi program:

from collections import deque 
    # from collections import deque adalah sebuah pernyataan impor dalam python.
    # artinya kita mengambil (mengimpor) sebuah kelas atau tipe data bernama deque dari modul yang lebih besar bernama collections.

    # secara bahasa from adalah dari.
    # collections adalah salah satu library yang dipilih/digunakan dalam program ini.
    # library itu sendiri adalah tempat yang memiliki banyak sekali alat.
    # analoginya, library itu seperti sebuah ruangan yang menyimpan banyak alat.
    # import yang berarti kita mengambil (mengimport) suatu alat dari library yang kita gunakan.
    # deque adalah "alat" yang diambil dari library itu.

INF = 2147483647
    # diprogram ini kita buat variabel yang namanya INF(inituh singkatan dari bahasa ingris infinity/tak terhingga), yang menyimpan nilai 2147483647,
    # emang apa sih 2147483647 itu? nah jadi, 2147483647 itu bukan angka ngasal, ini tuh berarti nilai yang besar banget,
    # karna di beberapa program biasanya butuh nilai ini dengan tujuan mencari jalur yang jarak awalnya kita ngga tau dan nyari nilai minimum.
    # jadi, nilai 2147483647 digunakan untuk merepresentasikan jarak yang sangat jauh atau belum terjangkau atau jarak yang belum diketahui,
    # sehingga jaraknya untuk sementara waktu dianggap "tak terhingga".

peta = [
    [INF, -1,   0,    INF],
    [INF, INF, INF,  -1],
    [INF, -1,  INF,  -1],
    [0,   -1,  INF,  INF]
]
    # diprogram ini kita buat variabel yang namanya peta, dia adalah sebuah matrix 2d yang isinya nyimpen daftar/nilai" yg ngewakilin setiap keadaan disetiap ruangan. 
    # ada 3 keadaan diprogram ini,
    # 1. INF (2147483647) → artinya ruangan kosong, belum ada jarak yang diketahui.
    # 2. -1 → artinya tembok, tidak bisa dilewati.
    # 3. 0 → artinya gerbang (gate), titik awal.

def isi_jarak_dari_gerbang(peta):
    # disini kita membuat 1 fungsi (def) yang bernama isi_jarak_ke_gerbang, yang dimana fungsi ini mengambil nilai parameter dari peta (peta):
    # parameter itu kaya sebuah variable yang punya nilai (diprogram ini, variabel itu punya nila dari peta), kata lainnya parameter ini buat ngewakilin
    # nilai yang dibutuhin fungsi isi_jarak_ke_gerbang (peta gituuu), ohiyaa parameter ini juga berguna banget buat si program, karna tanpa parameter (khususnya diprogram ini)
    # fungsi program ga akan jalan.
   
    if not peta or not peta[0]:
        return
        # pada kode if not peta or not peta[0]:, artinya fungsi inituh ngecek jika bukan peta atau bukan peta index/urutan pertama (if not peta or not peta[0]:),
        # dia akan mengembalikan hasilnya(return),
        # kenapa [0]? karna didalam bahasa pemrograman index pertama itu berawal dari 0.

    jumlah_baris = len(peta)
    jumlah_kolom = len(peta[0])
    antrian = deque()
        # diprogram ini kita buat variabel yang namanya jumlah_baris, yang menyimpan nilai jumlah baris dalam peta (len(peta)). len itu fungsinya menghitung jumlah item (panjang) dari sebuah objek (peta).
        # diprogram ini kita buat variabel yang namanya jumlah_kolom, yang menyimpan nilai jumlah kolom dalam peta (len(peta[0])). penjelasannya sama, cuma bedanya di index nya doang.            
        # diprogram ini kita buat variabel yang namanya antrian, yang menyimpan nilai deque/objek yang masih kosong (deque()),
        # deque tuh apa sih? jadi, deque itu kan "alat" yang diambil dari library collections,
        # diatuh kaya objek antrian yang dimana kita bisa tambah atau hapus objek itu dari ke 2 ujung pake deque ini,
        # kenapa kita pake deque? karna program ini tuh salah satu bentuk implementasi dari algoritma BFS untuk menemukan jarak.
    
    for baris in range(jumlah_baris):
        # for baris in range(jumlah_baris):
        # Ini adalah perulangan untuk setiap baris dalam peta.
        # kan diprogram ini jumlah_baris = 4, maka baris akan bernilai 0, 1, 2, 3 secara bergantian.
        for kolom in range(jumlah_kolom):            
            # for kolom in range(jumlah_kolom):
            # Perulangan untuk setiap kolom dalam baris yang sedang diproses.
            # diprogram ini jumlah_kolom = 4, maka kolom akan bernilai 0, 1, 2, 3.
            if peta[baris][kolom] == 0:
                # if peta[baris][kolom] == 0:
                # ngecek apakah isi dari peta[baris][kolom] adalah gerbang (0).
                # Kalo iya, berarti ini titik awal BFS.
                antrian.append((baris, kolom))
                    # antrian.append((baris, kolom))
                    # tambahin posisi (baris, kolom) ke dalam antrian deque.
                    # artinya kita menyimpen titik gerbang ke dalam antrian buat diproses.

    
    arah_gerakan = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # disini kita bikin variable namanya arah_gerakan, yang isinya tuple (x,y),
        # masing" tuple ngewakilin arah gerakan (dalam bentuk koordinat relatif),
        # 1. (-1, 0) → ke atas (baris berkurang 1)
        # 2. (1, 0) → ke bawah (baris bertambah 1)
        # 3. (0, -1) → ke kiri (kolom berkurang 1)
        # 4. (0, 1) → ke kanan (kolom bertambah 1)
        # kenapa harus pake/buat ini? karna ini penting buat menjelajah 4 arah dari satu titik ke titik yg lainnya (karna bentuknya peta matrix/grid).
    
    while antrian:
        baris, kolom = antrian.popleft()
            # while antrian: → artinya selama masih ada item dalam antrian, maka teruskan prosesnya.
            # antrian.popleft() akan mengambil dan menghapus elemen pertama dari deque (FIFO), sesuai logika antrian.
            # baris, kolom akan menyimpan koordinat saat ini yang sedang diproses dari deque.
            # ini bagian utama dari algoritma Breadth-First Search (BFS).

        for gerak_vertikal, gerak_horizontal in arah_gerakan:
             # perulangan untuk mencoba semua arah dari titik (baris, kolom) yang sedang diproses.
             # gerak_vertikal dan gerak_horizontal digunakan sebagai penyesuaian arah dari titik sekarang ke titik lainnya (posisi sekarang ke posisi tetangga).

            baris_baru = baris + gerak_vertikal
            kolom_baru = kolom + gerak_horizontal
                # kita itung koordinat titik lain (tetangga) dari titik (posisi) sekarang dengan menambahkan gerak ke baris dan kolom.

            if 0 <= baris_baru < jumlah_baris and 0 <= kolom_baru < jumlah_kolom:
                # disini kode ngecek batas.
                # supaya kita nggak keluar dari area peta waktu mencoba gerak dari titik satu ke titik lainnya.
                # dicek apakah koordinat baris dan kolom yang baru masih dalam batas indeks peta.
                
                if peta[baris_baru][kolom_baru] == INF:
                    # ini kita proses ruang kosong (INF), karna ruang yg bukan INF (misalnya -1 = tembok, atau udah berisi angka = sudah dikunjungi) tidak perlu diproses ulang lagi.

                    peta[baris_baru][kolom_baru] = peta[baris][kolom] + 1
                    # Di sini jarak diisi:
                    # misalnya titik awal adalah 0, maka tetangganya akan diisi 1, lalu tetangganya lagi 2, dst.
                    # ini cara mengisi jarak minimum dari gerbang ke ruangan kosong.
                    # karna BFS itu mencari jalur tercepat, maka jarak yang ditulis adalah yang paling optimal (terpendek).
                    
                    antrian.append((baris_baru, kolom_baru))
                    # titik baru yang valid tadi dimasukkan ke antrian untuk diproses di iterasi selanjutnya.
                    # proses ini akan terus berjalan sampai seluruh ruangan kosong yang bisa dijangkau dari gerbang sudah diisi dengan jarak.

print("\n")

print("Peta sebelum dihitung jarak dari gerbang:")
for baris in peta:
    print(baris)
    # ini bagian untuk menampilkan peta sebelum semua jarak diisi.
    # for baris in peta: → artinya mencetak setiap baris satu per satu.

print("\n")

isi_jarak_dari_gerbang(peta)
    # ini adalah pemanggilan fungsi isi_jarak_dari_gerbang, dengan input berupa peta.
    # artinya program sekarang akan mulai menghitung dan mengisi semua jarak dari gerbang.

print("Peta setelah dihitung jarak dari gerbang:")
for baris in peta:
    print(baris)
    # ini bagian untuk menampilkan hasil akhir dari peta setelah semua jarak diisi.
    # for baris in peta: → artinya mencetak setiap baris satu per satu.
