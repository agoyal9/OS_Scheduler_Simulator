# main.py

from scheduler import fcfs, sjf, round_robin
from deadlock import DeadlockSimulation
from utils import read_processes_csv, read_resource_csv

# Read processes for scheduling
processes = read_processes_csv('sample_input.csv')

# Run Scheduling Algorithms
fcfs(processes)
sjf(processes)
round_robin(processes, quantum=2)

# Read resource allocation for deadlock simulation
process_alloc, resources = read_resource_csv('resource_allocation.csv', 'resources.csv')

# Run Deadlock Detection
dl_sim = DeadlockSimulation(process_alloc, resources)
deadlocked = dl_sim.detect_deadlock()
print("\nDeadlocked Processes:", deadlocked if deadlocked else "None")
