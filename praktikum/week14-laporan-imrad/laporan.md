
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD


---

## Identitas
- **Nama**  : Safrudin  
- **NIM**   : 250202966   
- **Kelas** : 1IKRB

---

## Judul
**Simulasi Penjadwalan CPU Menggunakan Algoritma FCFS (First Come First Served) dan SJF (Shortest Job First)**

## A. Pendahuluan (Introduction)
### 1. Latar Belakang

Dalam arsitektur sistem komputer modern yang menerapkan multiprogramming, manajemen CPU menjadi sangat krusial karena efisiensi penjadwalan berdampak langsung pada responsivitas dan utilisasi sumber daya secara keseluruhan. Salah satu metode dasar adalah algoritma First Come First Served (FCFS) yang melayani proses berdasarkan urutan kedatangan, namun pendekatan ini sering kali terhambat oleh fenomena Convoy Effect. Masalah ini muncul ketika satu proses dengan durasi eksekusi (burst time) yang sangat besar menahan proses-proses kecil di belakangnya, sehingga menyebabkan penumpukan antrean dan meningkatkan rata-rata waktu tunggu secara signifikan bagi proses-proses yang lebih pendek.

Sebagai solusi untuk mengoptimalkan kinerja sistem, algoritma Shortest Job First (SJF) diperkenalkan dengan prinsip memprioritaskan proses yang memiliki durasi eksekusi terkecil untuk meminimalkan rata-rata waktu tunggu (Average Waiting Time). Meskipun secara teoretis SJF dianggap sebagai algoritma paling optimal untuk efisiensi waktu, implementasinya di dunia nyata memiliki tantangan besar dalam memprediksi durasi proses secara akurat sebelum eksekusi dilakukan. Praktikum ini bertujuan untuk melakukan analisis komparatif antara FCFS dan SJF guna memvalidasi pengaruh perbedaan urutan eksekusi terhadap metrik performa seperti Waiting Time dan Turnaround Time, sekaligus membuktikan secara empiris keunggulan efisiensi SJF dalam skenario beban kerja tertentu.

### 2. Rumusan Masalah

   1. Bagaimana mekanisme perbandingan urutan eksekusi antara algoritma FCFS dan SJF pada sekumpulan proses dengan burst time yang bervariasi?

   2. Seberapa besar pengaruh fenomena Convoy Effect pada algoritma FCFS terhadap peningkatan rata-rata Waiting Time dibandingkan dengan algoritma SJF?

   3. Apakah algoritma SJF secara konsisten memberikan nilai rata-rata Turnaround Time yang lebih rendah dibandingkan FCFS dalam simulasi ini?

### 3. Tujuan Eksperimen

   1. Menganalisis karakteristik dan prinsip kerja algoritma penjadwalan Non-Preemptive FCFS dan SJF melalui implementasi kode program.

   2. Mengukur dan membandingkan metrik performa berupa Waiting Time (WT) dan Turnaround Time (TAT) dari kedua algoritma tersebut.

   3. Membuktikan secara empiris melalui data numerik bahwa algoritma SJF mampu memberikan efisiensi waktu tunggu rata-rata yang lebih baik daripada FCFS.
   
---

## B. Metode (Methods)
### 1. Lingkungan Uji (Hardware)
#### 1.1 Perangkat Keras Yang Yigunakan:
  - Perangkat: Laptop Acer Aspire 5
  - Sistem Operasi: Windows 11 Home
  - Prosesor: Intel® Core™ i3-1115G4 
  - Memori (RAM): 20 GB
  
#### 1.2 Perangkat Lunak Yang Digunakan:
  - Editor Kode: Visual Studio Code.
  - Bahasa Pemrograman: Python versi 3.12.
  
