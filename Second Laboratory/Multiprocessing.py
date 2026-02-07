

#Member 1 : Charmaine J. Opiso

#Imports
#Process function
#User input handling

from multiprocessing import Process, Queue
import time
import os

def process_subject(grade, subject_number, result_queue):
    time.sleep(0.5)
    gwa = grade
    result_queue.put((subject_number, gwa, os.getpid()))

if __name__ == "__main__":
    print("=== Multiprocessing Grade Calculator ===")

    subject_count = int(input("How many subjects? "))
    grades = []

    for i in range(subject_count):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades.append(grade)

#Member 2 : Christian S. Dagcuta

# Process creation & execution
# Result collection
# GWA computation & timing
    processes = []
    result_queue = Queue()

    start_time = time.time()

    for i, grade in enumerate(grades):
        p = Process(
            target=process_subject,
            args=(grade, i + 1, result_queue)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\nResults from each process:")
    results = []

    while not result_queue.empty():
        results.append(result_queue.get())

    results.sort()

    for subject_number, gwa, pid in results:
        print(f"Process {pid} finished Subject {subject_number} GWA: {gwa}")

    overall_gwa = sum(grades) / len(grades)
    end_time = time.time()

    print(f"\nOverall GWA: {overall_gwa:.2f}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")