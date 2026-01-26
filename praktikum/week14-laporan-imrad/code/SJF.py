# 1. Fungsi Simulasi (SJF Non-Preemptive)
def simulasi_sjf(daftar_proses):
    # Urutkan awal berdasarkan Waktu Datang (at)
    daftar_proses.sort(key=lambda x: x['at'])
    
    waktu_sekarang = 0
    proses_selesai = []
    antrian_siap = []
    data_asli = daftar_proses.copy()

    while len(proses_selesai) < len(data_asli):
        # Masukkan semua proses yang sudah datang ke dalam antrian_siap
        for p in data_asli:
            if p['at'] <= waktu_sekarang and p not in antrian_siap and p not in proses_selesai:
                antrian_siap.append(p)

        if antrian_siap:
            # --- INTI SJF: Urutkan antrian berdasarkan Burst Time (BT) terkecil ---
            antrian_siap.sort(key=lambda x: x['bt'])
            
            # Ambil proses dengan BT terpendek
            proses = antrian_siap.pop(0)
            
            # HITUNG FT: Finish Time
            proses['ft'] = waktu_sekarang + proses['bt']
            # HITUNG TAT: Turnaround Time
            proses['tat'] = proses['ft'] - proses['at']
            # HITUNG WT: Waiting Time
            proses['wt'] = proses['tat'] - proses['bt']
            
            # Update waktu dan daftar selesai
            waktu_sekarang = proses['ft']
            proses_selesai.append(proses)
        else:
            # Jika belum ada proses yang datang, maju ke waktu kedatangan proses berikutnya
            waktu_sekarang += 1

    # Mengembalikan daftar yang sudah diproses untuk ditampilkan
    return proses_selesai

# 2. Fungsi Menggambar (Visualisasi)
def gambar_gantt(daftar_proses):
    print("\nGantt Chart (Visualisasi Urutan Kerja CPU - SJF):")
    
    # Gambar Garis Atas
    for p in daftar_proses:
        print("+" + "-" * (p['bt'] + 2), end="")
    print("+")

    # Gambar ID Proses di Tengah
    for p in daftar_proses:
        print(f"| P{p['id']}{' ' * (p['bt'] - 1)}", end="")
    print("|")

    # Gambar Garis Bawah
    for p in daftar_proses:
        print("+" + "-" * (p['bt'] + 2), end="")
    print("+")

    # Gambar Garis Waktu (Timeline)
    waktu_awal = 0
    print("0", end="")
    for p in daftar_proses:
        # Menyesuaikan spasi agar angka FT tepat berada di bawah garis pemisah
        print(f"{' ' * (p['bt'] + 2)}{p['ft']}", end="")
    print("\n")

# 3. Data Input
data_input = [
    {'id': 1, 'at': 0, 'bt': 7}, 
    {'id': 2, 'at': 1, 'bt': 9},
    {'id': 3, 'at': 2, 'bt': 4},
    {'id': 4, 'at': 3, 'bt': 3},
    {'id': 5, 'at': 4, 'bt': 5} 
]

# 4. Memanggil Fungsi Simulasi SJF
hasil_simulasi = simulasi_sjf(data_input)

# Bagian Perhitungan Rata-rata
total_tat = sum(p['tat'] for p in hasil_simulasi)
total_wt = sum(p['wt'] for p in hasil_simulasi)
jumlah_proses = len(hasil_simulasi)

rata_rata_tat = total_tat / jumlah_proses
rata_rata_wt = total_wt / jumlah_proses

# Tampilkan Tabel Hasil
print(f"{'Proses':<8} | {'AT':<3} | {'BT':<3} | {'FT':<3} | {'TAT':<3} | {'WT':<3}")
print("-" * 40)
# Urutkan kembali berdasarkan ID untuk tabel agar rapi
for p in sorted(hasil_simulasi, key=lambda x: x['id']):
    print(f"P{p['id']:<7} | {p['at']:<3} | {p['bt']:<3} | {p['ft']:<3} | {p['tat']:<3} | {p['wt']:<3}")

# Tampilkan Rata-rata
print("-" * 40)
print(f"Rata-rata Turnaround Time (TAT): {rata_rata_tat:.2f}")
print(f"Rata-rata Waiting Time (WT)   : {rata_rata_wt:.2f}")

# Tampilkan Gantt Chart
gambar_gantt(hasil_simulasi)