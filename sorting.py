#Sifa Sahira
#F55123059
#Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0 
        j = 0  
        k = 0  

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#Quick Sort
def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]  
        i = low - 1  

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

data = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("Data Array:", data)
merge_sort(data)
print("Merge Sort:", data)
quick_sort(data)
print("Quick Sort:", data)

# 1. Merge Sort
# Best Case: Terjadi jika data sudah terurut sebelumnya. Namun, Merge Sort tetap harus membagi dan menggabungkan elemen, sehingga kompleksitasnya tetap O(n log n).
# Worst Case: Terjadi jika data tidak terurut sama sekali. Namun, karena Merge Sort tidak bergantung pada urutan data (proses pembagian dan penggabungannya sama), kompleksitasnya tetap O(n log n).
# Average Case: Terjadi untuk data acak atau data dengan elemen berulang. Karena proses Merge Sort tidak terpengaruh oleh pola urutan data, semua kasusnya memiliki kompleksitas waktu yang sama (O(n log n)).
#Dalam program ini, Average Case adalah representasi hasil, meskipun kompleksitasnya tetap konsisten untuk semua kasus.

# 2. Quick Sort
# Best Case: Terjadi jika pivot selalu membagi array menjadi dua bagian yang hampir sama besar. Kompleksitas: O(n log n).
# Worst Case: Terjadi jika pivot selalu elemen terkecil atau terbesar. Misalnya, input terurut menurun akan menyebabkan partisi sangat tidak seimbang. Kompleksitas: O(n^2).
# Average Case: Terjadi jika data memiliki pola acak atau elemen berulang. Dengan pemilihan pivot terakhir, partisi cenderung cukup seimbang sehingga performa mendekati O(n log n).
# Program berada dalam Average Case karena input data cukup acak dan menghasilkan pembagian partisi yang seimbang.
