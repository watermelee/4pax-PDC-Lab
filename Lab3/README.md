# Applying Task and Data Parallelism using concurrent.futures

## 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
Task vs. Data Parallelism: In Part A, where SSS, PhilHealth, Pag-IBIG, and tax deductions are computed concurrently for a single employee using ThreadPoolExecutor, task parallelism divides work by type of deduction. As demonstrated in Part B, where ProcessPoolExecutor is used to apply the payroll function to multiple employees, data parallelism divides work by employee and performs the same task on multiple data elements.

## 2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.
 concurrent.futures execution: map() applies a function to several inputs and returns results in order, whereas submit() schedules a single task and returns a Future object for retrieving results later. Results and completion tracking are made possible by future objects. When tasks are finished, using with guarantees that executors are initialized and terminate automatically.

## 3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did
ThreadPoolExecutor and GIL: In Part A, threads provide concurrency but true parallelism does not occur for CPU-bound tasks because the GIL allows only one thread to execute Python bytecode at a time.

## 4. Explain why ProcessPoolExecutor enables true parallelism, including memory
ProcessPoolExecutor and true parallelism: In Part B, CPU-bound payroll computations for multiple employees can run truly in parallel across cores because each process has its own interpreter and memory space, avoiding the GIL.

## 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
Scalability: While ThreadPoolExecutor is constrained by the GIL for CPU-bound tasks, ProcessPoolExecutor scales better for 10,000 employees since each employee's payroll is calculated in a distinct process that utilizes multiple CPU cores.

## 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
Real-world payroll example: Task parallelism uses threads to calculate multiple deductions for a single employee in a payroll system, while data parallelism uses processes to compute payroll for all employees at once. Processes effectively manage CPU-bound large-scale computations, while threads are best suited for I/O-bound or lightweight tasks.