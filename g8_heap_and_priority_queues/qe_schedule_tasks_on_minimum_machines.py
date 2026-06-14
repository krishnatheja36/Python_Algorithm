"""
Schedule Tasks on Minimum Machines — Heap / Priority Queue

Logic:
    Sort tasks by start time. Use a min-heap keyed by end time to track machines
    in use. For each new task, pop all machines whose last task ended before this
    task starts (freeing them). Then push the new task's end time. The heap size
    at any point is the number of machines concurrently needed; the maximum is
    the answer.

Time:  O(n log n) — sorting plus n heap operations
Space: O(n) — heap can hold all n tasks in the worst case
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Schedule Tasks on Minimum Machines
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Statement
# We are given an input array, tasks, where tasks[i] =[starti,endi]=[starti,endi] represents the start and end times of nn tasks. Our goal is to schedule these tasks on machines given the following criteria:
# 1.	A machine can execute only one task at a time.
# 2.	A machine can begin executing a new task immediately after completing the previous one.
# 3.	An unlimited number of machines are available.
# Find the minimum number of machines required to complete these nn tasks.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Constraints:
# •	n==n== tasks.length
# •	1≤1≤ tasks.length ≤103≤103
# •	0≤0≤ tasksi.start << tasksi.end ≤104≤104
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import heapq

def minimum_machines(tasks):
    tasks.sort()
    machines = []

    for begin, end in tasks:
        
        while machines and machines[0] < begin:
            heapq.heappop(machines)

        heapq.heappush(machines, end)

    return len(machines)

# Driver code
def main():
    input_tasks_list = [
        [[1, 1], [5, 5], [8, 8], [4, 4], [6, 6], [10, 10], [7, 7]],
        [[1, 7], [1, 7], [1, 7], [1, 7], [1, 7], [1, 7]],
        [[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]],
        [[1, 3], [3, 5], [5, 9], [9, 12], [12, 13], [13, 16], [16, 17]],
        [[12, 13], [13, 15], [17, 20], [13, 14], [19, 21], [18, 20]]
    ]

    for i, tasks_list in enumerate(input_tasks_list, 1):
        print(f"{i}.\t Tasks: [", end="")
        for j, task in enumerate(tasks_list):
            print(f"[{task[0]}, {task[1]}]", end="")
            if j < len(tasks_list) - 1:
                print(", ", end="")
        print("]")
        print(f"\t Minimum number of machines: {minimum_machines(tasks_list)}")
        print("-" * 100)


if __name__ == "__main__":
    main()