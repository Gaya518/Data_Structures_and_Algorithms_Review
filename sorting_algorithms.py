"""
Sorting Algorithms review for my future interviews
Author: Gaya Kanagraj
Date: 07/09/2024
"""
import heapq


class SortingAlgorithms:
    def bubble_sort(self, array: list) -> list:
        """
        Bubble sort algorithm, iterates through the array and returns the sorted array.
        :param array: list to sort.
        :return: sorted array.
        """
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def selection_sort(self, array: list) -> list:
        """
        Selection sort algorithm, iterates through the array and returns the sorted array.
        :param array: list to sort.
        :return: sorted array.
        """
        n = len(array)
        for i in range(n):
            min_ind = i
            for j in range(i+1, n):
                if array[j] < array[min_ind]:
                    min_ind = j
            array[i], array[min_ind] = array[min_ind], array[i]
        return array

    def insertion_sort(self, array: list) -> list:
        """
        Insertion sort algorithm, iterates through the array and returns the sorted array.
        :param array: list to sort.
        :return: sorted array.
        """
        for i in range(len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[ j+ 1] = key
        return array

    def merge_sort(self, arr: list) -> list:
        """
        Merge sort algorithm, iterates through the array and returns the sorted array.
        :param arr: list to sort.
        :return: sorted array.
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)
            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def partition(self,arr: list, low: int, high: int) -> list:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    def quick_sort(self, arr: list, low: int, high: int) -> list:
        """
        Quick sort algorithm, iterates through the array and returns the sorted array.
        :param arr: List to sort.
        :param low: smallest element.
        :param high: largest element.
        :return:    sorted array.
        """
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)
        return arr

    def heapify(self, arr: list, n: int, i: int):
        """
        To heaapify subtree rooted at index i.
        :param arr: List to sort.
        :param n:   size of the heap
        :param i:   index of the subtree rooted at index i

        """
        largest = i
        l = 2* i + 1
        r = 2 * i + 2
        if l < n and arr[largest] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr: list) -> list:
        """
        Heap sort algorithm, iterates through the array and returns the sorted array.
        :param arr: list to sort.
        :return: sorted array.
        """
        n = len(arr)
        for i in range(n//2, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr

    # Function to perform the sorting using
    # heaop sort
    def heap_sort_python(selt,arr):
        heapq.heapify(arr)
        result = []
        while arr:
            result.append(heapq.heappop(arr))
        return result

if __name__ == '__main__':
    sort_algorithm = SortingAlgorithms()
    array =[3,10,5,2,1]
    # print(sort_algorithm.bubble_sort(array))
    # print(sort_algorithm.selection_sort(array))
    # print(sort_algorithm.insertion_sort(array))
    # print(sort_algorithm.merge_sort(array))
    # print(sort_algorithm.quick_sort(array, 0, len(array)-1))
    print(sort_algorithm.heap_sort_python(array))

