
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Safrudin 
- **NIM**   : 250202966
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

- Mahasiswa mampu menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
- Mahasiswa dapat menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
- Mahasiswa dapat membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
- Mahasiswa mampu menjelaskan kelebihan dan kekurangan masing-masing algoritma.
- Mahasiswa dapat menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.

---

## Dasar Teori
- Tujuan penjadwalan CPU adalah untuk memaksimalkan utilitas CPU dan meminimalkan waktu respons dan waktu tunggu bagi pengguna.
- Konsep Metrik Kinerja Kunci
  1. Waiting Time, waktu yang dihabiskan suatu proses dalam antrian, menunggu dieksekusi.
  2. Turnaround Time, total waktu sejak proses tiba hingga selesai.
  3. Burst Time, jumlah waktu CPU yang dibutuhkan proses untuk menyelesaikan eksekusinya.
- Algoritma FCFS adalah algoritma penjadwalan non-preemptive yang paling sederhana, beroperasi berdasarkan prinsip siapa yang tiba lebih dulu akan dieksekusi lebih dulu, tanpa memandang waktu proses yang dibutuhkan (Burst Time).
- Algoritma SJF adalah algoritma non-preemptive yang berfokus pada efisiensi. Prinsipnya adalah memilih proses dengan Burst Time terpendek dari semua proses yang sudah tiba di memori untuk dieksekusi berikutnya.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   - Menyiapkan data proses, P1,P2,P3,P4.
   - Membuka Google Sheets.
   - Mencoba eksperimen sesuai instruksi.  
2. Perintah yang dijalankan.
   - Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
   - Turnaround Time (TAT) = WT + Burst Time  
3. File dan kode yang dibuat.  
   tidak ada.
4. Commit message yang digunakan.
   - git add .
   - git commit -m "Minggu 5 CPU Scheduling FCFS & SJF"
   - git push origin main

---

## Kode / Perintah
- Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
- Turnaround Time (TAT) = WT + Burst Time
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](/praktikum/week5-scheduling-fcfs-sjf/screenshots/Cuplikan%20layar%202025-11-09%20172330.png)

| P1 | P2 | P3 | P4 |
0    6    14   21   24

![Screenshot hasil](/praktikum/week5-scheduling-fcfs-sjf/screenshots/Cuplikan%20layar%202025-11-09%20172345.png)
![Screenshot hasil](/praktikum/week5-scheduling-fcfs-sjf/screenshots/Cuplikan%20layar%202025-11-09%20172645.png)

| P1 | P4 | P3 | P2 |
0    6    9   16   24

## Perbandingan Algoritma Penjadwalan FCFS dan SJF

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
| :---: | :---: | :---: | :--- | :--- |
| **FCFS** | **8.75** | **14.75** | Sederhana, mudah diterapkan, dan menjamin **tanpa *starvation***. | Tidak efisien, rentan terhadap **Convoy Effect**, menghasilkan WT tinggi. |
| **SJF** | **6.25** | **12.25** | **Optimal** dalam meminimalkan **rata-rata Waiting Time** dan **Turnaround Time**. | Membutuhkan **estimasi Burst Time** (sulit diprediksi), dapat menyebabkan **Starvation**. |

Analisis Hasil
Perbandingan Rata-rata WT & TAT:

FCFS: Avg WT = 8.75; Avg TAT = 14.75

SJF: Avg WT = 6.25; Avg TAT = 12.25

Kesimpulan: SJF menghasilkan Avg Waiting Time dan Avg Turnaround Time yang lebih rendah (lebih baik) dibandingkan FCFS.

Kondisi Unggul:

SJF lebih unggul dari FCFS ketika ada variasi besar pada Burst Time (seperti pada data ini, dari 3 hingga 8). SJF dapat mengeksekusi proses pendek (P4) terlebih dahulu, sehingga proses tersebut selesai cepat dan mengurangi akumulasi waktu tunggu untuk keseluruhan sistem.

