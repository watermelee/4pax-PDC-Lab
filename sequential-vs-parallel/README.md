
# Invididual Reflections

watermelee - Carmeli Gadrinab

Parallel sorting was faster but parallel searching was slower. For sorting on bigger datasets, splitting the work across multiple processes actually paid off because the sorting itself took a lot of computation. But for searching, the parallel version just added extra overhead that wasn't worth it since the search itself is pretty fast. So parallelism only wins if the actual work is heavy enough to justify all the extra complexity of managing multiple processes.


synochan - Christian Dagcuta

In the benchmark runner, I tested and compared the performance of both sequential and parallel algorithms for sorting and searching by measuring their execution times on the same dataset. I made sure each method was fairly evaluated by using copies of the data and verifying their correctness using built-in checks. Through this, I observed how parallel approaches can sometimes perform faster, especially on larger datasets, but they can also be affected by overhead, which means sequential methods can still be more efficient in some cases. This part helped me better understand the real-world trade-offs between performance and accuracy when working with different algorithm implementations.


kccharms - Charmaine Opiso

I applied parallel processing to improve sorting performance by dividing the dataset into smaller chunks and sorting them simultaneously using multiple processes, where each process uses merge sort on its assigned data. After all chunks are sorted, they are merged into a single final output. Through this, I realized that while parallel sorting can be faster for large datasets, it also introduces overhead such as process management and merging, which means it is not always more efficient than the sequential approach, but it gave me a better understanding of how parallel algorithms work in practice.
