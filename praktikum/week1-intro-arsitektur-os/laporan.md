
# Laporan Praktikum Minggu [1]
Topik: [Arsitektur Sistem Operasi dan Kernel]

---

## Identitas
- **Nama**  : [Safrudin]  
- **NIM**   : [250202966]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.
> Mahasiswa mampu menjelaskan fungsi sistem operasi pada arsitektur komputer.
> Mahasiswa mampu menggambar diagram arsitektur menggunakan software komputer.
> Mahasiswa dapat mengidentifikasi komponen utama operating system.
> Mahasiswa bisa membandingkan beberapa model arsitektur OS yang ada.

---

## Dasar Teori
Dasar teori yang digunakan adalah teori sistem operasi linux, arsitektur kernel, dan logging sistem. Dimana teori sistem operasi linux menjelaskan mengapa  perintah *uname* dapat menampilkan versi sistem (karena kernel memang menyimpan informasi identitas). Lalu arsitektur kernel menjelaskan mengapa perintah *lsmod* dapat menunjukkan modul yang aktif (karena Linux menggunakan arsitektur modular). Dan logging sistem jika bisa mengakses perintah *dmesg* akan bisa melihat aktivitas kernel dan hardware sejak terakhir kali sistem dinyalakan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   - membuka cloud shell pada google chrome.
   - menuliskan perintah yang diminta.
   - mendapatkan hasil dari perintah yang dilakukan. 
2. Perintah yang dijalankan.
   - uname -a
   - whoami
   - lsmod | head
   - dmesg | head
3. File dan kode yang dibuat.
     Tidak ada file dan code yang dibuat karena perintah tersebut hanya berfungsi untuk menampilkan informasi.
4. Commit message yang digunakan.
   - git add .
   - git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   - git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week1-intro-arsitektur-os/screenshots/Cuplikan%20layar%202025-10-12%20220815.png)

---

## Analisis
- Jelaskan makna hasil percobaan.
Percobaan ini adalah pemeriksaan dasar kernel linux untuk mendapatkan informasi sistem dan menguji batasan hak akses.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
   - Fungsi kernel, Output dari *uname -a* mengidentifikasi inti OS (Kernel Linux versi 6.6.105+).
   - System Call, Perintah *dmesg* mencoba menjalankan System Call sebuah permintaan dari User Mode ke Kernel Mode untuk membaca Kernel Ring Buffer.
   - Arsitektur OS, Output lsmod menampilkan daftar modul kernel yang dimuat mengkonfirmasi bahwa Kernel Linux adalah modular.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  - Perintah *uname -a*, menampilkan arsitektur kernel linux pada linux sedangkan pada windows hanya akan menampilkan versi build Windows.
  - Perintah *whoami*, hasilnya sama.
  - Perintah *lsmod*, perintah ini menunjukkan daftar modul yang dimuat secara dinamis dalam arsitektur modular Linux, sedangkan pada windows tidak memiliki perintah shell langsung untuk fungsi ini.
  - Perintah *dmesg*, perintah ini membaca Kernel Ring Buffer Linux yang bersifat sementara, dan pada windows  tidak menggunakan sistem ring buffer yang sama.

---

## Kesimpulan
1. Sistem Beroperasi pada Arsitektur Kernel Linux Modular.
2. Adanya Isolasi Keamanan Ketat antara Mode Kernel dan Mode Pengguna.

---

## Quiz
1. [Sebutkan tiga fungsi utama sistem operasi]  
   **Jawaban:**
   1. Mengatur sumber daya seperti CPU, memori, input/output (I/O), dan storage.
   2. Sebagai antarmuka pengguna (user interface/UI) yang memungkinkan pengguna berinteraksi dengan komputer.
   3. Mengatur berkas dalam bentuk file dan folder juga menyediakan layanan supaya aplikasi dapat diinstal dan digunakan**  
2. [Jelaskan perbedaan antara kernel mode dan user mode]  
   **Jawaban:**
    Kernel Mode memiliki akses penuh secara langsung ke semua hardware sedangkan User Mode tidak bisa mengakses langsung ke hardware.
3. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel]  
   **Jawaban:**
   1. contoh OS dengan arsitektur monolithic yaitu Linux, UNIX, dan MS-DOS.
   2. contoh OS dengan arsitektur microkernel yaitu MINIX, QNX, dan Mach.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  Mencoba menggunakan github dan mencoba menjalankan perintah di terminal.
- Bagaimana cara Anda mengatasinya?  
  Bertanya pada teman dan menggunakan AI.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
