def detect_deadlock(processes, allocation, request):
    # Gabungkan semua resource unik
    resources = set()
    for res_list in allocation.values():
        resources.update(res_list)
    for res_list in request.values():
        resources.update(res_list)
    
    # Membangun Wait-For Graph
    # Node adalah proses. Busur P1 -> P2 ada jika P1 menunggu resource yang dipegang P2.
    graph = {p: set() for p in processes}
    
    for p_waiting, req_res_list in request.items():
        for res in req_res_list:
            # Cari siapa yang memegang resource ini
            for p_holding, alloc_res_list in allocation.items():
                if res in alloc_res_list:
                    graph[p_waiting].add(p_holding)

    def has_cycle(v, visited, stack, cycle_nodes):
        visited.add(v)
        stack.add(v)
        
        for neighbor in graph[v]:
            if neighbor not in visited:
                if has_cycle(neighbor, visited, stack, cycle_nodes):
                    cycle_nodes.add(v)
                    return True
            elif neighbor in stack:
                cycle_nodes.add(v)
                cycle_nodes.add(neighbor)
                return True
        
        stack.remove(v)
        return False

    visited = set()
    stack = set()
    deadlocked_processes = set()

    for process in processes:
        if process not in visited:
            if has_cycle(process, visited, stack, deadlocked_processes):
                pass # Cycle found

    return list(deadlocked_processes)

# Dataset Uji
processes = ['P1', 'P2', 'P3']
allocation = {
    'P1': ['R1'],
    'P2': ['R2'],
    'P3': ['R3']
}
request = {
    'P1': ['R2'],
    'P2': ['R3'],
    'P3': ['R1']
}

# Eksekusi
result = detect_deadlock(processes, allocation, request)

print("=== Hasil Deteksi Deadlock ===")
if result:
    print(f"Status: TERJADI DEADLOCK")
    print(f"Proses yang terlibat: {', '.join(sorted(result))}")
else:
    print("Status: SISTEM AMAN (Tidak ada Deadlock)")