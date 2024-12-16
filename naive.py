import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


random.seed(40)
data = [random.randint(0, 100) for _ in range(50)]
print("Sorted Data:", bubble_sort(data))