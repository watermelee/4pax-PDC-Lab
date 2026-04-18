
# Invididual Reflections

watermelee - Carmeli Gadrinab

Parallel sorting was faster but parallel searching was slower. For sorting on bigger datasets, splitting the work across multiple processes actually paid off because the sorting itself took a lot of computation. But for searching, the parallel version just added extra overhead that wasn't worth it since the search itself is pretty fast. So parallelism only wins if the actual work is heavy enough to justify all the extra complexity of managing multiple processes.

galathiea - Threcia Mae Cabuguason

The implementation demonstrates how sequential search and parallel search method both operate based their distinct conceptual frameworks. The sequential search operates through an easy system which checks each item one by one until it locates the required item yet this method works best for small data sets. The parallel search method divides its data into separate parts which it assigns to various processes while using multiple processors to search different parts of the data at the same time. The parallel method needs more effort to execute because it requires making new processes while establishing queue systems and synchronizing results yet this method provides better scalability for handling large data sets. The system performance depends on two factors which are proper chunk division and available system resources because multiple processes introduce additional overhead costs. The comparison between the two systems demonstrates how algorithm designers need to choose between creating simple systems and building systems that need more work to achieve better performance.

synochan - Christian Dagcuta

In the benchmark runner, I tested and compared the performance of both sequential and parallel algorithms for sorting and searching by measuring their execution times on the same dataset. I made sure each method was fairly evaluated by using copies of the data and verifying their correctness using built-in checks. Through this, I observed how parallel approaches can sometimes perform faster, especially on larger datasets, but they can also be affected by overhead, which means sequential methods can still be more efficient in some cases. This part helped me better understand the real-world trade-offs between performance and accuracy when working with different algorithm implementations.


kccharms - Charmaine Opiso

I applied parallel processing to improve sorting performance by dividing the dataset into smaller chunks and sorting them simultaneously using multiple processes, where each process uses merge sort on its assigned data. After all chunks are sorted, they are merged into a single final output. Through this, I realized that while parallel sorting can be faster for large datasets, it also introduces overhead such as process management and merging, which means it is not always more efficient than the sequential approach, but it gave me a better understanding of how parallel algorithms work in practice.
