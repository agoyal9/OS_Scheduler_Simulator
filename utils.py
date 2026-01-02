import csv
from scheduler import Process

def read_processes_csv(filename):
    processes = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            processes.append(Process(int(row['PID']), int(row['ArrivalTime']), int(row['BurstTime'])))
    return processes

def read_resource_csv(allocation_file, resources_file):
    process_alloc = {}
    resources = {}
    with open(allocation_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pid = int(row['PID'])
            process_alloc[pid] = {r: int(row[r]) for r in row if r != 'PID'}
    with open(resources_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            resources[row['Resource']] = int(row['Count'])
    return process_alloc, resources