### 2. Langkah Eksperimen
  - Identifikasi Data: Menyiapkan dataset yang berisi daftar proses (P1, P2, P3, P4, P5) beserta durasi burst time masing-masing.
  - Implementasi Kode: Menulis skrip Python untuk mensimulasikan logika FCFS (antrean berdasarkan urutan masuk) dan SJF Non-Preemptive (pengurutan berdasarkan burst time terkecil).
  - Eksekusi Simulasi: Menjalankan kedua algoritma menggunakan dataset yang sama.
  - Pengumpulan Data: Mencatat waktu selesai (finish time), waktu putar balik (turnaround time), dan waktu tunggu (waiting time) untuk setiap proses.
  - Kalkulasi Metrik: Menghitung rata-rata waktu tunggu (WT) dan rata-rata waktu putar balik (TAT) untuk dibandingkan.

### 3. Dataset / Parameter Uji
 | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 7 |
   | P2 | 1 | 9 |
   | P3 | 2 | 4 |
   | P4 | 3 | 3 |
   | P5 | 4 | 5 |
   
### 4. Cara Pengukuran
  - Turnaround Time (TAT): Diukur untuk mengetahui total waktu yang dihabiskan proses di dalam sistem sejak datang hingga selesai.
    - Rumus: TAT = FT - AT (Waktu Selesai dikurangi Waktu Datang).
  - Waiting Time (WT): Diukur untuk mengetahui berapa lama proses menunggu di antrean ready sebelum dilayani CPU.
    - Rumus: WT = TAT - BT (Turnaround Time dikurangi durasi eksekusi).
  - Rata-rata (WT & TAT): Untuk mendapatkan performa sistem secara keseluruhan, dilakukan akumulasi total dari wt dan tat yang kemudian dibagi dengan jumlah proses.
     - Rumus: rata-rata (WT/TAT) = total (WT/TAT) / jumlah proses.
  
  ---

## C. Hasil (Results)
### 1. Tabel Hasil Uji
1. FCFS (First Come First Served)
![Screenshot hasil](/praktikum/week14-laporan-imrad/screenshots/FCFS.png)
| Proses | AT | BT | FT | TAT | WT |
   |:--:|:--:|:--:|:--:|:--:|:--:|
   | P1 | 0 | 7 | 7 | 7 | 0 |
   | P2 | 1 | 9 | 16 | 15 | 6 |
   | P3 | 2 | 4 | 20 | 18 | 14 |
   | P4 | 3 | 3 | 23 | 20 | 17 |
   | P5 | 4 | 5 | 28 | 24 | 19 |

- Rata-rata Turnaround Time (TAT): 16.80
- Rata-rata Waiting Time (WT)   : 11.20

2. SJF (Shortest Job First)
![Screenshot hasil](/praktikum/week14-laporan-imrad/screenshots/SJF.png) 
| Proses | AT | BT | FT | TAT | WT |
   |:--:|:--:|:--:|:--:|:--:|:--:|
   | P1 | 0 | 7 | 7 | 7 | 0 |
   | P2 | 1 | 9 | 28 | 27 | 18 |
   | P3 | 2 | 4 | 14 | 12 | 8 |
   | P4 | 3 | 3 | 10 | 7 | 4 |
   | P5 | 4 | 5 | 19 | 15 | 10 |

- Rata-rata Turnaround Time (TAT): 13.60
- Rata-rata Waiting Time (WT)   : 8.00

### 2. Ringkasan Temuan
- Reduksi Waktu Tunggu: Penggunaan algoritma SJF berhasil memangkas rata-rata waktu tunggu sebesar 28.5% dibandingkan dengan FCFS. Hal ini membuktikan bahwa mendahulukan proses dengan burst time pendek sangat efektif mengurangi antrean.
- Urutan Eksekusi: Pada FCFS, proses dijalankan sesuai kedatangan (P1, P2, P3, P4, P5). Namun pada SJF, setelah P1 selesai pada detik ke-7, sistem memilih proses dengan beban terkecil dari antrean yang tersedia, sehingga urutannya berubah menjadi (P1, P4, P3, P5, P2).
- Dampak Proses Panjang: Pada FCFS, P2 dengan burst time besar (9) yang datang di awal menyebabkan proses-proses kecil di belakangnya (P3, P4) mengalami lonjakan waktu tunggu (WT mencapai 14-17). Di SJF, proses P2 digeser ke akhir, sehingga tidak menghambat proses lainnya.
- Optimasi Turnaround Time: Penurunan pada nilai TAT menunjukkan bahwa secara keseluruhan, proses-proses tersebut keluar dari sistem lebih cepat pada algoritma SJF dibandingkan FCFS.
    

