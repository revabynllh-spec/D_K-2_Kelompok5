class Process:

  def _init_(self, pid, arrival, burst, priority):
    self.pid = pid
    self.arrival = arrival
    self.burst = burst
    self.remaining = burst
    self.priority = priority
    self.start_time = -1
    self.finish_time = 0


def simulate_fcfs(processes):
  procs = sorted(processes, key=lambda x: x.arrival)
  time = 0
  for p in procs:
    if time < p.arrival:
      time = p.arrival
    p.start_time = time
    time += p.burst
    p.finish_time = time

  print_metrics("FCFS", procs)


def print_metrics(name, procs):
  avg_wt = sum(
      p.finish_time - p.arrival - p.burst for p in procs
  ) / len(procs)
  avg_tat = sum(p.finish_time - p.arrival for p in procs) / len(procs)
  avg_rt = sum(p.start_time - p.arrival for p in procs) / len(procs)
  print(f"=== {name} ===")
  print(f"Avg WT: {avg_wt:.2f} | Avg TAT: {avg_tat:.2f} | Avg RT: {avg_rt:.2f}\n")


dataset = [
    Process("P1", 0, 5, 2),
    Process("P2", 2, 3, 1),
    Process("P3", 3, 10, 4),
    Process("P4", 4, 4, 2),
    Process("P5", 7, 6, 3),
]

simulate_fcfs(dataset)