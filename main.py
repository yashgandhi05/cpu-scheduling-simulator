import streamlit as st
from fcfs import fcfs

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
    ["FCFS", "SJF", "Round Robin", "Priority"] 
)

time_quantum = None

if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1)

if st.button("Run Scheduling"):
    st.write("Processes:", processes)
    st.write("Selected Algorithm:", algorithm)

    if algorithm == "FCFS":
        gantt, avg_wt, avg_tat = fcfs(processes)

        st.subheader("Gantt Chart Data")
        st.write(gantt)

        st.subheader("Performance")
        st.write("Average Waiting Time:", avg_wt)
        st.write("Average Turnaround Time:", avg_tat)