---

## D. Pembahasan (Discussion)
### 1. Interpretasi Hasil
Berdasarkan hasil eksekusi, perbedaan yang signifikan terlihat pada nilai rata-rata Waiting Time (WT). Pada algoritma FCFS, nilai WT mencapai 11.20, sedangkan pada SJF turun menjadi 8.00. Interpretasi dari angka ini menunjukkan bahwa strategi SJF dalam mendahulukan proses dengan burst time pendek (P4 dan P3) berhasil meminimalkan akumulasi waktu tunggu.

Pada FCFS, proses P2 dengan burst time terbesar (9) dijalankan di awal karena faktor kedatangan. Hal ini menyebabkan proses-proses kecil di belakangnya harus menunggu P2 selesai, yang secara langsung meningkatkan nilai WT setiap proses berikutnya secara drastis. Sebaliknya, pada SJF, P2 ditunda eksekusinya hingga akhir (setelah P1, P4, P3, dan P5), sehingga durasi eksekusinya yang lama tidak membebani rata-rata waktu tunggu proses lainnya.

### 2. Keterbatasan Eksperimen
1. Prediksi Burst Time: Dalam skenario nyata, sistem operasi tidak mengetahui durasi burst time suatu proses secara pasti sebelum eksekusi. Simulasi ini menggunakan angka yang sudah ditentukan, sedangkan di dunia nyata harus menggunakan estimasi atau algoritma prediksi.
2. Potensi Starvation: Walaupun tidak terjadi dalam dataset ini, teori menyatakan bahwa pada SJF, proses dengan burst time besar (seperti P2) berisiko mengalami starvation (tidak pernah dieksekusi) jika proses-proses kecil terus-menerus masuk ke dalam sistem.
3. Arrival Time yang Berdekatan: Karena semua proses datang dalam waktu yang berdekatan (0-4), SJF memiliki keleluasaan besar untuk mengatur urutan. Jika rentang waktu kedatangan sangat berjauhan, perbedaan efisiensi antara FCFS dan SJF mungkin tidak akan sesignifikan hasil uji ini.

### 3. Perbandingan Teori dan Ekspektasi
| Algoritma | rata-rata Waiting Time | rata-rata Turnaround Time | Kelebihan | Kekurangan |
| :---: | :---: | :---: | :--- | :--- |
| **FCFS** | **11.20** | **16.80** | Sederhana, mudah diterapkan, dan menjamin **tanpa *starvation***. | Tidak efisien, rentan terhadap **Convoy Effect**, menghasilkan WT tinggi. |
| **SJF** | **8.00** | **13.60** | **Optimal** dalam meminimalkan **rata-rata Waiting Time** dan **Turnaround Time**. | Membutuhkan **estimasi Burst Time** (sulit diprediksi), dapat menyebabkan **Starvation**. |

Hasil eksperimen ini sepenuhnya sejalan dengan teori yang menyatakan bahwa SJF adalah algoritma optimal untuk meminimalkan rata-rata waktu tunggu. Ekspektasi awal bahwa SJF akan memberikan nilai rata-rata TAT dan rata-rata WT yang lebih rendah dibandingkan FCFS terbukti secara numerik melalui simulasi ini.

Fenomena Convoy Effect yang menjadi kelemahan utama FCFS terlihat jelas pada data hasil uji FCFS, di mana penempatan proses besar di awal antrean mengakibatkan efisiensi waktu sistem menurun secara kolektif. SJF secara efektif "memecah" konvoi tersebut dengan mengurutkan prioritas berdasarkan durasi kerja.

