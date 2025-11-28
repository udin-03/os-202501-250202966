
# Laporan Praktikum Minggu 7
Topik:  Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas Kelompok

| Nama | NIM |
| :--- | :--- |
| Ahmad Wildan Asrovi  | 250202927 |
| April Triadi | 250202930 |
| Safrudin | 250202966 |

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- Mahasiswa mampu mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).
- Mahasiswa mampu menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.
- Mahasiswa mampu menganalisis dan memberikan solusi untuk kasus deadlock.
- Mahasiswa mampu berkolaborasi dalam tim untuk menyusun laporan analisis.
- Mahasiswa mampu menyajikan hasil studi kasus secara sistematis.


---

## Dasar Teori
1. Deadlock
   Deadlock adalah suatu kondisi di mana terdapat dua proses saling tunggu sehingga tidak ada proses yang bisa berjalan. Ada 4 penyebab deadlock yaitu:
   - Mutual Exclusion (Saling Pengecualian).
   - Hold and Wait (Menahan dan Menunggu).
   - No Preemption (Tanpa Preemptif).
   - Circular Wait (Menunggu Melingkar).
2. Semaphore
   Semaphore adalah variabel integer sederhana yang digunakan untuk menyelesaikan masalah sinkronisasi proses. Hanya dapat diakses melalui dua operasi standar dan tidak dapat dibagi: Wait (P) dan Signal (V).
   Tipe Semaphore :
   - Counting Semaphore (Semaphore Penghitung): Nilai semaphora dapat berkisar dari nol hingga bilangan bulat positif tak terbatas. Biasanya digunakan untuk mengontrol akses ke kumpulan sumber daya, di mana nilai awalnya adalah jumlah sumber daya yang tersedia.
   Wait (P): Mengurangi nilai semaphora. Jika nilainya menjadi negatif, proses harus menunggu.
   Signal (V): Meningkatkan nilai semaphora. Jika ada proses yang menunggu, salah satunya akan dibangunkan.
   - Binary Semaphore (Mutex): Nilainya hanya bisa 0 atau 1. Ini sangat mirip dengan mutex lock (saling pengecualian) dan biasanya digunakan untuk mengimplementasikan lock pada bagian kode kritis (critical section).
3. Monitor
   Monitor adalah konstruksi pemrograman tingkat tinggi yang menyediakan mekanisme yang lebih terstruktur dan mudah digunakan untuk sinkronisasi.
   Fitur Kunci Monitor
   - Saling Pengecualian Otomatis (Automatic Mutual Exclusion): Monitor mengelompokkan variabel data bersama, prosedur, dan kode inisialisasi. Hanya satu proses (thread) pada satu waktu yang diizinkan untuk aktif di dalam prosedur monitor mana pun.
   - Variabel Kondisi (Condition Variables): Ini adalah fitur yang disediakan di dalam monitor yang memungkinkan proses menunggu suatu kondisi tertentu terpenuhi. Operasi pada variabel kondisi adalah:
   Wait: Proses melepaskan lock pada monitor dan menangguhkan dirinya hingga proses lain memanggil signal.
   Signal: Membangunkan tepat satu proses yang menunggu pada variabel kondisi tersebut. Jika tidak ada yang menunggu, operasi tidak berpengaruh.

---

## Langkah Praktikum

1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---


## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
1. Simulasi Dining Philosophers
![Screenshot hasil](/praktikum/week7-concurrency-deadlock/screenshots/code.png)
2. Versi Fixed
![Screenshot hasil](/praktikum/week7-concurrency-deadlock/screenshots/code0.png)

---

