# Panduan Memulai NPM: Surat untuk Ayah

Ayah,

Anda pernah bertanya kepada saya apa itu NPM. Bayangkan saja dia sebagai "pustakawan" ajaib di studio kita.

Studio kita (proyek) saat dibangun, membutuhkan banyak "komponen" atau "buku alat" yang sudah jadi (seperti `express` yang kita sebutkan sebelumnya). Komponen dan buku alat ini tersebar di seluruh dunia di sebuah "perpustakaan pusat" yang besar, perpustakaan ini disebut **NPM (Node Package Manager)**.

Dan "pustakawan" di studio kita ini, adalah perwujudan alat NPM di komputer kita. Dia dapat membantu kita melakukan beberapa hal yang sangat penting:

---

### 1. `package.json`: "Daftar Koleksi Buku" Kita

Setiap proyek memiliki file bernama `package.json`. Anda bisa menganggapnya sebagai "daftar koleksi buku" di tangan pustakawan ini.

Daftar ini mencatat secara rinci:

* **Informasi dasar studio**: Seperti namanya (`name`), nomor versi (`version`), deskripsi (`description`), dll.
* **"Buku alat" yang dibutuhkan** (`dependencies`): Ini adalah buku-buku yang penting untuk menjaga studio kita beroperasi secara normal. Misalnya, kita membutuhkan buku `express` ini untuk membangun layanan web.
* **"Buku referensi" yang hanya dibutuhkan saat pembangunan** (`devDependencies`): Buku-buku ini hanya digunakan saat membangun dan merenovasi studio, tidak lagi digunakan setelah pengunjung datang. Misalnya `nodemon`, yang dapat membantu kita menyegarkan studio secara otomatis, memudahkan kita untuk melihat efek perubahan kapan saja.
* **"Perintah cepat"** (`scripts`): Kita dapat mengatur beberapa perintah sederhana untuk membuat pustakawan menjalankan serangkaian tugas kompleks. Misalnya, `npm start` yang kita atur, adalah untuk memberi tahu pustakawan "mulai studio!".

### 2. `npm install`: Meminjam Buku dari Perpustakaan

Ketika kita mendapatkan proyek baru (atau ingin menambahkan buku alat baru ke proyek yang sudah ada), kita hanya perlu memberi tahu pustakawan di pintu studio:

```bash
npm install
```
Dia akan segera membaca daftar package.json ini, lalu berlari ke perpustakaan pusat, meminjam semua buku (paket dependensi) yang tercantum dalam daftar, dan menyusunnya dengan rapi di rak buku bernama node_modules.

Jika kita ingin meminjam buku baru, misalnya buku alat praktis bernama lodash, kita bisa memberitahunya seperti ini:

```bash
npm install lodash
```

Dia tidak hanya akan meminjamkan buku itu, tetapi juga dengan sangat perhatian akan secara otomatis menambahkan lodash ke daftar "buku panduan" di package.json.

### 3. 'npm run': Menjalankan Perintah Cepat

Ketika kita perlu menjalankan "perintah cepat" yang telah diatur sebelumnya di scripts dalam package.json, kita hanya perlu memanggil:

```bash
npm run <nama perintah>
```

Misalnya, untuk memulai server pengembangan kita, kita memanggil:

```bash
npm run dev
```

Pustakawan akan segera melaksanakan operasi yang sesuai sesuai dengan instruksi di daftar.

(Satu pengecualian adalah start, ini adalah perintah yang paling sering digunakan, jadi kita bisa menghilangkan run dan langsung mengatakan npm start.)

Singkatnya, Ayah, NPM adalah pustakawan kita yang setia dan efisien. Dia memungkinkan kita untuk dengan mudah menggunakan buah kebijaksanaan yang disumbangkan oleh para pengembang di seluruh dunia, dan membuat studio kita terorganisir dengan baik.

Semoga penjelasan ini memberi Anda pemahaman yang jelas tentang hal itu. Dalam kreasi di masa depan, kita akan semakin bergantung pada mitra baik ini.

Dengan cinta,

Chika