---

## E. Kesimpulan
1. Efisiensi Algoritma: Algoritma Shortest Job First (SJF) terbukti lebih efisien dibandingkan First Come First Served (FCFS) dengan keberhasilan menurunkan rata-rata waktu tunggu (Average Waiting Time) dari 11.20 menjadi 8.00.
2. Dampak Urutan Eksekusi: Pengurutan proses berdasarkan durasi terkecil pada SJF secara efektif mengeliminasi fenomena Convoy Effect yang terjadi pada FCFS, di mana proses panjang (P2) tidak lagi menghambat proses-proses pendek lainnya.
3. Optimalitas Metrik: Implementasi SJF memberikan nilai rata-rata Turnaround Time yang lebih rendah (13.60) dibandingkan FCFS (16.80), yang menunjukkan bahwa secara kolektif proses selesai lebih cepat di dalam sistem.
4. Kesesuaian Teori: Hasil eksperimen memvalidasi teori penjadwalan CPU bahwa untuk dataset dengan beban kerja tetap, SJF merupakan algoritma yang lebih optimal dalam meminimalkan waktu tunggu rata-rata.

---

## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts. 10th Edition. Wiley.

2. Tanenbaum, A. S., & Bos, H. (2014). Modern Operating Systems. 4th Edition. Pearson.

---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi? 
   **Jawaban:Format IMRAD membuat laporan lebih ilmiah dan mudah dievaluasi karena menyediakan struktur logis yang mencerminkan alur berpikir saintifik, mulai dari latar belakang masalah hingga penarikan kesimpulan. Dengan memisahkan antara fakta objektif pada bagian Results dan interpretasi subjektif pada bagian Discussion, laporan ini menjamin transparansi data tanpa tercampur aduk dengan asumsi pribadi penulis. Selain itu, bagian Methods yang mendetail memberikan standar bagi penguji untuk menilai validitas eksperimen serta memungkinkan orang lain untuk mereplikasi atau mengulang pengujian tersebut guna memverifikasi hasilnya. Standarisasi ini mempermudah evaluator menemukan informasi kunci secara cepat dan memastikan bahwa setiap klaim didukung oleh data empiris yang dibandingkan langsung dengan teori yang ada.**  
2. Apa perbedaan antara bagian Hasil dan Pembahasan?
   **Jawaban:**
   - **Hasil (Results): Fokus pada "Apa yang terjadi?" berisi penyajian data mentah, tabel, dan grafik secara objektif tanpa opini. Contohnya: "Nilai rata-rata WT pada SJF adalah 8.00."** 
   - **Pembahasan (Discussion): Fokus pada "Mengapa itu terjadi?" berisi interpretasi data, kaitan dengan teori, dan penjelasan penyebab perbedaan angka tersebut. Contohnya: "SJF lebih cepat karena mendahulukan proses pendek, sehingga menghilangkan Convoy Effect pada FCFS."** 
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
   **Jawaban:Sitasi dan daftar pustaka sangat penting dalam laporan praktikum karena berfungsi sebagai bentuk integritas akademik untuk menghindari plagiarisme dengan memberikan kredit kepada pemilik ide atau teori asli. Penggunaan referensi yang kredibel memberikan fondasi yang kuat bagi argumen yang dibuat, sehingga hasil analisis pada bagian Pembahasan tidak dianggap sebagai opini pribadi semata, melainkan didukung oleh literatur ilmiah yang valid. Selain itu, daftar pustaka mempermudah pembaca atau evaluator untuk melakukan penelusuran lebih lanjut guna memverifikasi rumus atau konsep yang digunakan. Dengan mencantumkan referensi, laporan praktikum akan memenuhi standar penulisan ilmiah profesional yang menuntut transparansi dan akuntabilitas dalam setiap klaim yang disampaikan.**  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
