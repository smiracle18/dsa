from sorting import Sorting
from Strategies.bubble_sort import BubbleSort
from Strategies.insertion_sort import InsertionSort
from Strategies.selection_sort import SelectionSort
from Strategies.merge_sort import MergeSort
from Strategies.quick_sort import Quicksort
from Strategies.heap_sort import HeapSort

if __name__ == "__main__":

    # Create an array of integers.
    arr = [1, 9, 14, 13, 4, 5, 6, 3, 7, 8, 2, 9, 10]

    sorting = Sorting(BubbleSort())
    print(sorting.sort(arr))
    print('arr',arr)
    sorting = Sorting(strategy=InsertionSort())
    print(sorting.sort(arr))
    print('arr',arr)
    sorting.set_strategy = SelectionSort()
    print(sorting.sort(arr))
    print('arr',arr)
    sorting.set_strategy = MergeSort()
    print(sorting.sort(arr))
    print('arr',arr)

    sorting.set_strategy = Quicksort()
    print(sorting.sort(arr))
    print('arr',arr)

    sorting.set_strategy = HeapSort()
    print(sorting.sort(arr))
    print('arr',arr)
