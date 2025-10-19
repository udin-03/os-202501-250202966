
# Laporan Praktikum Minggu [2]
Topik: [" Struktur System Call dan Fungsi Kernel "]

---

## Identitas
- **Nama**  : [Safrudin]  
- **NIM**   : [250202966]  
- **Kelas** : [1IKRB]

---

## Tujuan 
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.
> Mahasiswa mampu mengamati alur perpindahan dari user mode ke kernel mode.
> Mahasiswa mampu mengidentifikasi jenis-jenis system call beserta fungsinya.
> Mahasiswa mampu menggunakan perintah linux untuk menganalisis dan menampilkan system call.

---

## Dasar Teori
Dasar teori yang digunakan dalam percobaan ini adalah arsitektur sistem operasi khusunya system call. System call berfungsi sebagai antarmuka bagi program aplikasi untuk meminta layanan dari kernel. Permintaan ini memicu system call yang secara otomatis mengubah mode CPU dari user mode ke kernel mode. Lalu setelah diproses oleh kernel, kernel mode akan beralih ke user mode. Untuk memberikan hasil perintah ke program aplikasi.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   > membuka cloud shell
   > memasukan perintah sesuai contoh 
   > menganalisis hasilnya  
2. Perintah yang dijalankan.
   > strace ls
   > strace -e trace=open,read,write,close cat /etc/passwd
   > dmesg | tail -n 10
3. File dan kode yang dibuat.
   > tidak ada file dan kode yang dibuat.  
4. Commit message yang digunakan.
   > git add .
   > git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   > git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week2-syscall-structures/screenshots/Diagram%20Alur%20System%20Call.png)

---

## Analisis
- Jelaskan makna hasil percobaan.
  > Hasil dari percobaan tercebut menunjukkan bahwa program aplikasi tidak dapat langsung mengakses sumber daya sistem. Harus melalui layanan system call yang dikelola oleh kernel (kernel mode).  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
  > Fungsi kernel adalah sumber daya tunggal dengan system call sebagai mekanisme untuk menghubungkan program aplikasi(user mode) dengan kernel(kernel mode) sesuai arsitektur OS.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  > Perbedaanya adalah pada Windows fokus pada lapisan API(Application Programming Interface) dan log terstruktur untuk interaksi sistem sedangkan Linux fokus pada fungsi kernel mentah.

---

## Kesimpulan
Kesimpulan dalam praktikum ini adalah program aplikasi(user mode) tidak dapat langsung mengakses kernel(kernel mode) harus melalui system call.

---

## Quiz
1. [Apa fungsi utama system call dalam sistem operasi?]  
   **Jawaban: Fungsi system call dalam sistem operasi adalah sebagai antarmuka untuk meminta layanan dari user mode ke kernel mode.**  
2. [Sebutkan 4 kategori systen call yang umum digunakan.]  
   **Jawaban: 4 kategori system call yang umum digunakan adalah manajemen proses, manajemen perangkat, manajemen berkas, dan komunikasi antar proses (IPC).**  
3. [Mengapa system call tidak bisa dipanggil langsung oleh user program?]  
   **Jawaban: System call tidak bisa dipanggil langsung oleh user program karena alasan keamanan dan stabilitas sistem.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
> memahami alur kerja system call.  
- Bagaimana cara Anda mengatasinya? 
> mempelajari penjelasannya di internet. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
