
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Safrudin  
- **NIM**   : 250202966  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- Mahasiswa mampu mengimplementasikan algoritma page replacement FIFO dalam program.
- Mahasiswa mampu mengimplementasikan algoritma page replacement LRU dalam program.
- Mahasiswa mampu menjalankan simulasi page replacement dengan dataset tertentu.
- Mahasiswa mampu membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
- Mahasiswa mampu menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
- **Konsep Memori Virtual**: Sistem yang memungkinkan eksekusi proses yang ukurannya melampaui kapasitas fisik RAM dengan cara membagi program menjadi unit-unit kecil yang disebut pages. Hanya page yang sedang dibutuhkan yang dimuat ke dalam RAM.

- **Mekanisme Page Fault**: Kondisi yang terjadi ketika CPU mencoba mengakses halaman yang tidak ada di memori fisik. Hal ini memicu sistem operasi untuk mengambil halaman tersebut dari memori sekunder (disk) dan menempatkannya di salah satu frame RAM yang kosong.

- **Algoritma Penggantian Halaman (Page Replacement)**: Ketika RAM penuh dan terjadi page fault, algoritma ini bertugas memilih halaman mana yang harus dikeluarkan (victim page) untuk memberi ruang bagi halaman baru. Tujuan utamanya adalah meminimalkan jumlah page fault.

- **Karakteristik FIFO (First-In First-Out)**: Mengganti halaman berdasarkan waktu kedatangan paling awal. Algoritma ini mudah diimplementasikan tetapi tidak efisien karena mengabaikan frekuensi akses halaman dan berisiko mengalami Belady's Anomaly.

- **Karakteristik LRU (Least Recently Used)**: Mengganti halaman yang paling lama tidak diakses oleh CPU. Algoritma ini didasarkan pada prinsip Temporal Locality, di mana halaman yang baru saja digunakan memiliki peluang besar untuk digunakan kembali dalam waktu dekat.
  
---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
1. **FIFO** 
```bash
    for i, page in enumerate(pages):
        status = ""
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0) # Menghapus elemen tertua (indeks 0)
                memory.append(page)
            faults += 1
            status = "FAULT"
        else:
            hits += 1
            status = "HIT"
```
2. **LRU**
```bash
for i, page in enumerate(pages):
        status = ""
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Hapus elemen indeks 0 (yang paling lama tidak digunakan)
                memory.pop(0)
                memory.append(page)
            faults += 1
            status = "FAULT"
        else:
            # Pindahkan halaman yang hit ke posisi paling belakang
            memory.remove(page)
            memory.append(page)
            hits += 1
            status = "HIT"
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](/os-202501-250202966/praktikum/week10-page-replacement/screenshots/FIFO.png)

![Screenshot hasil](/os-202501-250202966/praktikum/week10-page-replacement/screenshots/LRU.png)

---

## Analisis

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | Kurang efisien namun sederhana |
   | LRU | 9 | Efisien namun lebih kompleks |

**Mengapa jumlah *page fault* bisa berbeda.**
-  **FIFO (First-In First-Out)**: Mendapatkan hasil *page fault* 10, karena hanya melihat kapan halaman itu masuk. Halaman yang sudah lama di RAM akan dibuang, tidak peduli apakah halaman itu masih sering dipakai atau tidak.
-  **LRU (Least Recently Used)**:  Mendapatkan hasil *page fault* 9, karena LRU melihat kapan terakhir kali halaman itu disentuh oleh CPU. Halaman yang baru saja diakses akan dianggap "berharga" dan diberi proteksi agar tidak dibuang.
  
**Algoritma yang lebih efisien**
- **LRU (Least Recently Used)** lebih efisien, karena menghasilkan *page fault* yang lebih sedikit. Program cenderung menggunakan data yang sama secara berulang dalam waktu singkat. Jika sebuah halaman baru saja diakses (Page Hit), LRU akan memperbarui status halaman tersebut menjadi "baru digunakan" dan melindunginya agar tidak dihapus.
- **FIFO (First-In First-Out)** kurang efisien, karena menghasilkan *page fault* yang lebih banyak. FIFO mengabaikan aktivitas CPU. Walaupun sebuah halaman sangat sering digunakan, FIFO tetap akan membuangnya hanya karena halaman tersebut sudah lama berada di RAM.

---

## Kesimpulan
- **Efisiensi Berdasarkan Data**: Berdasarkan hasil simulasi, algoritma LRU lebih efisien dibandingkan FIFO karena menghasilkan jumlah page fault yang lebih sedikit. Hal ini membuktikan bahwa program berdasarkan riwayat penggunaan data jauh lebih efektif daripada sekadar urutan kedatangan.

- **Pentingnya Mekanisme Page Hit**: Perbedaan jumlah fault terjadi karena cara kedua algoritma menangani Page Hit. LRU memperbarui status halaman yang sering diakses agar tetap berada di memori (RAM), sementara FIFO membuang halaman secara buta tanpa mempertimbangkan apakah halaman tersebut masih dibutuhkan oleh CPU atau tidak.

- **Korelasi Performa Sistem**: Pengurangan jumlah page fault pada algoritma LRU secara langsung meningkatkan performa sistem operasi. Karena akses ke memori fisik (RAM) jauh lebih cepat daripada memori sekunder (Disk), pemilihan algoritma page replacement yang tepat sangat krusial untuk meminimalkan latensi dan overhead pada sistem.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU? 
   **Jawaban:**
   - **FIFO: Menggunakan waktu kedatangan (arrival time). Halaman yang sudah paling lama berada di memori akan diganti lebih dulu, tanpa memedulikan apakah halaman tersebut masih sering digunakan atau tidak.**
   - **LRU: Menggunakan waktu penggunaan terakhir (last access time). Halaman yang sudah paling lama tidak disentuh atau diakses oleh CPU akan diganti lebih dulu.**  
2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?
   **Jawaban:FIFO dapat mengalami Belady's Anomaly karena kriterianya yang kaku (hanya berdasarkan waktu masuk) mengabaikan frekuensi dan waktu akses terakhir. Hal ini menyebabkan penambahan memori terkadang mengganggu ritme antrean dan membuang halaman krusial yang seharusnya masih dipertahankan jika jumlah frame lebih sedikit.**  
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:LRU menghasilkan performa yang lebih baik karena, LRU meminimalkan page fault dengan cara mempertahankan halaman yang aktif digunakan, sementara FIFO sering membuang halaman penting hanya karena faktor umur.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
- membagi waktu soalnya tugasnya numpuk. 
- Bagaimana cara Anda mengatasinya?  
- menyelesaikannya satu per satu.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
