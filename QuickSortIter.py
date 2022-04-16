import random
from collections import deque
import time
from Sort import Sort


class QuickSortIter(Sort):
    def __init__(self):
        super().__init__()
        self.__compares = 0
        self.__swaps = 0

    def __partition(self, array, left, right):
        pivotIndex = random.randint(left, right)
        array[right], array[pivotIndex] = array[pivotIndex], array[right]
        self.__swaps += 1
        pivotIndex = right
        pivot = array[right]
        i = left - 1
        for j in range(left, right):
            self.__compares+=1
            if array[j] < pivot:
                self.__swaps+=1
                i += 1
                array[j], array[i] = array[i], array[j]
        self.__swaps+=1
        array[i + 1], array[pivotIndex] = array[pivotIndex], array[i + 1]
        return i + 1

    def __quickSortIter(self, array):
        stack = deque()
        stack.append((0, len(array) - 1))
        while len(stack) != 0:
            left, right = stack.pop()
            pivot = self.__partition(array, left, right)
            if pivot - 1 > left:
                stack.append((left, pivot - 1))
            if pivot + 1 < right:
                stack.append((pivot + 1, right))

    def sort(self, array):
        self.__quickSortIter(array)
        print("Compares " + str(self.__compares))
        print("Swaps " + str(self.__swaps))
        self.__compares = 0
        self.__swaps = 0
        return
