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

# Member 2: Started execution time measurement
start_time = time.time()


threads = []


# Member 2: Created and started threads dynamically
for i, grade in enumerate(grades_list):
   t = threading.Thread(
       target=compute_gwa,
       args=([grade], i + 1)
   )
   threads.append(t)
   t.start()


# Member 2: Ensured all threads complete before proceeding
for t in threads:
   t.join()


# Member 1: Calculated the overall GWA after threads finished
overall_gwa = sum(grades_list) / len(grades_list)


# Member 2: Stopped execution time measurement
end_time = time.time()


print("Overall GWA:", overall_gwa)
print("Multithreading Execution Time:", end_time - start_time)
