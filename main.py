import streamlit as st
from fcfs import fcfs
import plotly.graph_objects as go
from sjf_non_preemptive import sjf_non_preemptive
from sjf_preemptive import sjf_preemptive
from round_robin import round_robin
from priority import priority_scheduling

st.title("CPU Scheduling Simulator")

st.header("Enter Process Details")

num_process = st.number_input("Number of Processes", min_value=1, step=1, value=1)

processes = []

for i in range(num_process):
    st.subheader(f"process p{i+1}")

    arrival = st.number_input(f"Arrival Time P{i+1}", key=f"a{i}", min_value=0, step=1, value=0)
    burst = st.number_input(f"Burst Time P{i+1}", key=f"b{i}", min_value=1, step=1, value=1)
    priority = st.number_input(f"Priority P{i+1}", key=f"p{i}", min_value=1, step=1, value=1)

    processes.append({
        "pid" : f"P{i+1}",
        "arrival" : int(arrival),
        "burst" : int(burst),
        "priority": int(priority)
    })

algorithm = st.selectbox(
    "Select Scheduling Algorithm",
    ["FCFS", "SJF Non Preemptive", "SJF Preemptive", "Round Robin", "Priority"] 
)

time_quantum = None

if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1)

if st.button("Run Scheduling"):
    st.write("Processes:", processes)
    st.write("Selected Algorithm:", algorithm)

    if algorithm == "FCFS":
        gantt, avg_wt, avg_tat = fcfs(processes)

    elif algorithm == "SJF Non Preemptive":
        gantt, avg_wt, avg_tat = sjf_non_preemptive(processes)

    elif algorithm == "SJF Preemptive":
        gantt, avg_wt, avg_tat = sjf_preemptive(processes)

    elif algorithm == "Round Robin":
        gantt, avg_wt, avg_tat = round_robin(processes, time_quantum)

    elif algorithm == "Priority":
        gantt, avg_wt, avg_tat = priority_scheduling(processes)

    st.subheader("Gantt Chart Data")
    st.write(gantt)

    st.subheader("Performance")
    st.write(f"Average Waiting Time : {avg_wt:.2f}")
    st.write(f"Average Turnaround Time : {avg_tat:.2f}")

    fig = go.Figure()

    for p in gantt:
        process = p[0]
        start = p[1]
        finish = p[2]
        duration = finish - start

        fig.add_bar(
            x=[duration],
            y=[process],
            base=start,
            orientation="h",
            name=process
        )

    fig.update_layout(
        title="CPU Scheduling Gantt Chart",
        xaxis_title="Time",
        yaxis_title="Process",
        barmode="stack"
    )

    st.plotly_chart(fig)

       