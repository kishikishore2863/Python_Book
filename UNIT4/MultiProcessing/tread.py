# Code Breakdown
# 1. Imports:
# from multiprocessing import Process: Imports the class needed to create new processes.
# import os: Allows interacting with the operating system (specifically for fetching Process IDs).
# import time: Used to simulate a delay in the child process.

# 2. child_task() function:
# This is the function that will run in the child process.
# time.sleep(1): Pauses this process for 1 second.
# os.getpid(): Returns the Process ID (PID) of the current process (the child).
# os.getppid(): Returns the Parent Process ID (PPID) of the current process.

# 3. if __name__ == '__main__'::
# This is essential in Python multiprocessing to prevent the child process from creating its own child processes recursively when the script imports the main module.

# 4. Main Execution Flow:
# p = Process(target=child_task): Creates a process object, telling it to run child_task.
# p.start(): This command creates the separate process in memory and begins executing it.
# p.pid: Accesses the unique ID of the newly created child process.
# p.join(): This tells the parent process to wait at this line until the child process (p) finishes its work.
from multiprocessing import Process
'''Process is imported to create a new OS process. '''
import os
'''os is imported to read process IDs'''
import time
'''time is imported to calculate time, pause execution'''

def child_task():
    """child_task is defined.
    This function is executed inside child process only."""
    time.sleep(1)
    '''pauses the child for one second.'''
    '''delay is added so execution order is visible'''
    print("Child prints after 1 second")
    print("Child PID:", os.getpid())
    '''prints the child process ID.'''
    print("Child PPID:", os.getppid())
    '''prints the parent process ID.'''

if __name__ == '__main__':
    '''The main guard is checked
    Code inside runs only once in the parent.
    This guard is required on Windows.
    Infinite process spawning is prevented.'''

    print("Parent prints immediately")
    print("Parent PID:", os.getpid())
    '''The parent process ID is printed.
    Only one process exists at this point.'''

    p = Process(target=child_task)
    '''A Process object is created.
    child_task is registered as the child entry function.
    No new process is started yet.'''

    p.start()
    '''A new OS process is created.
    A new Python interpreter starts for the child.
    child_task begins execution in parallel.'''

    print("Parent created child PID:", p.pid)
    print("Parent will wait now")

    p.join()
    '''The parent is blocked here.
    The parent waits until the child finishes execution.'''
    print("Parent prints last because join completes.")