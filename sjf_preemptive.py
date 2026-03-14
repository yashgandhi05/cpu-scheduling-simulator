def sjf_preemptive(processes):

    n = len(processes)

    remaining = [p["burst"] for p in processes]
    arrival = [p["arrival"] for p in processes]
    pid = [p["pid"] for p in processes]

    complete = 0
    time = 0
    minm = float("inf")
    shortest = None
    finish_time = 0

    waiting = [0]*n
    turnaround = [0]*n

    gantt = []
    prev = None
    start = 0

    while complete != n:

        for i in range(n):
            if arrival[i] <= time and remaining[i] < minm and remaining[i] > 0:
                minm = remaining[i]
                shortest = i

        if shortest is None:
            time += 1
            continue

        if prev != pid[shortest]:
            if prev is not None:
                gantt.append((prev, start, time))
            start = time
            prev = pid[shortest]

        remaining[shortest] -= 1
        minm = remaining[shortest]

        if remaining[shortest] == 0:
            complete += 1
            finish_time = time + 1

            waiting[shortest] = finish_time - arrival[shortest] - processes[shortest]["burst"]
            turnaround[shortest] = finish_time - arrival[shortest]

            minm = float("inf")

        time += 1

    gantt.append((prev, start, time))

    avg_wt = sum(waiting)/n
    avg_tat = sum(turnaround)/n

    return gantt, avg_wt, avg_tat