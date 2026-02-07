import threading
import time

# Member 1: Defined the function to compute and display GWA
def compute_gwa(grades, thread_no):
   time.sleep(0.5)
   gwa = sum(grades) / len(grades)
   print(f"[Thread {thread_no}] Calculated GWA: {gwa}")

grades_list = []
n = int(input("Enter number of subjects: "))

for i in range(n):
   grade = float(input(f"Enter grade for subject {i+1}: "))
   grades_list.append(grade)

# Member 1: Calculated the overall GWA after threads finished
overall_gwa = sum(grades_list) / len(grades_list)
print("Overall GWA:", overall_gwa)