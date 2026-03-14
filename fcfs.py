def fcfs(processes):
    processes.sort(key=lambda x: x["arrival"])
    
    time = 0
    gantt = []
    waiting = []
    turnaround = []

    for p in processes:
        if time < p["arrival"]:
            time = p["arrival"]

        start = time
        finish = start + p["burst"]

        gantt.append((p["pid"], start, finish))
        
        wt = start - p["arrival"]
        tat = finish - p["arrival"]

        waiting.append(wt)
        turnaround.append(tat)

        time = finish

    avg_wt = sum(waiting)/len(waiting)
    avg_tat = sum(turnaround)/len(turnaround)

    return gantt, avg_wt, avg_tat
