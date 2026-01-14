
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Safrudin   
- **NIM**   : 250202966  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini. 

- Mahasiswa mampu menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
- Mahasiswa mampu membangun image dan menjalankan container.
- Mahasiswa mampu menjalankan container dengan pembatasan CPU dan memori.
- Mahasiswa mampu mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
- Mahasiswa mampu menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
1. Control Groups (cgroups): Docker menggunakan fitur kernel Linux yang disebut cgroups untuk membatasi, mencatat, dan mengisolasi penggunaan sumber daya fisik (seperti CPU, memori, dan I/O disk) dari sekumpulan proses. Inilah teknologi di balik layar yang memungkinkan parameter --cpus dan --memory bekerja.

2. Isolasi Resource: Container bersifat terisolasi dari host dan container lainnya. Tanpa pembatasan sumber daya, sebuah container dapat mengonsumsi seluruh RAM atau CPU dari mesin host (fenomena Noisy Neighbor), yang berisiko menyebabkan kegagalan sistem pada layanan lain yang berjalan di mesin yang sama.

3. CPU Throttling: Saat kita memberikan limit CPU (misal --cpus="0.5"), Docker tidak benar-benar mematikan core prosesor, melainkan mengatur jadwal waktu penggunaan CPU (time slicing). Container hanya diberikan jatah waktu tertentu untuk menggunakan prosesor dalam setiap periode, yang secara visual terlihat sebagai penurunan persentase penggunaan di docker stats.

4. OOM (Out of Memory) Killer: Docker dan sistem operasi memiliki mekanisme keamanan bernama OOM Killer. Jika sebuah container mencoba menggunakan memori melebihi batas yang ditentukan (dan memori swap juga habis), sistem akan secara paksa mematikan proses di dalam container tersebut untuk melindungi integritas sistem host. Inilah alasan mengapa container bisa berhenti tiba-tiba dengan status "Killed".

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
docker version
docker ps
docker build -t week13-resource-limit .
docker run --rm week13-resource-limit
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
docker stats
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week13-docker-resource-limit/screenshots/Docker_verifikasi.png)

![Screenshot hasil](/praktikum/week13-docker-resource-limit/screenshots/Docker_build.png)

![Screenshot hasil](/praktikum/week13-docker-resource-limit/screenshots/Docker_tanpa_limit.png)

![Screenshot hasil](/praktikum/week13-docker-resource-limit/screenshots/Monitoring_tanpa_limit.png)

![Screenshot hasil](/praktikum/week13-docker-resource-limit/screenshots/Docker_limit.png)

![Screenshot hasil](/praktikum/week13-docker-resource-limit/screenshots/Monitoring_limit.png)

---

## Analisis
1. Analisis Efektivitas Pembatasan CPU (--cpus="0.5")
   - Berdasarkan pengamatan pada docker stats selama proses "Komputasi CPU Intensif":
   Tanpa Limit: Container akan mencoba mengambil daya prosesor sebanyak mungkin. Pada mesin multi-core, satu proses single-threaded Python biasanya akan menggunakan 100% dari satu core.
   - Dengan Limit: Meskipun kode program dirancang untuk melakukan looping tanpa henti (yang seharusnya memakan 100% CPU), Docker berhasil membatasi utilisasi maksimal hanya pada 50.00%.
   - Dampak: Waktu yang dibutuhkan untuk menyelesaikan setiap langkah komputasi menjadi lebih lama (dua kali lipat). Ini menunjukkan bahwa mekanisme CPU Throttling pada Docker berjalan dengan sempurna untuk mencegah satu container mendominasi daya prosesor host.

2. Analisis Perilaku Memori (--memory="256m")
Ada temuan menarik di mana program tidak mengalami crash meskipun total alokasi teoritis mencapai 500MB (10 langkah × 50MB):
   - Manajemen Swap: Pada Docker Desktop (Windows), limitasi --memory tidak secara otomatis mematikan program jika masih ada Memory Swap yang tersedia. Container memindahkan data yang jarang diakses dari RAM ke disk (swap) sehingga program tetap bisa berjalan hingga selesai.
   - Keamanan Sistem: Meskipun tidak crash, Docker menjamin bahwa penggunaan RAM fisik tidak akan melewati 256MB. Ini melindungi host dari kegagalan sistem total akibat kehabisan memori (Out of Memory).

---

## Kesimpulan
1. Efektivitas Isolasi Resource: Docker terbukti mampu membatasi penggunaan daya komputasi secara presisi. Meskipun aplikasi menjalankan looping intensif yang secara normal akan menghabiskan 100% kapasitas satu core CPU, penggunaan parameter --cpus="0.5" berhasil mengunci utilisasi maksimal pada angka 50%. Hal ini memastikan stabilitas sistem host agar tidak didominasi oleh satu container tunggal.

2. Mekanisme Pembatasan Memori dan Swap: Pembatasan memori sebesar 256m bertindak sebagai ambang batas penggunaan RAM fisik. Namun, keberhasilan program menyelesaikan 10 langkah (sekitar 500MB alokasi) menunjukkan bahwa Docker (terutama pada Docker Desktop) memanfaatkan Memory Swap sebagai cadangan. Ini membuktikan bahwa Docker memberikan perlindungan berlapis: menjaga RAM fisik tetap aman sambil tetap mengupayakan aplikasi berjalan melalui memori virtual.

3. Pentingnya Manajemen Resource dalam Deployment: Praktikum ini menegaskan bahwa penentuan limit resource sangat krusial dalam arsitektur mikroservis. Tanpa limitasi, sebuah container yang mengalami bug (seperti kebocoran memori atau loop tak terbatas) dapat menyebabkan efek domino yang mematikan seluruh server. Dengan limitasi, dampak masalah tersebut hanya terisolasi di dalam container itu sendiri.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
   **Jawaban:Karena jika container dibiarkan berjalan tanpa batasan, ia akan berperilaku rakus dan mengambil apa pun yang tersedia di mesin host.**  
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
   **Jawaban:**  
   **- Virtual Machine (VM) melakukan isolasi di tingkat perangkat keras. VM biasanya menggunakan alokasi statis. Karena harus melakukan booting seluruh sistem operasi dari awal, VM membutuhkan waktu hitungan menit untuk siap digunakan dan memakan ruang disk yang besar (ukuran Gigabyte).**
   **- Container melakukan isolasi di tingkat sistem operasi. Container bersifat dinamis dan jauh lebih ringan. Karena hanya menjalankan proses aplikasi di atas kernel yang sudah ada, container bisa menyala dalam hitungan detik. Ukurannya pun sangat kecil (ukuran Megabyte) karena tidak membawa file sistem operasi yang lengkap.**
3. Apa dampak limit memori terhadap aplikasi yang boros memori? 
   **Jawaban:** 
   **- Dampak yang paling sering terjadi adalah aplikasi dimatikan secara paksa oleh Docker atau sistem operasi.**
   **- Jika sistem tidak langsung mematikan aplikasi, biasanya sistem akan memaksa aplikasi menggunakan Swap (memori cadangan di harddisk).** 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
