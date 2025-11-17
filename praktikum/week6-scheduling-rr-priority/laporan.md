
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Safrudin 
- **NIM**   : 250202966  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini. 

- Mahasiswa mampu menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
- Mahasiswa mampu menyusun tabel hasil perhitungan dengan benar dan sistematis.
- Mahasiswa mampu membandingkan performa algoritma RR dan Priority.
- Mahasiswa mampu menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
- Mahasiswa mampu menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.
  
---

## Dasar Teori
1. Tujuan penjadwalan CPU adalah untuk memaksimalkan kinerja CPU yang didasarkan pada Waiting Time dan Turnaround Time.
2. Konsep Preemption dan Context Switching. Di mana pada Round Robin (preemptive) suatu proses dapat dihentikan dan dilanjutkan nanti sesuai time quantum yang digunakan. Proses pergantian suatu proses yang bekerja ini disebut Context Switching. Sedangkan dalam Priority Scheduling (non preemptive), proses harus diselesaikan dulu baru bisa proses selanjutnya berjalan.
3. Time Quantum dalam Round Robin adalah batas waktu dalam menjalankan suatu proses.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
   - Menyiapkan data proses, P1,P2,P3,P4.
   - Membuka Google Sheets.
   - Mencoba eksperimen sesuai instruksi.  
2. Perintah yang dijalankan. 
   - WT[i] = waktu mulai eksekusi - Arrival[i].
   - TAT[i] = WT[i] + Burst[i]. 
3. File dan kode yang dibuat. 
   Tidak ada. 
4. Commit message yang digunakan.
- git add .
- git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
- git push origin main
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week6-scheduling-rr-priority/screenshots/Cuplikan%20layar%202025-11-16%20150852.png)

   ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   15   17   20   22
   ```

![Screenshot hasil](/praktikum/week6-scheduling-rr-priority/screenshots/Cuplikan%20layar%202025-11-16%20151644.png)

   ```
     | P1 | P2 | P3 | P4 |
     0    5    8    14   22 
   ```


| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
| :--- | :--- | :--- | :--- | :--- |
| RR | 9,375 | 13,625 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
| Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

- Time Quantum dalam Round Robin adalah parameter dalam proses untuk mengatur kinerja CPU.
- Priority Scheduling berfungsi sebagai mekanisme untuk menjalankan proses sesuai urutan paling penting (priority) terlebih dahulu.

---

## Analisis
- Jelaskan makna hasil percobaan.
  Percobaan ini menunjukkan perbedaan antara Round Robin dengan Priority Scheduling. Di mana pada RR proses dilakukan secara adil sesuai Time Quantum dan waktu tunggu antar proses yang lebih cepat. Sedangkan pada PS, proses dikerjakan lebih efisien karena harus melakukan proses terpenting dulu hingga selesai.   
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
  1. Fungsi kernel adalah sebagai pengelola sumber daya CPU.
  2. System call berfungsi untuk memberhentikan proses dan memulai proses lainnya.
  3. Pada arsitektur monolitik semua sistem berada di satu alamat yang sama sehingga penjadwalan bisa berjalan cepat. Sedangkan pada arsitektur mikrokernel beberapa fungsinya berada di luar sehingga komunikasinya lebih lama. 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Pada Linux lebih sering menggunakan RR yang mengutamakan keadilan. Sedangkan pada Windows lebih sering menggunakan PS yang mengutamakan proses yang paling penting dahulu.

---

## Kesimpulan
Secara performa, PS menghasilkan waktu tunggu rata-rata dan turnaround time yang lebih rendah, menunjukkan efisiensi waktu yang unggul. Sebaliknya, RR menghasilkan waktu tunggu rata-rata dan turnaround time yang lebih tinggi, namun unggul dalam keadilan dan waktu respons yang merata. Dalam lingkungan OS yang berbeda, Linux cenderung mengimplementasikan filosofi fairness yang mirip RR tetapi lebih canggih, sementara Windows mengandalkan penjadwalan prioritas yang ketat, di mana hasil nyata akan sangat tergantung pada level prioritas yang diterapkan pada setiap proses.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
   **Jawaban:Round Robin lebih mengutamakan keadilan dan waktu tunggu yang lebih cepat sehingga semua proses akan mendapatkan giliran secara berkala dengan waktu tunggu yang lumayan singkat. Sedangkan pada Priority Scheduling penjadwalan didasarkan pada proses yang terpenting terlebih dahulu hingga selesai, baru proses selanjutnya bisa dijalankan. PS memiliki waktu tunggu yang lama.**  
2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem? 
   **Jawaban:Jika q besar maka sistem akan lebih efisien tetapi waktu tunggu akan lebih lama sedangkan, jika q kecil waktu tunggu akan lebih singkat tetapi sistem menjadi tidak efisien.**  
3. Mengapa algoritma Priority dapat menyebabkan starvation?  
   **Jawaban:Karena pada PS proses dijalankan berdasarkan prioritas. Jadi, meskipun ada proses yang datang lebih dulu dan sudah siap, hanya menunggu untuk dieksekusi tetapi ada proses yang baru datang dengan prioritas lebih tinggi. Maka proses dengan prioritas tinggi akan dieksekusi lebih dulu. Sehingga proses yang datang lebih dulu akan berada dalam kondisi starvation.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
  membuat perhitungan pada Round Robin dan Priority Scheduling. 
- Bagaimana cara Anda mengatasinya?
  menggunakan AI dan bertanya ke teman.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
