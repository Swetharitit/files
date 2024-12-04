def sum_of_elements(lst):
    return sum(lst)
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print(result)


def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total


















def square_elements(lst):
    return [x ** 2 for x in lst]
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_elements(numbers)
print(squared_numbers)

def square_elements(lst):
    return list(map(lambda x: x ** 2, lst))















def longest_string(lst):
    return max(lst, key=len)
strings = ["hello", "world", "abc", "defghi"]
longest = longest_string(strings)
print(longest)
def longest_string(lst):
    longest = ""
    for s in lst:
        if len(s) > len(longest):
            longest = s
    return longest

























def average_of_elements(lst):
    return sum(lst) / len(lst)
numbers = [1, 2, 3, 4, 5]
average = average_of_elements(numbers)
print(average)

def average_of_elements(lst):
    if len(lst) == 0:
        return 0  
    return sum(lst) / len(lst)

import statistics

def average_of_elements(lst):
    return statistics.mean(lst)















def target_in_list(lst, target):
    return target in lst
numbers = [1, 2, 3, 4, 5]
target = 3
result = target_in_list(numbers, target)
print(result)

target = 6
result = target_in_list(numbers, target)
print(result)

def target_in_list(lst, target):
    for num in lst:
        if num == target:
            return True
    return False













def remove_duplicates(lst):
    return list(set(lst))
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]















def common_elements(list1, list2):
    return list(set(list1) & set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = common_elements(list1, list2)
print(common)

def common_elements(list1, list2):
    return [x for x in list1 if x in list2]














def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

numbers = [5, 2, 8, 3, 1]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst
















def sort_strings(lst):
    return sorted(lst)
strings = ["hello", "world", "abc", "def", "ghi"]
sorted_strings = sort_strings(strings)
print(sorted_strings)

def sort_strings(lst):
    lst.sort()
    return lst
def sort_strings(lst):
    return sorted(lst, key=str.lower)


















def max_min(lst):
    return (max(lst), min(lst))
numbers = [5, 2, 8, 3, 1]
max_min_values = max_min(numbers)
print(max_min_values)

def max_min(lst):
    max_val = min_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return (max_val, min_val)
def max_min(lst):
    if not lst:
        return (None, None)  
    return (max(lst), min(lst))






