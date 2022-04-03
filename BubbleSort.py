from Sort import Sort


class BubbleSort(Sort):

    def __init__(self):
        super().__init__()
        pass

    def sort(self, array):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                if j + 1 < len(array) and array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]