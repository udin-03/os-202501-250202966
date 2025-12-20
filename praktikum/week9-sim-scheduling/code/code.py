# 1. Fungsi Simulasi (Menghitung Angka)
def simulasi_fcfs(daftar_proses):
    # Urutkan berdasarkan Waktu Datang (at)
    daftar_proses.sort(key=lambda x: x['at'])
    
    waktu_sekarang = 0
    for proses in daftar_proses:
        # Jika CPU menganggur, lompat ke waktu kedatangan proses
        if waktu_sekarang < proses['at']:
            waktu_sekarang = proses['at']
        
        # HITUNG FT: Finish Time (Waktu Selesai)
        proses['ft'] = waktu_sekarang + proses['bt']
        
        # HITUNG TAT: Turnaround Time (Lama di Sistem)
        proses['tat'] = proses['ft'] - proses['at']
        
        # HITUNG WT: Waiting Time (Waktu Tunggu)
        proses['wt'] = proses['tat'] - proses['bt']
        
        # Update waktu sekarang ke Finish Time proses ini
        waktu_sekarang = proses['ft']

# 2. Fungsi Menggambar (Visualisasi)
def gambar_gantt(daftar_proses):
    print("\nGantt Chart (Visualisasi Urutan Kerja CPU):")
    
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

    # Gambar Garis Waktu (Timeline) menggunakan 'ft'
    print("0", end="")
    for p in daftar_proses:
        print(f"{' ' * (p['bt'] + 2)}{p['ft']}", end="")
    print("\n")

# 3. Data Input
data_input = [
    {'id': 1, 'at': 0, 'bt': 6}, 
    {'id': 2, 'at': 1, 'bt': 8},
    {'id': 3, 'at': 2, 'bt': 7},
    {'id': 4, 'at': 3, 'bt': 3} 
]

# 4. Memanggil Fungsi Simulasi
simulasi_fcfs(data_input)

# Bagian Perhitungan Rata-rata
total_tat = 0
total_wt = 0
jumlah_proses = len(data_input)

for p in data_input:
    total_tat += p['tat']
    total_wt += p['wt']

rata_rata_tat = total_tat / jumlah_proses
rata_rata_wt = total_wt / jumlah_proses


# Tampilkan Tabel Hasil
print(f"{'Proses':<8} | {'AT':<3} | {'BT':<3} | {'FT':<3} | {'TAT':<3} | {'WT':<3}")
print("-" * 40)
for p in data_input:
    print(f"P{p['id']:<7} | {p['at']:<3} | {p['bt']:<3} | {p['ft']:<3} | {p['tat']:<3} | {p['wt']:<3}")

# Tampilkan Rata-rata
print("-" * 40)
print(f"Rata-rata Turnaround Time (TAT): {rata_rata_tat:.2f}")
print(f"Rata-rata Waiting Time (WT)   : {rata_rata_wt:.2f}")

# Tampilkan Gantt Chart
gambar_gantt(data_input)