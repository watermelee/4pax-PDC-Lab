import random
import time
import sys
import multiprocessing


# ─────────────────────────────────────────
#  DATASET GENERATION
# ─────────────────────────────────────────

def generate_random(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

def generate_sorted(n):
    return sorted(generate_random(n))

def generate_reverse_sorted(n):
    return sorted(generate_random(n), reverse=True)


# ─────────────────────────────────────────
#  SEQUENTIAL SORT  (Merge Sort)
# ─────────────────────────────────────────

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sequential_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left  = sequential_sort(data[:mid])
    right = sequential_sort(data[mid:])
    return merge(left, right)