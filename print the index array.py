def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the target is at the mid position
        if arr[mid] == target:
            return mid
        
        # If target is smaller than mid, ignore the right half
        elif arr[mid] > target:
            high = mid - 1
        
        # If target is larger than mid, ignore the left half
        else:
            low = mid + 1
    
    return -1  # Target not found

# Main program to test binary search
def main():
    # Example input arrays
    arr1 = [2, 3, 5, 7, 9]
    target1 = 7
    
    arr2 = [1, 4, 5, 8, 9]
    target2 = 7

    # Test binary search with arr1 and target1
    index1 = binary_search(arr1, target1)
    if index1 != -1:
        print(f"Element found at Index {index1}")
    else:
        print("Element Not Found")

    # Test binary search with arr2 and target2
    index2 = binary_search(arr2, target2)
    if index2 != -1:
        print(f"Element found at Index {index2}")
    else:
        print("Element Not Found")

# Run the program
if __name__ == "__main__":
    main()
