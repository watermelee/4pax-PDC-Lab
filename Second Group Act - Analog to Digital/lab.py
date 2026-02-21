import time
import os
from concurrent.futures import ProcessPoolExecutor

def grade(submission):
    time.sleep(0.1)  # simulate grading time
    return submission * 2

