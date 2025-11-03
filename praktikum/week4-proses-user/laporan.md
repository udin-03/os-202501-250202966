
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Safrudin  
- **NIM**   : 250202966
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- Mahasiwa mampu menjelaskan konsep proses dan user dalam sistem operasi Linux.
- Mahasiswa mampu menggunakan perintah untuk membuat dan mengelola user.
- Mahasiwa mampu menjelaskan kaitan antara manajemen user dan keamanan sistem.
- Mahasiwa mampu menghentikan atau mengontrol proses tertentu menggunakan PID.

---

## Dasar Teori
Semua perintah (seperti ps aux, pstree, dan kill) didasarkan pada konsep manajemen proses, di mana setiap program yang dieksekusi disebut proses dan diberi Process ID (PID) unik oleh kernel (contohnya PID 3309 untuk sleep 1000). Proses-proses ini diatur dalam hierarki induk-anak (terlihat pada output pstree), yang memastikan bahwa semua program, seperti dockerd atau python, berasal dari satu proses induk utama, yaitu bash(1) di lingkungan Cloud Shell Anda. Kernel bertanggung jawab penuh atas penjadwalan proses, mengukur beban kerja (Load Average), dan mengelola statusnya (seperti Sleeping atau Running). Kedua, percobaan whoami, id, dan groups didasarkan pada Manajemen Pengguna dan Izin Akses, yang menetapkan bahwa setiap proses berjalan di bawah identitas pemiliknya (safrudindidin03). Prinsip ini menentukan siapa yang berhak mengontrol (misalnya, mengakhiri dengan kill) dan mengakses sumber daya sistem.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   - membuka cloud shell,
   - memasukan perintah sesuai contoh,
   - menganalisis hasilnya
2. Perintah yang dijalankan. 
   - whoami
   - id
   - groups
   - ps aux | head -10
   - top -n 1
   - sleep 1000 &
   - ps aux | grep sleep
   - kill <PID>
   - pstree -p | head -20
3. File dan kode yang dibuat. 
   
| Pilar Teori | Konsep Kunci | Percobaan yang Relevan |
| :--- | :--- | :--- |
| **Manajemen Proses** | **PID & Hierarki** | Perintah `pstree -p` (menunjukkan struktur induk-anak) dan `ps aux`. |
| | **Siklus Hidup Proses** | Perintah `kill` (mengubah status menjadi 'Terminated') dan status `S` (Sleeping) di `ps aux`. |
| | **Penjadwalan & Beban** | Analisis metrik `%CPU`, `%MEM`, dan `Load Average`. |
| **Manajemen Pengguna** | **Identitas & Izin** | Perintah `whoami`, `id`, dan `groups` (menentukan UID, GID, dan hak `sudo`). |
| | **Hak Kontrol** | Kemampuan pengguna (`safrudindidin03`) untuk menghentikan proses yang dimilikinya (`kill 3309`). |
4. Commit message yang digunakan.
   - git add .
   - git commit -m "Minggu 4 - Manajemen Proses & User"
   - git push origin main
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week4-proses-user/screenshots/Cuplikan%20layar%202025-10-26%20033849.png)
| Perintah | Output | Deskripsi Singkat |
| :--- | :--- | :--- |
| **`whoami`** | `safrudindidin03` | Menampilkan nama pengguna (username) yang sedang login. |
| **`id`** | `uid=1000(safrudindidin03) gid=1000(safrudindidin03) groups=1000(safrudindidin03),4(adm),27(sudo),996(docker)` | Menampilkan User ID (UID), Group ID (GID) utama, dan semua grup keanggotaan pengguna. |
| **`groups`** | `safrudindidin03 adm sudo docker` | Menampilkan daftar nama grup tempat pengguna menjadi anggota. |
| **Hak Akses Tambahan** | `adm`, `sudo`, `docker` | Hak administratif (sudo) dan izin untuk mengelola kontainer Docker. |

![Screenshot hasil](/praktikum/week4-proses-user/screenshots/top.png)

| Kolom | Deskripsi | Fungsi Kunci | Status di Contoh Output |
| :--- | :--- | :--- | :--- |
| **PID** | Process ID (ID Proses) | Nomor identifikasi unik yang diberikan oleh kernel Linux ke setiap proses. | Angka unik untuk setiap proses. |
| **USER** | User (Pengguna) | Nama pengguna yang memiliki atau menjalankan proses tersebut. | root, syslog, safrudi+ (safrudindidin03). |
| **%CPU** | CPU Usage (Penggunaan CPU) | Persentase waktu CPU yang digunakan oleh proses sejak pembaruan terakhir. | 0.0 (Menunjukkan sistem ringan). |
| **%MEM** | Memory Usage (Penggunaan Memori) | Persentase memori fisik (RAM) yang digunakan oleh proses. | Tertinggi 7.3% (Digunakan oleh proses node). |
| **COMMAND** | Command (Perintah) | Nama program atau perintah yang memulai proses tersebut. | bash, node, dockerd, adduser. |

![Screenshot hasil](/praktikum/week4-proses-user/screenshots/Cuplikan%20layar%202025-10-26%20034529.png)

| Proses | PID (Process ID) | Pemilik Proses | Catatan |
| :--- | :--- | :--- | :--- |
| **sleep 1000** | **3309** | safrudi+ | Proses ini sedang dalam status tidur (S) selama 1000 detik. |
| Proses `grep` | 3313 | safrudi+ | Proses sementara yang digunakan untuk mencari (grep) proses 'sleep'. |

