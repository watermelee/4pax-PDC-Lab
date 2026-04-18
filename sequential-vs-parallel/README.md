
# Invididual Reflections

watermelee - Carmeli Gadrinab

Parallel sorting was faster but parallel searching was slower. For sorting on bigger datasets, splitting the work across multiple processes actually paid off because the sorting itself took a lot of computation. But for searching, the parallel version just added extra overhead that wasn't worth it since the search itself is pretty fast. So parallelism only wins if the actual work is heavy enough to justify all the extra complexity of managing multiple processes.