## Analisis
1. Simulasi Dining Philosophers
![Screenshot hasil](/praktikum/week7-concurrency-deadlock/screenshots/code.png)
Deadlock terjadi ketika filsuf mencoba mengambil garpu sebelah kanan. Karena, semua filsuf sudah meng-lock garpu di sebelah kirinya masing-masing sehingga tidak ada garpu yang tersisa untuk digunakan sebagai garpu kanan.
2. Versi Fixed
![Screenshot hasil](/praktikum/week7-concurrency-deadlock/screenshots/code0.png)
Deadlock telah dihindari dengan cara hanya mengizinkan 4 filsuf yang dapat makan secara bersamaan.
Bukti:
- Hanya filsuf 0 sampai 3 yang dapat masuk ke ruangan untuk makan bersama, sedangkan filsuf 4 harus menunggu.
- Garpu F4 dalam kondisi tidak terpakai.
- Filsuf 3 dapat memulai proses (makan) karena sudah menggunakan garpu kiri (F3) dan bisa menggunakan garpu kanan (F4). 
- Filsuf 3 menyelesaikan proses, menaruh kembali ke dua garpu (F3 dan F4) lalu keluar ruangan dan Filsuf 4 bisa masuk ruangan.
- Filsuf 2 dapat memulai proses (makan) karena sudah menggunakan garpu kiri (F2) dan bisa menggunakan garpu kanan (F3).
- Filsuf 2 menyelesaikan proses dan menaruh kembali ke dua garpu (F2 dan F3).
- Filsuf 1 dapat memulai proses (makan) karena sudah menggunakan garpu kiri (F1) dan bisa menggunakan garpu kanan (F2).
- Filsuf 1 menyelesaikan proses dan menaruh kembali ke dua garpu (F1 dan F2).
- Filsuf 0 dapat memulai proses (makan) karena sudah menggunakan garpu kiri (F0) dan bisa menggunakan garpu kanan (F1).
- Filsuf 0 menyelesaikan proses dan menaruh kembali ke dua garpu (F0 dan F1).
- Filsuf 4 dapat memulai proses (makan) karena sudah menggunakan garpu kiri (F4) dan bisa menggunakan garpu kanan (F0).
- Filsuf 4 menyelesaikan proses dan menaruh kembali ke dua garpu (F4 dan F0).
- Semua filsuf sudah berhasil menyelesaikan proses (makan).
3. Analisis Deadlock
     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya bisa digunakan satu filsuf) | Tetap dipertahankan karena garpu adalah sumber daya yang tidak dapat dibagi |
     | Hold and Wait | Ya (semua filsuf saling tunggu tanpa akhir) | Pengurangan jumlah filsuf yang dapat makan bersama, sehingga hold and wait dapat berakhir dan proses dapat berjalan |
     | No Preemption | Ya (ketika garpu sedang digunakan, maka filsuf lain tidak dapat mengambilnya secara paksa) | Tetap digunakan. Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya (semua filsuf menunggu garpu kanan yang menyebabkan rantai melingkar) | Pengurangan jumlah filsuf yang dapat makan bersama, sehingga memutus rantai melingkar |
---

## Diskusi
1. Berdasarkan hasil eksperimen, Dining Philosophers mengalami Deadlock yang disebabkan:
   - Mutual Exclusion: Garpu adalah sumber daya yang tidak dapat dibagi.
   - Hold and Wait: Setiap filsuf dapat mengambil garpu kirinya dan menahan sambil menunggu garpu kanannya tersedia.
   - No Preemption: Garpu tidak dapat diambil paksa dari tangan filsuf yang memegangnya.
   - Circular Wait: Jika semua filsuf secara bersamaan mengambil garpu kirinya, mereka semua akan menunggu garpu kanan yang dipegang oleh tetangga sebelah mereka. Ini menciptakan rantai menunggu melingkar, dan tidak ada yang bisa makan.
2. Penggunaan Counting Semaphore (room dengan nilai $N-1 = 4$) berhasil mencegah terjadinya deadlock. Semaphore ini membatasi jumlah filsuf yang diizinkan untuk masuk ke critical section secara bersamaan, sehingga melanggar kondisi Circular Wait. Ini menjamin bahwa selalu ada setidaknya satu filsuf yang dapat memperoleh kedua garpu dan melanjutkan proses makan.
3. Mekanisme sinkronisasi ganda yaitu Mutex (forks) menjamin eksklusivitas akses ke satu sumber daya (garpu) dan Counting Semaphore (room) untuk mengelola sumber daya bersama secara efisien, aman, dan tanpa menghasilkan kebuntuan.
---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.  
   **Jawaban:**
   - **Mutual Exclusion (Saling Pengecualian).**
   - **Hold and Wait (Menahan dan Menunggu).**
   - **No Preemption (Tanpa Preemptif).**
   - **Circular Wait (Menunggu Melingkar).**  
2. Mengapa sinkronisasi diperlukan dalam sistem operasi? 
   **Jawaban:Sinkronisasi diperlukan dalam sistem operasi untuk mengelola akses bersama ke sumber daya atau data oleh proses atau thread yang berjalan secara bersamaan dan untuk menghindari deadlock.**  
3. Jelaskan perbedaan antara semaphore dan monitor.  
   **Jawaban:Semaphore adalah sinkronisasi tingkat rendah yang harus diimplementasikan secara eksplisit oleh programmer dengan menempatkan operasi P (wait) dan V (signal) di tempat yang tepat.** 
   **Sedangkan Monitor adalah sinkronisasi tingkat tinggi yang bisa melakukan mutual exclusion secara otomatis, sistem menjamin hanya satu proses yang dapat aktif di dalam monitor pada satu waktu.** 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
   Mengerjakan tugas secara berkelompok.
- Bagaimana cara Anda mengatasinya?  
   Bertanya ke teman.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