![Screenshot hasil](/praktikum/week4-proses-user/screenshots/Cuplikan%20layar%202025-10-26%20034834.png)

* **bash(1)** * --**dockerd(207)**
        * --**containerd(234)**
            * --{containerd}(252)
            * --{containerd}(253)
            * --{containerd}(254)
            * --{containerd}(256)
            * --{containerd}(280)
            * --{containerd}(281)
            * --{containerd}(287)
            * --{containerd}(1971)
        * --{dockerd}(213)
        * --{dockerd}(214)
        * --{dockerd}(215)
        * --{dockerd}(216)
        * --{dockerd}(231)
        * --{dockerd}(237)
        * --{dockerd}(322)
        * --{dockerd}(323)
        * --{dockerd}(325)
        * --{dockerd}(327)
    * --**logger(26)**
    * --**python(25)** * --editor-proxy(246)
        * --runuser(269) 
            * --sh(271) 
                * --node(286) 
                    * --node(287) 
                        * --gcloudcode_cli(3292)
                            * --{gcloudcode_cli}(+)
                            * --{gcloudcode_cli}(+)
                            * --{gcloudcode_cli}(+)

---
## Analisis
- Jelaskan makna hasil percobaan.
    Makna dari hasil semua percobaannya adalah untuk menguji dan memverifikasi prinsip-prinsip dasar dari manajemen proses dan manajemen pengguna dalam sebuah lingkungan Sistem Operasi Linux. Semua percobaan berhasil menunjukkan bagaimana kernel Linux mengelola identitas pengguna, mengalokasikan PID, mengontrol siklus hidup proses (seperti mengakhiri dengan kill), dan menyusun proses-proses tersebut ke dalam hierarki yang logis.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
  Inti dari semua percobaan tersebut adalah untuk memverifikasi tiga pilar arsitektur Sistem Operasi Linux: **Fungsi Kernel**, **System Call**, dan **Arsitektur Keamanan OS**. Hasil dari `ps aux`, `%CPU`, dan `Load Average` membuktikan fungsi **Kernel** dalam melakukan manajemen proses dan penjadwalan sumber daya secara efisien. Keberhasilan perintah `kill 3309` membuktikan implementasi **System Call**, di mana program di *user space* meminta Kernel untuk mengubah status proses. Sementara itu, output dari `id` dan `groups` menunjukkan penerapan **Arsitektur Keamanan OS**, di mana Kernel secara ketat mengawasi dan menegakkan hak akses (UID dan GID), memastikan bahwa pengguna hanya dapat memanipulasi proses yang mereka miliki. Secara keseluruhan, **`pstree -p`** adalah bukti visual dari bagaimana Kernel mengatur seluruh aktivitas sistem dalam sebuah **struktur hierarki** yang teratur, menegaskan bahwa semua layanan sistem berakar dari satu proses induk utama.  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
   Perbedaan hasil antara lingkungan Linux dan Windows terletak pada arsitektur inti dan utilitas command-line kedua OS. Di Linux, fokus utama ada pada hierarki proses yang ketat (pstree -p), di mana semua proses adalah turunan dari proses induk (bash(1)), dan identitas pengguna diatur oleh UID/GID. Sebaliknya, Windows berfokus pada daftar proses yang diurus oleh Kernel dengan penekanan kurang pada hubungan Parent-Child yang kaku, menggunakan Security Identifier (SID), bukan UID/GID, untuk manajemen identitas.
---

## Kesimpulan
Inti dari semua percobaan tersebut adalah untuk memverifikasi tiga pilar arsitektur Sistem Operasi Linux: **Fungsi Kernel**, **System Call**, dan **Arsitektur Keamanan OS**. Hasil dari `ps aux`, `%CPU`, dan `Load Average` membuktikan fungsi **Kernel** dalam melakukan manajemen proses dan penjadwalan sumber daya secara efisien. Keberhasilan perintah `kill 3309` membuktikan implementasi **System Call**, di mana program di *user space* meminta Kernel untuk mengubah status proses. Sementara itu, output dari `id` dan `groups` menunjukkan penerapan **Arsitektur Keamanan OS**, di mana Kernel secara ketat mengawasi dan menegakkan hak akses (UID dan GID), memastikan bahwa pengguna hanya dapat memanipulasi proses yang mereka miliki. Secara keseluruhan, **`pstree -p`** adalah bukti visual dari bagaimana Kernel mengatur seluruh aktivitas sistem dalam sebuah **struktur hierarki** yang teratur, menegaskan bahwa semua layanan sistem berakar dari satu proses induk utama.

---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?
   **Jawaban:Fungsi utama dari proses init (untuk sistem lama) atau systemd (untuk sebagian besar distribusi Linux modern) adalah bertindak sebagai proses induk tertinggi atau manajer sistem yang mengendalikan seluruh lingkungan operating system.**  
2. Apa perbedaan antara kill dan killall?
   **Jawaban:Perbedaan antara perintah kill dan killall di Linux terletak pada bagaimana mereka menargetkan proses yang akan dihentikan. Perintah kill menargetkan proses berdasarkan ID Proses (PID)-nya. Sedangkan perintah killall menargetkan proses berdasarkan nama program/perintah yang menjalankannya.**  
3.   Mengapa user root memiliki hak istimewa di sistem Linux?
   **Jawaban:Karena root adalah akun administrator utama yang dirancang untuk memiliki otoritas tak terbatas terhadap sistem operasi.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
 cara membuat diagram pstree.
- Bagaimana cara Anda mengatasinya?  
  bertanya kepada teman.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
