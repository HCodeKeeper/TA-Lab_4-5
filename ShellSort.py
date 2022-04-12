import math

from Sort import Sort

class ShellSort(Sort):

    def __init__(self):
        super().__init__()
        pass


    def sort(self, array):
        swaps = 0
        comparisons = 0

        gap = len(array) // 2
        while gap > 0:
            for i in range(len(array)):
                left_index = i - gap
                right_index = i
                comparisons += 1
                while left_index >= 0 and array[right_index] < array[left_index]:
                    swaps += 1
                    array[left_index], array[right_index] = array[right_index], array[left_index]
                    right_index = left_index
                    left_index = left_index - gap

            gap = gap // 2
        print("swaps", swaps)
        print("comparisons", comparisons)