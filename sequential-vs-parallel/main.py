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








# ─────────────────────────────────────────
#  BENCHMARK RUNNER
# ─────────────────────────────────────────

def run_benchmark(label, data):
   print(f"\n  Dataset: {label}")
   print("-" * 60)

   # --- sorting ---
   start = time.time()
   seq_sorted = sequential_sort(data[:])
   seq_sort_time = time.time() - start

   start = time.time()
   par_sorted = parallel_sort(data[:])
   par_sort_time = time.time() - start

   assert seq_sorted == sorted(data), "Sequential sort is incorrect!"
   assert par_sorted == sorted(data), "Parallel sort is incorrect!"

   print(f"  Sort  | Sequential: {seq_sort_time:.4f}s   Parallel: {par_sort_time:.4f}s", end="   ")
   print("(parallel faster)" if par_sort_time < seq_sort_time else "(sequential faster)")

   # --- searching ---
   target = data[len(data) // 2]

   start = time.time()
   seq_idx = sequential_search(data, target)
   seq_search_time = time.time() - start

   start = time.time()
   par_idx = parallel_search(data, target)
   par_search_time = time.time() - start

   assert data[seq_idx] == target, "Sequential search is incorrect!"
   assert data[par_idx] == target, "Parallel search is incorrect!"

   print(f"  Search| Sequential: {seq_search_time:.6f}s   Parallel: {par_search_time:.6f}s", end="   ")
   print("(parallel faster)" if par_search_time < seq_search_time else "(sequential faster)")


def main():
   sizes = {
       "small":   ("Small (1,000)",      generate_random(1_000)),
       "medium":  ("Medium (100,000)",    generate_random(100_000)),
       "large":   ("Large (1,000,000)",   generate_random(1_000_000)),
       "sorted":  ("Sorted (100,000)",    generate_sorted(100_000)),
       "reverse": ("Reverse (100,000)",   generate_reverse_sorted(100_000)),
   }

   valid = ", ".join(sizes.keys())

   if len(sys.argv) < 2:
       print(f"Usage: python main.py <dataset>")
       print(f"Choose from: {valid}")
       sys.exit(1)

   key = sys.argv[1].lower()
   if key not in sizes:
       print(f"Unknown dataset '{key}'. Choose from: {valid}")
       sys.exit(1)

   label, data = sizes[key]

   print("=" * 60)
   print("  SEQUENTIAL vs PARALLEL ALGORITHM BENCHMARK")
   print("=" * 60)

   run_benchmark(label, data)

   print("\n" + "=" * 60)
   print("  Done. All correctness checks passed.")
   print("=" * 60)


if __name__ == "__main__":
   multiprocessing.freeze_support()
   main()