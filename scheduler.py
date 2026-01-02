class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs(processes):
    time = 0
    processes.sort(key=lambda x: x.arrival_time)
    print("\n--- FCFS Scheduling ---")
    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time
        p.waiting_time = time - p.arrival_time
        p.turnaround_time = p.waiting_time + p.burst_time
        time += p.burst_time
        print(f"Process {p.pid}: Waiting Time = {p.waiting_time}, Turnaround Time = {p.turnaround_time}")

def sjf(processes):
    time = 0
    completed = 0
    n = len(processes)
    is_completed = [False] * n
    print("\n--- SJF Scheduling ---")
    while completed != n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if processes[i].arrival_time <= time and not is_completed[i]:
                if processes[i].burst_time < min_bt:
                    min_bt = processes[i].burst_time
                    idx = i
        if idx != -1:
            p = processes[idx]
            p.waiting_time = time - p.arrival_time
            p.turnaround_time = p.waiting_time + p.burst_time
            time += p.burst_time
            is_completed[idx] = True
            completed += 1
            print(f"Process {p.pid}: Waiting Time = {p.waiting_time}, Turnaround Time = {p.turnaround_time}")
        else:
            time += 1

def round_robin(processes, quantum):
    time = 0
    queue = processes.copy()
    remaining_bt = {p.pid: p.burst_time for p in processes}
    waiting_time = {p.pid: 0 for p in processes}
    last_exec = {p.pid: p.arrival_time for p in processes}
    print("\n--- Round Robin Scheduling ---")
    while queue:
        p = queue.pop(0)
        if remaining_bt[p.pid] > quantum:
            time += quantum
            remaining_bt[p.pid] -= quantum
            queue.append(p)
        else:
            time += remaining_bt[p.pid]
            waiting_time[p.pid] += time - last_exec[p.pid] - remaining_bt[p.pid]
            remaining_bt[p.pid] = 0
            print(f"Process {p.pid}: Waiting Time = {waiting_time[p.pid]}, Turnaround Time = {waiting_time[p.pid] + p.burst_time}")
        last_exec[p.pid] = time
