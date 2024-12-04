import random
import time

# Method to generate 100,000 random floating-point numbers between 1.0 and 100.0
def generate_random_numbers(size=100000):
    return [random.uniform(1.0, 100.0) for _ in range(size)]

# Method to perform Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Method to perform Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Method to calculate the time taken by each sorting algorithm
def measure_time(sort_function, arr):
    start_time = time.time()  # Record the start time
    sort_function(arr)        # Run the sorting algorithm
    end_time = time.time()    # Record the end time
    return (end_time - start_time) * 1000  # Convert to milliseconds

# Main program to compare the performance of Selection Sort and Quick Sort
def main():
    # Generate random numbers
    arr = generate_random_numbers()
    
    # Copy the array for fair comparison
    arr_selection = arr.copy()
    arr_quick = arr.copy()

    # Measure time for Selection Sort
    time_selection_sort = measure_time(selection_sort, arr_selection)
    print(f"Selection Sort Time: {time_selection_sort:.2f} ms")

    # Measure time for Quick Sort
    time_quick_sort = measure_time(quick_sort, arr_quick)
    print(f"Quick Sort Time: {time_quick_sort:.2f} ms")

    # Calculate the percentage difference in speed
    if time_quick_sort < time_selection_sort:
        percentage_difference = ((time_selection_sort - time_quick_sort) / time_selection_sort) * 100
        print(f"Quick Sort is faster by {percentage_difference:.2f}%.")
    else:
        percentage_difference = ((time_quick_sort - time_selection_sort) / time_quick_sort) * 100
        print(f"Selection Sort is faster by {percentage_difference:.2f}%.")

# Run the program
if __name__ == "__main__":
    main()
