
# Second Laboratory – Multithreading and Multiprocessing in Python

## Execution Time Comparison

| Method | Execution Order | GWA Output | Execution Time |
|-------|----------------|------------|----------------|
| Multithreading | Non-sequential (may appear ordered) | 86.25 | ~0.50079 seconds |
| Multiprocessing | Non-sequential | 86.25 | ~0.5054 seconds |

> Note: Execution time may vary depending on system performance and number of inputs.

---

## Questions and Answers

### 1. Which approach demonstrates true parallelism in Python? Explain.
Multiprocessing demonstrates true parallelism because each process runs independently and can execute on different CPU cores at the same time.

---

### 2. Compare execution times between multithreading and multiprocessing.
For small workloads, multithreading and multiprocessing show similar execution times. Multithreading has lower overhead, while multiprocessing becomes more efficient for heavier computations.

---

### 3. Can Python handle true parallelism using threads? Why or why not?
Python cannot achieve true parallelism using threads for CPU-bound tasks because of the Global Interpreter Lock (GIL), which allows only one thread to execute Python code at a time.

---

### 4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?
With a large number of grades, both approaches experience overhead. Multiprocessing is generally faster for CPU-bound tasks because it can utilize multiple CPU cores, while multithreading is limited by the GIL.

---

### 5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?
- CPU-bound tasks: Multiprocessing  
- I/O-bound tasks: Multithreading  

---

### 6. How did your group apply creative coding or algorithmic solutions in this lab?
Our group replaced hardcoded inputs with user input, added labels to threads and processes for clearer output, measured execution time using the time module, and computed the overall GWA after concurrent execution.
