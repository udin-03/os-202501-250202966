
# Laporan Praktikum Minggu 11
Topik:  Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Safrudin   
- **NIM**   : 250202966   
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

- Mahasiswa mampu membuat program sederhana untuk mendeteksi deadlock.
- Mahasiswa mampu menjalankan simulasi deteksi deadlock dengan dataset uji.
- Mahasiswa mampu menyajikan hasil analisis deadlock dalam bentuk tabel.
- Mahasiswa mampu memberikan interpretasi hasil uji secara logis dan sistematis.
- Mahasiswa mampu menyusun laporan praktikum sesuai format yang ditentukan

---

## Dasar Teori
1. Deadlock adalah suatu kondisi di mana sekumpulan proses tidak dapat melanjutkan eksekusinya karena setiap proses sedang menunggu resource yang sedang dipegang oleh proses lain dalam kelompok tersebut.

2. Empat kondisi yang menyebabkan deadlock:

   - Mutual Exclusion: Resource tidak dapat digunakan bersama.

   - Hold and Wait: Proses memegang satu resource sambil meminta resource lain.

   - No Preemption: Resource tidak bisa diambil paksa dari proses lain.

   - Circular Wait: Terdapat rantai melingkar dari proses-proses yang saling menunggu.

3. Wait-For Graph (WFG): Pada sistem dengan single-instance resource (satu resource hanya punya satu unit), kondisi deadlock dapat dipresentasikan menggunakan graf arah. Titik (node) mewakili proses, dan garis arah (edge) mewakili hubungan tunggu. Jika terbentuk siklus (cycle) pada graf ini, maka dipastikan terjadi deadlock.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash

# Eksekusi
result = detect_deadlock(processes, allocation, request)

print("=== Hasil Deteksi Deadlock ===")
if result:
    print(f"Status: TERJADI DEADLOCK")
    print(f"Proses yang terlibat: {', '.join(sorted(result))}")
else:
    print("Status: SISTEM AMAN (Tidak ada Deadlock)")
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](/praktikum/week11-deadlock-detection/screenshots/Cuplikan%20layar%202026-01-04%20152818.png)

---

## Analisis

   | Proses | Allocation | Request | Keterangan |
   |:--:|:--:|:--:| :--: |
   | P1 | R1 | R2 | Terjadi deadlock. Karena, P1 memegang R1 dan meminta R2 yang sedang dipegang P2. |
   | P2 | R2 | R3 | Terjadi deadlock. Karena, P2 memegang R2 dan meminta R3 yang sedang dipegang P3. |
   | P3 | R3 | R1 | Terjadi deadlock. Karena, P3 memegang R3 dan meminta R1 yang sedang dipegang P1. |

Deadlock terjadi karena ketiga proses ini (P1, P2, P3) akan selamanya saling tunggu dan resource yang mereka butuhkan tidak pernah dilepaskan oleh pemegangnya.

Kaitannya dengan empat kondisi Deadlock: 
   - Mutual Exclusion: Resource (R1, R2, R3) bersifat non-sharable, hanya satu proses yang bisa menggunakannya di satu waktu.
   - Hold and Wait: P1 memegang R1 sambil menunggu R2 diberikan.
   - No Preemption: Resource tidak bisa dipaksa lepas dari proses yang sedang memegangnya, P1 tidak bisa mengambil paksa R2 dari P2.
   - Circular Wait: Terbentuk rantai melingkar di mana P1 menunggu P2, P2 menunggu P3, dan P3 menunggu P1.

---

## Kesimpulan
1. Ketergantungan terhadap Empat Kondisi Deadlock, hasil percobaan menunjukkan bahwa deadlock tidak terjadi secara acak, melainkan akibat terpenuhinya empat kondisi (Mutual Exclusion, Hold and Wait, No Preemption, dan Circular Wait). Jika salah satu kondisi tersebut diputus, misalnya dengan mengizinkan preemption (pengambilalihan resource) maka deadlock dapat dihindari atau dipulihkan.
2. Praktikum ini membuktikan bahwa pada sistem dengan single-instance resource, munculnya Circular Wait (siklus) dalam Wait-For Graph adalah syarat mutlak terjadinya deadlock. Tanpa adanya siklus, sistem dipastikan berada dalam kondisi aman meskipun ada proses yang harus mengantre.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?  
   **Jawaban:**
   - **Deadlock prevention, strategi ini bekerja dengan memastikan sebelum proses berjalan salah satu dari kondisi yang menyebabkan Deadlock (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) tidak terjadi.**
   - **Deadlock avoidance, strategi ini bekerja pada saat proses berjalan dengan cara memprediksi apa yang akan terjadi jika memberikan resource kepada proses. Prediksi ini didasarkan pada informasi awal proses yang akan berjalan.**
   - **Deadlock detection, strategi ini bekerja dengan cara membiarkan semua proses berjalan. Lalu jika terjadi Deadlock, strategi ini akan bekerja untuk menghentikan proses dan memperbaikinya agar proses bisa berjalan lagi.**  
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
   **Jawaban:Deteksi deadlock tetap diperlukan karena, deteksi memungkinkan resource digunakan secara maksimal tanpa batasan di awal, dan algoritma pemantauannya hanya dijalankan secara berkala sehingga tidak membebani performa CPU secara terus-menerus. Ketika deadlock ditemukan melalui deteksi ini, sistem operasi dapat mengambil tindakan pemulihan yang tepat, seperti melakukan terminasi pada salah satu proses atau melakukan pengambilan paksa resource (preemption) untuk memutus rantai lingkaran setan tersebut dan mengembalikan sistem ke kondisi normal.**  
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock? 
   **Jawaban:**
   - **Kelebihannya adalah tidak menghambat jalannya proses dan resource digunakan secara maksimal.**  
   - **Kekurangannya adalah ada biaya performa untuk menjalankan algoritma deteksi dan risiko kehilangan data saat proses dihentikan paksa untuk pemulihan.**

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
