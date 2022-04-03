from Sort import Sort


class SortContext:
    def __init__(self, sort_strategy: Sort):
        self.__sort_strategy = sort_strategy


    def get_strategy(self):
        return self.__sort_strategy

    def set_strategy(self, strategy: Sort):
        self.__sort_strategy = strategy

