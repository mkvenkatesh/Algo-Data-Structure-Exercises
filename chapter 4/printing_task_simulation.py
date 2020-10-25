'''
Printing Task Simulation

Consider the following situation in a computer science laboratory. On any
average day about 10 students are working in the lab at any given hour. These
students typically print up to twice during that time, and the length of these
tasks ranges from 1 to 20 pages. The printer in the lab is older, capable of
processing 10 pages per minute of draft quality. The printer could be switched
to give better quality, but then it would produce only five pages per minute.
The slower printing speed could make students wait too long. What page rate
should be used?

Algo: 
Here is the main simulation.
1. Create a queue of print tasks. Each task will be given a timestamp upon its
   arrival. The queue is empty to start.
2. For each second (current_second): 
    • Does a new print task get created? If so, add it to the queue with the
    current_second as the timestamp. 
    • If the printer is not busy and if a task is waiting, 
        – Remove the next task from the print queue and assign it to the printer. 
        – Subtract the timestamp from the current_second to compute the waiting time
        for that task. 
        – Append the waiting time for that task to a list for later processing. 
        – Based on the number of pages in the print task, figure out how much time
        will be required.
   • The printer now does one second of printing if necessary. It also subtracts
   one second from the time required for that task. 
   • If the task has been completed, in other words the time required has
   reached zero, the printer is no longer busy.
3. After the simulation is complete, compute the average waiting time from the
   list of waiting times generated.

Notes: To model this situation we need to use some probabilities. For example,
students may print a paper from 1 to 20 pages in length. If each length from 1
to 20 is equally likely, the actual length for a print task can be simulated by
using a random number between 1 and 20 inclusive. This means that there is equal
chance of any length from 1 to 20 appearing.

If there are 10 students in the lab and each prints twice, then there are 20
print tasks per hour on average. What is the chance that at any given second, a
print task is going to be created? The way to answer this is to consider the
ratio of tasks to time. Twenty tasks per hour means that on average there will
be one task every 180 seconds. For every second we can simulate the chance that
a print task occurs by generating a random number between 1 and 180 inclusive.
If the number is 180, we say a task has been created.
'''

from queues import Queue
from random import randrange
import math

def generate_task(task_rate):
    task_rate = (60 * 60) // task_rate
    random_num = randrange(0, task_rate + 1)
    if random_num == task_rate:
        return True
    else:
        return False

def simulate_print_task(task_rate, max_page_length_per_task, print_rate):
    task_queue = Queue()
    printer_busy = False
    task_wait_times = []
    # Loop for an hour to calculate the average wait time of a task in the queue
    for current_second in range(1, (60 * 60) + 1):
        # simulate generating a task and adding it to the queue for printing
        if (generate_task(task_rate)):
            page_length = randrange(1, max_page_length_per_task + 1)
            # calculate how long in second the task would take to print
            task_print_time = (60 / print_rate) * page_length
            # add the task to the queue for printing
            task_queue.enqueue({"current_second": current_second, "print_time": task_print_time})

        # if the printer is not busy and there's a task in the queue, take it up
        if (not printer_busy) and (not task_queue.is_empty()):
            # take up a print task from the queue
            print_task = task_queue.dequeue()
            # when you take up the task, make the printer busy
            printer_busy = True
            
            # calculate the time the task waited in the queue by subtracting the
            # task's current_second with the loop's current_second
            # print(current_second, print_task["current_second"], print_task["print_time"], task_queue.size())
            task_wait_times.append(current_second - print_task["current_second"])


        if (printer_busy):                
            # if the print task time is going to be less than 1 second, the printer can be freed up
            if print_task["print_time"] <= 1:
                printer_busy = False
            else:
                # reduce the print time for the task so the printer can be freed
                # up if necessary on the next iteration
                print_task["print_time"] -= 1

    return sum(task_wait_times) / len(task_wait_times)

if __name__ == "__main__":
    # 20 tasks can be generated in an hour (10 students * 2)
    task_rate = 20
    # max pages that a student is allowed to print per task
    max_page_length_per_task = 20
    # Pages per minute. Change this to figure out the optimum page printing rate to reduce wait times.
    print_rate = 10
    # number of hours. check task wait time for every hour in a day
    num_simulations = 24

    for i in range(num_simulations):
        print("\nHour:", i + 1)
        print("Average task wait time in seconds: ", "{:.2f}".format(simulate_print_task(task_rate, max_page_length_per_task, print_rate)))