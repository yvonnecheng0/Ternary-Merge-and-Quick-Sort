""""
Module will show runtimes of functions of sorts.py
Yvonne Cheng 
csci 112
Winter, 2023
"""
from sorts import *
import random
import time
import copy

#Generate list of 2,000 random numbers
random_list = [random.randint(0, 100) for i in range(2000)]

# Measure the execution time of mergeSortBinary
start_time = time.time()
mergeSortBinary(copy.copy(random_list))
end_time = time.time()
mergeSortBinary_time = end_time - start_time

# Measure the execution time of mergeSortTertiary
start_time = time.time()
mergeSortTernary(copy.copy(random_list))
end_time = time.time()
mergeSortTernary_time = end_time - start_time

# Measure the execution time of quickSortBinary
start_time = time.time()
quickSortBinary(copy.copy(random_list))
end_time = time.time()
quickSortBinary_time = end_time - start_time

# Measure the execution time of quickSortTertiary
start_time = time.time()
quickSortTernary(copy.copy(random_list))
end_time = time.time()
quickSortTertiary_time = end_time - start_time

if __name__ == "__main__":
# Print the execution times
    print("mergeSortBinary: ", mergeSortBinary_time)
    print("mergeSortTernary: ", mergeSortTernary_time)
    print("mergeSortBinary is slower than mergeSortTertiary:", mergeSortBinary_time > mergeSortTernary_time)
    print("quickSortBinary: ", quickSortBinary_time)
    print("quickSortTertiary: ", quickSortTertiary_time)
    print("quickSortBinary is slower than quickSortTertiary:", quickSortBinary_time > quickSortTertiary_time)


