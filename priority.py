def priority_scheduling(processes):

    processes = sorted(processes, key=lambda x: x["arrival"])

    time = 0
    gantt = []
    waiting = []
    turnaround = []

    while processes:

        available = [p for p in processes if p["arrival"] <= time]

        if not available:
            time += 1
            continue

        highest = min(available, key=lambda x: x["priority"])

        start = time
        finish = time + highest["burst"]

        gantt.append((highest["pid"], start, finish))

        wt = start - highest["arrival"]
        tat = finish - highest["arrival"]

        waiting.append(wt)
        turnaround.append(tat)

        time = finish

        processes.remove(highest)

    avg_wt = sum(waiting) / len(waiting)
    avg_tat = sum(turnaround) / len(turnaround)

    return gantt, avg_wt, avg_tat