FCFS unggul dari SJF dalam hal kesederhanaan dan keadilan (fairness). FCFS menjamin tidak ada proses yang mengalami starvation. FCFS juga akan memiliki performa yang hampir sama dengan SJF jika semua proses memiliki Burst Time yang serupa atau jika semua proses tiba pada waktu yang hampir bersamaan (AT = 0).

Kesimpulan Singkat

Penjadwalan SJF terbukti lebih efisien daripada FCFS dalam meminimalkan waktu tunggu dan waktu penyelesaian rata-rata (TAT) untuk set data ini. Namun, FCFS menawarkan solusi yang lebih sederhana dan adil, menjamin setiap proses akan dieksekusi tanpa risiko starvation.

---

## Analisis
- Jelaskan makna hasil percobaan.  
  Makna utama dari perbandingan kedua algoritma penjadwalan ini adalah bahwa SJF terbukti lebih efisien dan optimal dibandingkan FCFS dalam meminimalkan waktu tunggu dan waktu penyelesaian tugas. Hasil eksperimen menunjukkan bahwa Avg Waiting Time dan Avg Turnaround Time SJF (6.25 dan 12.25) jauh lebih rendah daripada FCFS (8.75 dan 14.75).

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
  Makna dari perbandingan FCFS dan SJF menunjukkan bahwa efisiensi kernel OS sangat bergantung pada kebijakan penjadwalan yang dipilih. Hasil percobaan membuktikan bahwa SJF lebih optimal karena menghasilkan rata-rata Waiting Time (WT) dan Turnaround Time (TAT) yang jauh lebih rendah (misalnya, WT 6.25 vs. 8.75 pada FCFS). Keunggulan SJF berasal dari keputusan Kernel untuk memprioritaskan proses dengan Burst Time terpendek, suatu fungsi yang berada dalam Kernel Space dan dipicu oleh System Call atau interupsi. Sebaliknya, FCFS, meskipun sederhana dan adil, menyebabkan Convoy Effect yang tidak efisien, menaikkan WT secara keseluruhan.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Perbedaan hasil simulasi penjadwalan (FCFS vs SJF) di lingkungan OS yang berbeda, seperti Linux vs Windows, terletak pada implementasi kernel masing-masing. Hasil simulasi FCFS/SJF di atas kertas tidak berubah, tetapi jika program nyata dijalankan, waktu Waiting dan Turnaround aktual akan berbeda karena kedua OS menggunakan algoritma penjadwalan preemptive yang jauh lebih canggih, bukan FCFS atau SJF murni.

---

## Kesimpulan
Praktikum ini menyimpulkan bahwa Algoritma SJF lebih optimal untuk mencapai efisiensi waktu, menghasilkan rata-rata Waiting Time (WT) dan Turnaround Time (TAT) terendah (WT 6.25, TAT 12.25). Keunggulan ini terjadi karena SJF meminimalkan total waktu tunggu komulatif dengan memprioritaskan proses pendek. Sebaliknya, FCFS terbukti tidak efisien (WT 8.75, TAT 14.75) karena kebijakan kedatangan murni menyebabkan Convoy Effect, memaksa proses cepat menunggu di belakang proses lambat.

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
   **Jawaban:FCFS bekerja berdasarkan siapa yang datang lebih dulu. Sedangkan, SJF bekerja berdasarkan waktu siapa yang dihabiskan paling singkat.**  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
   **Jawaban:Katena SJF menggunakan algoritma untuk mengerjakan tugas-tugas dengan waktu terpendek dahulu dan menunda proses yang paling lama menyumbang waktu tunggu hingga akhir.**  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
   **Jawaban:Kelemahan utama algoritma SJF jika diterapkan pada sistem interaktif adalah ketidakmampuannya untuk menjamin respons yang cepat dan konsisten, terutama pada sistem yang memiliki variasi beban kerja tinggi.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
Membuat percobaan pada google sheets. 
- Bagaimana cara Anda mengatasinya?  
Mengatasinya menggunakan AI.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
