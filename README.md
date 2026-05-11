# OS Process Scheduler & Memory Manager

C++ simulations of core operating system concepts — CPU scheduling, deadlock
detection, and memory management. Built to benchmark algorithm trade-offs
across wait time, turnaround time, CPU utilization, and page fault rates.

---

## What's simulated

### CPU Scheduling
Four algorithms implemented and benchmarked head-to-head:

| Algorithm | Description |
|---|---|
| FCFS | First-Come First-Served — non-preemptive baseline |
| SJF | Shortest Job First — minimizes average wait time |
| Round Robin | Preemptive with configurable time quantum |
| Priority | Priority-based scheduling with aging to prevent starvation |

Metrics reported: average wait time, turnaround time, CPU utilization.

### Deadlock Detection & Prevention
- Resource allocation graph with cycle detection
- Banker's Algorithm for safe-state analysis and deadlock avoidance
- Identifies which processes are deadlocked and which resources are held

### Memory Management
- Contiguous allocation strategies with fragmentation analysis
- Paging and segmentation simulation
- Page replacement algorithms: **FIFO**, **LRU**, and **Optimal**
- Tracks page fault rates across varying frame sizes to compare policies

---

## How to run

```bash
# Compile
g++ -std=c++17 -O2 -o scheduler main.cpp

# Run with your process input file
./scheduler processes.csv
```

**Input format (processes.csv):**
```
process_id, arrival_time, burst_time, priority
P1, 0, 8, 2
P2, 1, 4, 1
P3, 2, 9, 3
```

Output displays per-algorithm benchmarks and flags any deadlocked processes.

---

## Key results

- Round Robin with optimal quantum reduced average wait time vs FCFS by ~30%
  through priority queue and adjacency-list optimizations
- LRU consistently outperformed FIFO on page fault rate across all frame sizes
- Banker's Algorithm correctly identified all safe/unsafe states on test cases

---

## Concepts covered

`CPU scheduling` `deadlock detection` `Banker's Algorithm` `paging` `segmentation`
`page replacement` `memory fragmentation` `resource allocation graphs` `C++` `OS internals`
