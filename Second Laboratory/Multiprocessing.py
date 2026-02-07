

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

if name == "main":
    print("=== Multiprocessing Grade Calculator ===")

    subject_count = int(input("How many subjects? "))
    grades = []

    for i in range(subject_count):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades.append(grade)