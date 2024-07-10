# Sorting Algorithms

## Bubble Sort:
    
Bubble sort compares adjecent elements and swaps them if they are in the wrong order. The algorithm repeadly passes through the list until no more swaps are needed. indicating that the list is sorted.
    
#### Time Complexity:
- Best case - O(n) when the list is already sorted
- Worst case - O(n<sup>2</sup>) 
- Average case - O(n^2)
#### Space Complexity:
- O(1) - Inplace sort (Since we swap elements within the array, we don't need any space)

## Selection Sort:
    
Selection sort is another comparison-based algorithm. It divides the input list into two parts: a sorted and an unsorted sublist. It repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the end of the sorted sublist.

#### Time Complexity:
- Best case - O(n<sup>2</sup>) 
- Worst case - O(n<sup>2</sup>) 
- Average case - O(n<sup>2</sup>) 
#### Space Complexity:
- O(1) - Inplace sort (Since we swap elements within the array, we don't need any space)

## Insertion Sort:
    
Insertion sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advances algorithms such as quicksort, heapsort, or merge sort.

#### Time Complexity:
- Best case - O(n) 
- Worst case - O(n<sup>2</sup>) 
- Average case - O(n<sup>2</sup>) 
#### Space Complexity:
- O(1) - Inplace sort (Since we swap elements within the array, we don't need any space)

## Merge Sort:
 
Merge sort is one of the efficient sorting algorithm. It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down a list into several sublists until each sublist consistes of a single element and merges those sublists in a manner that results in a sorted list.

#### Time Complexity:
- Best case - O(nlogn) 
- Worst case - O(nlogn) 
- Average case - O(nlogn) 
#### Space Complexity:
- O(n)

## Quick Sort:
 
Quick sort is an efficient ,comparison-based, divide and conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning other elements into two sub-arrays according to whether they are less than or greater than the pivot.
Pivot element can be selected randomly or a median of the array. It is not a stable sort like merge sort. 
#### Time Complexity:
- Best case - O(nlogn) 
- Worst case - O(n<sup>2</sup>) 
- Average case - O(nlogn) 
#### Space Complexity:
- O(1) - Inplace sort

    
## HeapSort:
 
Heapsort is a comparison-based sorting technique based on a Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining element.
- Best case - O(nlogn) 
- Worst case - O(nlogn) 
- Average case - O(nlogn) 
#### Space Complexity:
- O(1) - Inplace sort


