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
