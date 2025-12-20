
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Safrudin 
- **NIM**   : 250202966 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

- Mahasiswa mampu membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
- Mahasiswa mampu menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
- Mahasiswa mampu menyajikan output simulasi dalam bentuk tabel atau grafik.
- Mahasiswa mampu menjelaskan hasil simulasi secara tertulis.
- Mahasiwa mampu mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
- Prinsip Non-Preemptive: FCFS adalah algoritma penjadwalan yang bersifat non-preemptive. Artinya, begitu CPU dialokasikan untuk sebuah proses, proses tersebut akan memegang kendali CPU sampai ia selesai eksekusi atau berhenti secara sukarela. CPU tidak bisa "merebut" tugas di tengah jalan untuk beralih ke tugas lain.
- Mekanisme Antrean FIFO (First-In, First-Out): Logika dasarnya identik dengan antrean di dunia nyata. Proses yang masuk ke antrean ready paling awal dengan Arrival Time (AT) terkecil akan dilayani terlebih dahulu oleh CPU. Data dikelola menggunakan struktur data antrean.
- Metrik Kinerja (TAT & WT): Efisiensi algoritma diukur berdasarkan Turnaround Time (TAT) dan Waiting Time (WT). TAT mengukur total waktu sejak proses datang hingga selesai (FT - AT), sedangkan WT mengukur berapa lama proses menunggu di antrean sebelum dieksekusi (TAT - BT).

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
def simulasi_fcfs(daftar_proses):
    daftar_proses.sort(key=lambda x: x['at'])
    
    waktu_sekarang = 0
    for proses in daftar_proses:
        if waktu_sekarang < proses['at']:
            waktu_sekarang = proses['at']
        
        proses['ft'] = waktu_sekarang + proses['bt']
        
        proses['tat'] = proses['ft'] - proses['at']
        
        proses['wt'] = proses['tat'] - proses['bt']
        
        waktu_sekarang = proses['ft']

def gambar_gantt(daftar_proses):
    print("\nGantt Chart (Visualisasi Urutan Kerja CPU):")
    
    for p in daftar_proses:
        print("+" + "-" * (p['bt'] + 2), end="")
    print("+")

    for p in daftar_proses:
        print(f"| P{p['id']}{' ' * (p['bt'] - 1)}", end="")
    print("|")

    for p in daftar_proses:
        print("+" + "-" * (p['bt'] + 2), end="")
    print("+")

    print("0", end="")
    for p in daftar_proses:
        print(f"{' ' * (p['bt'] + 2)}{p['ft']}", end="")
    print("\n")

data_input = [
    {'id': 1, 'at': 0, 'bt': 6}, 
    {'id': 2, 'at': 1, 'bt': 8},
    {'id': 3, 'at': 2, 'bt': 7},
    {'id': 4, 'at': 3, 'bt': 3} 
]

simulasi_fcfs(data_input)

total_tat = 0
total_wt = 0
jumlah_proses = len(data_input)

for p in data_input:
    total_tat += p['tat']
    total_wt += p['wt']

rata_rata_tat = total_tat / jumlah_proses
rata_rata_wt = total_wt / jumlah_proses


print(f"{'Proses':<8} | {'AT':<3} | {'BT':<3} | {'FT':<3} | {'TAT':<3} | {'WT':<3}")
print("-" * 40)
for p in data_input:
    print(f"P{p['id']:<7} | {p['at']:<3} | {p['bt']:<3} | {p['ft']:<3} | {p['tat']:<3} | {p['wt']:<3}")

print("-" * 40)
print(f"Rata-rata Turnaround Time (TAT): {rata_rata_tat:.2f}")
print(f"Rata-rata Waiting Time (WT)   : {rata_rata_wt:.2f}")

gambar_gantt(data_input)
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](/praktikum/week9-sim-scheduling/screenshots/code.png)

![Screenshot hasil](/praktikum/week9-sim-scheduling/screenshots/Cuplikan%20layar%202025-12-20%20160012.png)

---

## Analisis
1. Alur eksekusi program. 
   - P1 datang pada waktu 0 dan langsung dieksekusi karena belum ada program lain yang datang dan harus dieksekusi. Program P1 selesai di waktu 6 karena memiliki BT 6.
   - P2 datang pada waktu 1 dan harus menunggu P1 selesai dieksekusi. P2 dieksekusi pada waktu 6 dan selesai pada waktu 14 karena memiliki BT 8.
   - P3 datang pada waktu 2 dan harus menunggu P1 dan P2 selesai dieksekusi. P3 dieksekusi pada waktu 14 dan selesai pada waktu 21 karena memiliki BT 7.
   - P4 datang pada waktu 3 dan harus menunggu P1,P2 dan P3 selesai dieksekusi. P4 dieksekusi pada waktu 21 dan selesai pada waktu 24 karena memiliki BT 3. 
2. Bandingkan hasil simulasi dengan perhitungan manual.
   Berdasarkan hasil yang terlihat, hasil perhitungan otomatis maupun perhitungan memiliki hasil yang sama.
3. Jelaskan kelebihan dan keterbatasan simulasi.
   - Kelebihan dalam simulasi ini adalah kita tidak perlu mencoba-coba algoritma langsung pada sistem operasi yang sedang berjalan karena berisiko membuat komputer crash.
   - Kekurangannya adalah simulasinya terlalu sederhana, tidak memperhitungkan gangguan yang mungkin muncul atau kemampuan kinerja hardware. Sehingga hasil simulasi tidak 100% sesuai kondisi di dunia nyata.

---
## Kesimpulan
- Keadilan Berdasarkan Urutan Kedatangan: Algoritma FCFS terbukti sebagai metode penjadwalan yang paling adil secara kronologis, karena menggunakan metode non-preemptive.
- Efisiensi Tergantung pada Variasi Burst Time: Jika proses pertama memiliki Burst Time yang sangat lama, maka akan terjadi lonjakan besar pada rata-rata Waiting Time bagi proses-proses berikutnya, yang secara teknis dikenal sebagai fenomena Convoy Effect.
- Akurasi Perhitungan melalui Simulasi: Melalui simulasi Python, dapat dibuktikan bahwa nilai Finish Time (FT) suatu proses merupakan akumulasi dari waktu mulai ditambah durasi kerjanya. Simulasi ini mempermudah visualisasi dan perhitungan metrik performa sistem (TAT dan WT) secara otomatis dibandingkan perhitungan manual yang rentan terhadap kesalahan manusia.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling? 
   **Jawaban:Karena menguji langsung pada komputer akan sangat beresiko jika terjadi kesalahan sistem dan dapat merusak komputer. Sehingga lebih aman jika mencobanya menggunakan simulasi.**  
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   **Jawaban:Jika perhitungan dataset besar akan lebih baik menggunakan simulasi dibandingkan dengan perhitungan manual, karena perhitungan simulasi memiliki akurasi yang lebih tingi.**  
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan. 
   **Jawaban:Algoritma FCFS, karena hanya perlu menjalankan proses berdasarkan urutan datang tidak perlu membandingkan BT terlebih dahulu.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
- Membuat program simulasi. 
- Bagaimana cara Anda mengatasinya?
- Menggunakan AI.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
