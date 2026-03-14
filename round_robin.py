def round_robin(processes, time_quantum):

    time = 0
    gantt = []

    remaining = {p["pid"]: p["burst"] for p in processes}

    arrival = {p["pid"]: p["arrival"] for p in processes}

    waiting = {p["pid"]: 0 for p in processes}
    turnaround = {}

    queue = []
    processes = sorted(processes, key=lambda x: x["arrival"])

    i = 0

    while queue or i < len(processes):

        while i < len(processes) and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1
            continue

        current = queue.pop(0)

        pid = current["pid"]

        start = time
        execute = min(time_quantum, remaining[pid])

        time += execute
        remaining[pid] -= execute

        gantt.append((pid, start, time))

        while i < len(processes) and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        if remaining[pid] > 0:
            queue.append(current)
        else:
            turnaround[pid] = time - arrival[pid]
            waiting[pid] = turnaround[pid] - current["burst"]

    avg_wt = sum(waiting.values()) / len(waiting)
    avg_tat = sum(turnaround.values()) / len(turnaround)

    return gantt, avg_wt, avg_tat