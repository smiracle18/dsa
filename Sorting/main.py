from Strategies.bubble_sort import BubbleSort
from Strategies.insertion_sort import InsertionSort

from sorting import Sorting


if __name__ == "__main__":

    # Create an array of integers.
    arr = [1, 9, 13, 4, 5, 6, 3, 7, 8, 2, 9, 10]

    sorting = Sorting(BubbleSort())
    print(sorting.sort(arr))
    print(arr)
    sorting = Sorting(strategy=InsertionSort())
    print(sorting.sort(arr))

    sorting.set_strategy = BubbleSort()
    print(sorting.sort(arr))

