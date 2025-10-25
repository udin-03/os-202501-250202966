
# Laporan Praktikum Minggu 3
Topik: Linux File System & Permission

---

## Identitas
- **Nama**  : Safrudin 
- **NIM**   : 250202966 
- **Kelas** : 1IKRB

---

## Tujuan 
- Mahasiswa mampu menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
- Mahasiswa mampu menggunakan chmod dan chown untuk manajemen hak akses file.
- Mahasiswa mampu menjelaskan hasil output dari perintah Linux dasar.

---

## Dasar Teori

Eksperimen ini didasarkan pada tiga konsep inti sistem operasi mirip Unix: Manajemen Sistem File, Struktur Akun Pengguna, dan Pengendalian Akses. Manajemen Sistem File berfokus pada hierarki direktori tunggal yang berakar di /, di mana setiap sesi terminal beroperasi dalam Direktori Aktif (pwd, cd). Perintah ls -l mengekspos metadata file, termasuk hak akses. Teori Struktur Akun Pengguna diwakili oleh file /etc/passwd, yang berfungsi sebagai database akun dan mengidentifikasi setiap entitas dengan UID (User ID) dan GID (Group ID) numerik; akun sistem penting ditandai dengan shell non-login (/sbin/nologin) untuk alasan keamanan. Terakhir, Pengendalian Akses adalah fondasi manipulasi file, membagi hak akses (Baca, Tulis, Eksekusi) ke dalam tiga kategori: Pemilik (User), Group, dan Lainnya (Others). Perintah chmod (Change Mode) menerapkan batasan ini, misalnya 600 secara drastis membatasi akses hanya untuk Pemilik, sementara chown (Change Ownership) mengubah identitas pemilik file, mentransfer hak istimewa penuh ke akun baru, seperti root.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   - membuka cloud shell,
   - memasukan perintah sesuai contoh,
   - menganalisis hasilnya

2. Perintah yang dijalankan.
     pwd
- ls -l
- cd /tmp
- ls -a
- cat /etc/passwd | head -n 5
- echo "Hello <NAME><NIM>" > percobaan.txt
- ls -l percobaan.txt
- chmod 600 percobaan.txt
- ls -l percobaan.txt
- sudo chown root percobaan.txt
- ls -l percobaan.txt

3. File dan kode yang dibuat.
- percobaan.txt, file ini dibuat dengan perintah echo "Hello <NAME><NIM>" > percobaan.txt.

4. Commit message yang digunakan.
- git add .
- git commit -m "Minggu 3 - Linux  File System & Permission"
- git push origin main
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
cat /etc/passwd | head -n 5
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week3-linux-fs-permission/screenshots/Cuplikan%20layar%202025-10-24%20222603.png)
![Screenshot hasil](/praktikum/week3-linux-fs-permission/screenshots/Cuplikan%20layar%202025-10-24%20222640.png)
---

### **1. Tabel Observasi Perintah**

| No. | Perintah (Command) | Direktori Awal | Direktori Aktif Akhir | Hasil Observasi | Fungsi Utama |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `pwd` | `/home/user` | `/home/user` | Menampilkan jalur direktori aktif saat ini. | Mengetahui lokasi di sistem file. |
| **2** | `ls -l` | `/home/user` | `/home/user` | Daftar file/folder dengan detail atribut (izin, ukuran, pemilik). | Melihat isi folder secara terperinci. |
| **3** | `cd /tmp` | `/home/user` | `/tmp` | Perubahan direktori ke `/tmp`. (Tidak ada output visual saat sukses) | Pindah ke direktori file sementara. |
| **4** | `ls -a` | `/tmp` | `/tmp` | Daftar **SEMUA** file/folder, termasuk yang tersembunyi (`.` dan `..`). | Melihat semua isi folder, termasuk file konfigurasi tersembunyi. |

---

### **2. Detail File Tersembunyi (Output dari `ls -a` di `/tmp`)**

Perintah `ls -a` akan selalu menampilkan setidaknya dua entri tersembunyi:

| Entri | Status | Deskripsi |
| :--- | :--- | :--- |
| **`.`** | Tersembunyi | Merepresentasikan **direktori saat ini** (`/tmp`). |
| **`..`** | Tersembunyi | Merepresentasikan **direktori induk** (`/`). |
| **`.hidden_file_contoh`** | Tersembunyi (Contoh) | File atau folder lain yang diawali titik, dibuat oleh sistem atau aplikasi. |

---

### **3. Struktur Kolom**

Setiap baris dipisahkan oleh tanda titik dua (`:`) dan mengikuti urutan ini:

$$\text{Nama}:\text{Kata Sandi}:\text{UID}:\text{GID}:\text{Info Pengguna}:\text{Direktori Home}:\text{Shell}$$

---

### **4. Tabel Observasi (Output dari `cat /etc/passwd | head -n 5`)**

| Baris | User | UID | GID | Direktori Home | Shell (Login Program) | Keterangan |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | `root` | **0** | **0** | `/root` | `/bin/bash` | **Administrator Sistem**. Hak akses tertinggi. |
| **2** | `daemon` | 1 | 1 | `/usr/sbin` | `/usr/sbin/nologin` | Akun layanan sistem (daemon). **Dilarang login interaktif**. |
| **3** | `bin` | 2 | 2 | `/bin` | `/usr/sbin/nologin` | Akun sistem untuk utilitas biner. **Dilarang login interaktif**. |
| **4** | `sys` | 3 | 3 | `/dev` | `/usr/sbin/nologin` | Akun sistem untuk manajemen *device*. |
| **5** | `sync` | 4 | 65534 | `/bin` | `/bin/sync` | Akun sistem untuk sinkronisasi data disk. |


