import random
from collections import deque

from Sort import Sort


class QuickSort(Sort):
    def __init__(self):
        super().__init__()
        self.__compares = 0
        self.__swaps = 0

    def __quick(self, array, l, h):
        pivot = l
        o = array[pivot]
        i = l
        j = h
        while i <= j:
            while array[i] < o:
                self.__compares += 1
                i += 1
            while array[j] > o:
                self.__compares += 1
                j -= 1
            if i <= j:
                self.__swaps += 1
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        if h > i:
            self.__quick(array, i, h)
        if l < j:
            self.__quick(array, l, j)

    def sort(self, array):
        self.__quick(array, 0, len(array)-1)
        print("Compares " + str(self.__compares))
        print("Swaps " + str(self.__swaps))
        self.__compares = 0
        self.__swaps = 0
        return
