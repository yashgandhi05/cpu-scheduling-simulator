def sjf_non_preemptive(processes):
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

        shortest = min(available, key=lambda x: x["burst"])

        start = time
        finish = time + shortest["burst"]

        gantt.append((shortest['pid'], start, finish))

        wt = start - shortest["arrival"]
        tat = finish - shortest["arrival"]

        waiting.append(wt)
        turnaround.append(tat)

        time = finish

        processes.remove(shortest)

    avg_wt = sum(waiting)/len(waiting)
    avg_tat = sum(turnaround)/len(turnaround)

    return gantt, avg_wt, avg_tat