#Simulasi FIFO
def simulate_fifo(pages, capacity):
    memory = []
    faults = 0
    hits = 0
    
    print(f"{'Step':<6} | {'Page':<6} | {'Memory State':<15} | {'Status'}")
    print("-" * 45)

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
        
        # Menampilkan status memori saat ini
        print(f"{i+1:<6} | {page:<6} | {str(memory):<15} | {status}")

    print("-" * 45)
    print(f"Total Page Faults: {faults}")
    print(f"Total Page Hits  : {hits}")

# Data Eksekusi
ref_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3
simulate_fifo(ref_string, frames)

#Simulasi LRU
def simulate_lru(pages, capacity):
    memory = []
    faults = 0
    hits = 0
    
    print(f"{'Step':<6} | {'Page':<6} | {'Memory State':<15} | {'Status'}")
    print("-" * 45)

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
        
        print(f"{i+1:<6} | {page:<6} | {str(memory):<15} | {status}")

    print("-" * 45)
    print(f"Total Page Faults: {faults}")
    print(f"Total Page Hits  : {hits}")

# Data Eksekusi
ref_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3
simulate_lru(ref_string, frames)