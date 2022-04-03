from Sort import Sort


class InsertionSort(Sort):

    def __init__(self):
        super().__init__()
        pass

    def sort(self, array):
        for i in range(len(array)):
            index_to_insert = i
            element = array[i]
            while index_to_insert > 0 and element < array[index_to_insert - 1]:
                array[index_to_insert] = array[index_to_insert - 1]
                index_to_insert -= 1
            array[index_to_insert] = element