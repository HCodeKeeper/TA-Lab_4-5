from Sort import Sort


class SelectionSort(Sort):

    def __init__(self):
        super().__init__()
        pass

    def sort(self, array):
        for i in range(len(array)):
            index_to_insert = i
            min_element_index = i
            for j in range(i, len(array)):
                if array[j] < array[min_element_index]:
                    min_element_index = j
            array[index_to_insert], array[min_element_index] = array[min_element_index], array[index_to_insert]