def list():
    numbers = (1,2,3,4,5)
    
    bob = len(numbers)
    
    
    print(bob)

list()

print(f"This is Binary Search")

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary_search([1,2,3,4,5], 3))

print(f"********************************")

print(f"This is Linear Search")
import random

def linear_search(values, target):
    for item in range(len(values)):
        if values[item] == target:
            return item
    return -1

def get_values():
    values = random.sample(range(-10, 10),5)
    print(f"The list is {values}")
    target = int(input("Enter value to search "))
    result = linear_search(values, target)
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print(f"Value enterd is not present")

get_values()



