
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine

---

## Identitas
|     Nama      |    NIM    | Kelas  |
| :-----------: | :-------: | :----: |
| Muhamad Juhan | 250202953 | 1 IKRB |
|   Safrudin    | 250202966 | 1 IKRB |

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.

- Mahasiswa mampu menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
- Mahasiswa mampu membuat dan menjalankan sistem operasi guest di dalam VM.
- Mahasiswa mampu mengatur konfigurasi resource VM (CPU, RAM, storage).
- Mahasiswa mampu menjelaskan mekanisme proteksi OS melalui virtualisasi.
- Mahasiswa mampu menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.
  
---

## Dasar Teori

1. Teknologi Virtualisasi: Sistem yang memungkinkan pembuatan mesin virtual di atas perangkat keras fisik, sehingga satu komputer dapat menjalankan beberapa sistem operasi secara terisolasi.

2. Manajemen Sumber Daya (Resource Management): Proses pengalokasian kapasitas perangkat keras, seperti memori (RAM), dari komputer host ke mesin virtual. Dalam pengujian ini, terlihat perbandingan alokasi memori antara 2048 MB dan 4096 MB untuk performa sistem.

3. Sistem Operasi Guest (Linux Ubuntu): Penggunaan distribusi Linux berbasis open-source sebagai sistem operasi yang berjalan di dalam lingkungan virtual untuk keperluan simulasi dan pengujian.

4. Antarmuka Pengguna (Graphical User Interface): Implementasi GUI pada Ubuntu yang memungkinkan interaksi pengguna melalui aplikasi visual, seperti penggunaan peramban Firefox di dalam lingkungan mesin virtual.
   
---

## Langkah Praktikum
1. Pembuatan Mesin Virtual: Membuat mesin virtual baru dengan nama Linux_Ubuntu, serta menentukan tipe sistem operasi Linux dan versi Ubuntu (64-bit).

2. Konfigurasi RAM: Mengatur alokasi Base Memory pada bagian System; terlihat dalam percobaan dilakukan pengaturan sebesar 2048 MB dan juga 4096 MB untuk memastikan performa yang optimal.

4. Pengaturan Urutan Boot: Menyesuaikan Boot Device Order pada tab Motherboard dengan urutan: Optik, Floppy, Hard Disk, dan Jaringan.

5. Aktivasi Fitur Tambahan: Memastikan fitur I/O APIC dan Hardware Clock in UTC sudah dalam posisi tercentang/aktif sesuai pengaturan standar sistem.

6. Instalasi dan Pengujian: Menjalankan VM hingga proses instalasi Ubuntu selesai, kemudian memverifikasi hasilnya dengan membuka aplikasi Firefox di dalam sistem operasi guest tersebut.

7. screenshot hasilnya dan membuat laporan praktikum lalu unggah di github.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
# Mengecek user yang sedang aktif di sistem Ubuntu
whoami

# Menampilkan informasi sistem dan arsitektur (identitas VM)
uname -a

# Mengecek penggunaan memori (RAM) untuk verifikasi perubahan 2GB ke 4GB
free -h

# Menjalankan browser Firefox melalui terminal
firefox
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week12-virtual-machine/screenshots/Cuplikan%20layar%202026-01-10%20121229.png)

![Screenshot hasil](/praktikum/week12-virtual-machine/screenshots/Cuplikan%20layar%202026-01-10%20122309.png)

![Screenshot hasil](/praktikum/week12-virtual-machine/screenshots/Cuplikan%20layar%202026-01-10%20122415.png)

![Screenshot hasil](/praktikum/week12-virtual-machine/screenshots/Cuplikan%20layar%202026-01-10%20125211.png)

---

## Analisis
Hasil percobaan menunjukkan bahwa sistem operasi Ubuntu dapat berjalan stabil di dalam mesin virtual dengan nama Linux_Ubuntu. Peningkatan RAM dari 2048 MB menjadi 4096 MB secara nyata meningkatkan responsivitas sistem saat menjalankan aplikasi berat seperti Firefox.

Perintah uname -a membuktikan peran kernel sebagai jembatan antara hardware virtual yang kita atur di VirtualBox dengan perangkat lunak.

Saat menjalankan perintah free -h atau membuka firefox, terjadi system call di mana aplikasi meminta izin kepada kernel untuk menggunakan alokasi memori RAM (2GB atau 4GB) yang telah disediakan.

Penggunaan versi Ubuntu (64-bit) pada arsitektur x86_64 memungkinkan sistem untuk mengelola memori yang lebih besar (di atas 4GB) secara lebih efisien dibandingkan arsitektur 32-bit.

Pada Linux, pengelolaan sumber daya jauh lebih transparan di mana kita bisa memantau penggunaan modul dan memori secara mendetail lewat terminal (CLI), sedangkan di Windows hal ini lebih banyak dikelola secara otomatis melalui antarmuka grafis (GUI) seperti Task Manager.

---

## Kesimpulan
1. Praktikum ini berhasil menginisialisasi dan menjalankan mesin virtual dengan nama Linux_Ubuntu menggunakan sistem operasi Ubuntu 64-bit di atas platform VirtualBox.

2. Berdasarkan perbandingan yang dilakukan, pengalokasian memori sebesar 4096 MB memberikan performa sistem yang lebih stabil dan responsif saat menjalankan aplikasi seperti Firefox dibandingkan alokasi 2048 MB.

---

## Quiz
1. Apa perbedaan antara host OS dan guest OS? 
   **Jawaban:** 
   - **Host OS adalah sistem operasi utama yang terinstal langsung pada perangkat keras fisik komputer, yang dalam praktikum ini adalah sistem Windows pada laptop.** 
   - **Guest OS adalah sistem operasi yang dijalankan di dalam lingkungan virtual di atas Host OS, yaitu mesin Linux_Ubuntu yang dibuat melalui VirtualBox.**
2. Apa peran hypervisor dalam virtualisasi?
   **Jawaban:**  
   - **Hypervisor (seperti Oracle VM VirtualBox) berfungsi sebagai perantara yang mengelola dan membagi sumber daya fisik dari Host OS ke mesin virtual.**
   - **Hypervisor mengatur alokasi kapasitas memori secara spesifik, seperti pengaturan 2048 MB atau 4096 MB untuk digunakan oleh sistem operasi tamu tanpa mengganggu stabilitas sistem utama.**
3. Mengapa virtualisasi meningkatkan keamanan sistem?
   **Jawaban:**  
   - **Isolasi Sistem: Virtualisasi mengisolasi Guest OS sehingga aktivitas di dalamnya tidak berpengaruh langsung pada Host OS.**
   - **Lingkungan Pengujian: Pengguna dapat melakukan verifikasi sistem dan menjalankan perintah terminal yang berisiko di lingkungan virtual tanpa ancaman kerusakan pada sistem operasi fisik.**

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
- menjalankan Virtual Machine.
- Bagaimana cara Anda mengatasinya?  
- bertanya ke teman dan menggunakan ai.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
