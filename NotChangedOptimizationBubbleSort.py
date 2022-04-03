from BubbleSort import BubbleSort


class NotChangedOptimizedBubbleSort(BubbleSort):

    def __init__(self):
        super().__init__()
        pass

    def sort(self, array):
        n = len(array)
        for i in range(0, n):
            changed = False
            for j in range(1, n):
                if array[j - 1] > array[j]:
                    array[j - 1], array[j] = array[j], array[j - 1]
                    changed = True
            if not changed:
                return
