
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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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

* **bash(1)** * --**dockerd(207)** * --**containerd(234)** * --{containerd}(252)
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
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
