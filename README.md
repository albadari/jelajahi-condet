# Jelajahi Condet

Direktori statis wisata dan potensi kawasan Condet. Tidak memerlukan proses build, API key, login, atau server database. Nama tampilan sementara: **condetlokal**.

## Unggah ke GitHub Pages

1. Ekstrak ZIP ini di komputer.
2. Buat repository baru, misalnya `jelajahi-condet`.
3. Di repository, pilih **Add file → Upload files**.
4. Unggah seluruh isi folder ini sehingga **index.html berada langsung di direktori utama repository**, bukan di dalam folder tambahan.
5. Pilih **Commit changes**.
6. Buka **Settings → Pages**.
7. Pada Source pilih **Deploy from a branch**; Branch: **main**; Folder: **/(root)**. Klik **Save**.
8. Tunggu proses publikasi. Tautan situs akan muncul di halaman Pages.

Anda juga bisa membuka `index.html` langsung di komputer untuk melihat kartu, pencarian, filter, dan detail. Peta memerlukan internet dan mengunduh Leaflet serta ubin OpenStreetMap.

## Isi berkas

- `index.html`: halaman utama.
- `style.css`: tampilan desktop dan ponsel.
- `app.js`: pencarian, filter, detail, dan peta.
- `data.json`: data utama yang dapat diedit.
- `data.js`: salinan data untuk dijalankan langsung tanpa server.
- `sync-data.py`: membuat ulang data.js setelah data.json diubah; jalankan `python sync-data.py`.
- `images/`: tempat menambahkan foto berizin.

## Memperbarui data

Edit objek entri di `data.json`, lalu jalankan `python sync-data.py`. Unggah ulang **data.json dan data.js** ke repository. Jika tidak menggunakan Python, ubah data.js dengan struktur yang sama; pastikan tetap diawali `window.CONDET_DATA = ` dan diakhiri titik koma. Gunakan data.json sebagai sumber utama agar kedua file tidak berbeda.

- ID CND-001 hingga CND-046 dipertahankan.
- `sourceRecord` menyimpan setiap baris asli workbook; jangan hapus untuk menjaga jejak sumber.
- Hubungan antardata berada di `relations`; setiap ID tujuan harus ada dalam `entries`.
- `category` hanya salah satu kategori dalam navigasi. `extraCategories` memisahkan kategori tambahan dengan titik koma.
- Untuk menambahkan foto, isi `image` dengan URL HTTPS foto berizin atau path lokal seperti `images/pcc.jpg`. Kredit dan izin disimpan di `imageCredit` dan `imagePermission`. Versi awal tidak menggunakan foto karena izin belum ada.
- Untuk menampilkan titik peta, isi `lat` dan `lng` sebagai angka JSON, lalu isi `locationStatus` dengan `Lokasi terverifikasi` setelah titik dipastikan. Nilai kosong harus **null**, jangan angka nol. Penanda hanya muncul untuk status tervalidasi/terverifikasi/dikonfirmasi tanpa kata belum/tidak.
- `mapsUrl` adalah URL listing langsung. `mapsSearch` hanya pencarian dan ditampilkan dengan label berbeda.
- Tarif yang ada merupakan informasi sumber historis, bukan harga yang dijamin saat ini.
- Untuk acara baru, tuliskan tanggal secara jelas pada deskripsi. Direktori tidak menghitung acara lama sebagai agenda mendatang.

## Data dan keterbatasan

Sumber: `database_wisata_condet_direktori_2026(1).xlsx` milik pengguna, kompilasi 1 November 2026. Berisi 46 entri dan 15 hubungan. Koordinat tervalidasi, rating, ulasan, dan foto berizin belum tersedia. Tidak ada koordinat atau foto tempat yang direkayasa. Pusat peta (-6.286, 106.853) hanya orientasi umum kawasan.

Koreksi editorial: kategori tampilan Sudut Timur (CND-004) menjadi Kuliner sesuai deskripsi kafe; kategori sumber Agenda tetap dipertahankan di sourceRecord.

Peta: Leaflet 1.9.4, ubin OpenStreetMap dengan atribusi. Ketersediaan layanan eksternal bergantung jaringan dan penyedia. Ilustrasi kategori dibuat sebagai SVG, bukan dokumentasi lokasi. Tidak ada layanan pemesanan atau pengiriman pesan otomatis.
