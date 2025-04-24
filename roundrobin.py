from collections import deque

def Find(tasks, time_slice):
    Q = deque()  # Queue to hold tasks (with task number)
    
    # Append tasks with their respective task number (starting from 1)
    for i in range(len(tasks)):
        Q.append((tasks[i], i + 1))
    
    time = 0  # Track the total time passed
    
    while Q:
        task, task_num = Q.popleft()  # Get the next task from the queue
        
        # Execute the task for the time slice or the remaining time, whichever is smaller
        executed = min(task, time_slice)
        time += executed
        
        # Print task execution details
        print(f"Task {task_num} ---> executed {executed} units: time {time}")
        
        # If the task is not finished, re-add it to the queue with the remaining burst time
        if task > time_slice:
            Q.append((task - executed, task_num))  # Remaining time is task - executed

# Example usage:
tasks = [10, 5, 8]  # CPU burst times (using a list, not a set)
time_slice = 4  # Time slice

Find(tasks, time_slice)