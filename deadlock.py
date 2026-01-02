class DeadlockSimulation:
    def __init__(self, processes, resources):
        """
        processes: dict {pid: [allocated_resources]}
        resources: dict {resource: available_count}
        """
        self.processes = processes
        self.resources = resources

    def detect_deadlock(self):
        work = self.resources.copy()
        finish = {p: False for p in self.processes}
        while True:
            progress = False
            for p, alloc in self.processes.items():
                if not finish[p]:
                    # check if all requested resources <= available
                    if all(work.get(r, 0) >= alloc.get(r, 0) for r in alloc):
                        for r in alloc:
                            work[r] += alloc[r]  # release resources
                        finish[p] = True
                        progress = True
            if not progress:
                break
        deadlocked = [p for p, done in finish.items() if not done]
        return deadlocked
