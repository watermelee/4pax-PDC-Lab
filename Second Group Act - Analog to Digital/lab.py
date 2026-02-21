import time
import os
from concurrent.futures import ProcessPoolExecutor

def grade(submission):
    time.sleep(0.1)  # simulate grading time
    return submission * 2

def run_sequential(students):
    start = time.time()

    for s in students:
        grade(s)

    end = time.time()
    return end - start

def run_parallel(students):
    start = time.time()

    with ProcessPoolExecutor() as executor:
        list(executor.map(grade, students))

    end = time.time()
    return end - start

def main():
    students = list(range(200))

    # Execute sequential
    sequential_time = run_sequential(students)

    # Execute parallel
    parallel_time = run_parallel(students)

    # Compute speedup
    speedup = sequential_time / parallel_time if parallel_time > 0 else float("inf")

    # Output required results
    print("=== Programming Assignments Grading Benchmark ===")
    print(f"Students graded: {len(students)}")
    print(f"Sequential Time: {sequential_time:.4f} seconds")
    print(f"Parallel Time:   {parallel_time:.4f} seconds")
    print(f"Speedup:         {speedup:.2f}x")

    # Scaling explanation
    cpu_cores = os.cpu_count()
    print("\n=== Scaling Explanation ===")
    print(f"Available CPU cores: {cpu_cores}")
    print("Ideal linear scaling would approach the number of cores.")

    if speedup >= cpu_cores * 0.8:
        print("Result approaches ideal linear scaling.")
    else:
        print("Speedup is lower than ideal due to:")
        print("- Process creation overhead")
        print("- Scheduling cost")
        print("- Shared CPU limits (Codespaces)")
        print("- Some parts remain sequential")


if __name__ == "__main__":
    main()