---

### **5. Observasi Navigasi & Listing File**

| No. | Perintah (Command) | Direktori Aktif Awal | Direktori Aktif Akhir | Izin/Listing Awal (Contoh) | Keterangan Fungsi |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `pwd` | `/home/user` | `/home/user` | `/home/user` | Menampilkan **jalur direktori kerja**. |
| **2** | `ls -l` | `/home/user` | `/home/user` | `-rw-rw-r--` (Izin default) | Melihat **isi folder** dengan detail atribut. |
| **3** | `cd /tmp` | `/home/user` | `/tmp` | N/A | Mengubah direktori kerja ke `/tmp`. |
| **4** | `ls -a` | `/tmp` | `/tmp` | `.` , `..` , `.hidden_file` | Melihat **semua isi folder**, termasuk file tersembunyi (diawali titik). |

---

### **6. Observasi Analisis File `/etc/passwd`**

Output dari `cat /etc/passwd | head -n 5`

| Baris | User | UID | GID | Direktori Home | Shell (Login Program) | Keterangan |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | `root` | **0** | **0** | `/root` | `/bin/bash` | **Administrator Sistem** (Hak Penuh). |
| **2** | `daemon` | 1 | 1 | `/usr/sbin` | `/usr/sbin/nologin` | **Akun Layanan Sistem**. Dilarang login interaktif. |
| **3** | `bin` | 2 | 2 | `/bin` | `/usr/sbin/nologin` | **Akun Layanan Sistem**. Dilarang login interaktif. |

* **Catatan:** Karakter `x` pada kolom kata sandi menunjukkan bahwa kata sandi asli disimpan di file **`/etc/shadow`**.

---

### **7. Observasi Manipulasi Izin & Kepemilikan File**

File yang diuji: `percobaan.txt`

| No. | Perintah (Command) | Izin (Awal) | Izin (Akhir) | Pemilik (Akhir) | Analisis Perubahan |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **5** | `echo "..." > percobaan.txt` | `-rw-rw-r--` | N/A | `user group` | File dibuat dengan izin standar (R/W untuk Pemilik & Grup). |
| **6** | `chmod 600 percobaan.txt` | `-rw-rw-r--` | **`-rw-------`** | `user group` | **Pembatasan Keamanan:** Hanya **Pemilik** yang memiliki izin Baca/Tulis (`600`). Izin Grup dan Lainnya dicabut. |
| **7** | `sudo chown root percobaan.txt` | `-rw-------` | Tetap (`600`) | **`root group`** | **Perubahan Identitas:** Kepemilikan file dialihkan dari `user` ke **`root`**. Hanya `root` yang kini dapat memanipulasi file ini. |

---


## Analisis
- Jelaskan makna hasil percobaan.
>   Hasil percobaan menunjukkan  bagaimana sistem Linux mengelola keamanan dan struktur internalnya. Perintah tersebut menunjukkan pentingnya hierarki sistem file dan bagaimana setiap file dilengkapi dengan metadata izin dan kepemilikan.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
> Setiap perintah yang dieksekusi adalah cerminan dari interaksi antara Shell dan Kernel melalui System Call. Ketika perintah seperti chmod 600 dimasukkan, Shell menerjemahkannya menjadi permintaan yang kemudian disampaikan kepada Kernel melalui system call yang sesuai (misalnya, chmod).
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
> Perbedaan utama terletak pada model keamanan dan struktur sistem file. Linux menggunakan model DAC berbasis tiga kategori pengguna (Owner, Group, Others) yang izinnya mudah diubah menggunakan nilai oktal (600). Sebaliknya, Windows menggunakan Access Control List (ACL) yang jauh lebih granular dan kompleks, di mana izin diwariskan dan diatur per objek keamanan spesifik, bukan per kategori pengguna.

---

## Kesimpulan
Kesimpulan dari serangkaian percobaan kode tersebut adalah bahwa sistem operasi Linux (berbasis Unix) beroperasi berdasarkan tiga prinsip mendasar: hierarki terstruktur, identitas berbasis numerik, dan pengendalian akses ketat.

---

## Quiz
1. Apa fungsi dari perintah chmod?  
   **Jawaban: Fungsi dari perintah chmod adalah untuk mengubah hak akses pada sebuah file atau direktori.**  
2. Apa arti dari kode permission rwxr-xr--?  
   **Jawaban:**
   - **rwx, memiliki izin baca, tulis, dan eksekusi.**
   - **r-x, hanya memiliki izin baca dan eksekusi, tetapi tidak memiliki izin tulis.**
   - **r--, hanya memiliki izin baca, tidak memiliki izin tulis dan eksekusi.**
3. Jelaskan perbedaan antara chown dan chmod.  
   **Jawaban: Chmod berfungsi untuk mengubah hak akses pada file atau direktori, sedangkan chown berfungsi untuk mengubah kepemilikan dari sebuah file atau direktori.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 

   Membuat tabel pada vscode 
- Bagaimana cara Anda mengatasinya?  
Mempelajari caranya dengan ai.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
