# imports
import random
import time
from termcolor import colored

from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from SortContext import SortContext
from ShellSort import ShellSort

random_lists = [
    [random.randrange(1, 1000) for i in range(1000)],
    [random.randrange(1, 5000) for i in range(5000)],
    [random.randrange(1, 10000) for i in range(10000)],
    [random.randrange(1, 20000) for i in range(20000)],
    [random.randrange(1, 50000) for i in range(50000)]
]

not_random_lists = [
    [i for i in range(1000)],
    [i for i in range(5000)],
    [i for i in range(10000)],
    [i for i in range(20000)],
    [i for i in range(50000)]
]

def do_tests():
    print(colored("RANDOM LISTS", 'yellow'))
    for lst in random_lists:
        print(colored("RANDOM {0} elements list: ".format(len(lst)), 'green'), end="")
        t1 = time.perf_counter()
        sorter.get_strategy().sort(lst.copy())
        t2 = time.perf_counter()
        print(colored(str(t2 - t1), 'blue'))

    print(colored("NOT RANDOM LISTS", 'yellow'))
    for lst in not_random_lists:
        print(colored("NOT RANDOM {0} elements list: ".format(len(lst)), 'green'), end="")
        t1 = time.perf_counter()
        sorter.get_strategy().sort(lst.copy())
        t2 = time.perf_counter()
        print(colored(str(t2 - t1), 'blue'))

####################### big data sort execution
bubble_sort = BubbleSort()
insertion_sort = InsertionSort()
selection_sort = SelectionSort()
shell_sort = ShellSort()

# BUBBLE
print(colored("BUBBLE SORT", 'red'))
sorter = SortContext(bubble_sort)
do_tests()

# INSERTION
print(colored("INSERTION SORT", 'red'))
sorter.set_strategy(insertion_sort)
do_tests()

# SELECTION
print(colored("SELECTION SORT", 'red'))
sorter.set_strategy(selection_sort)
do_tests()

# SHELL
print(colored("SHELL SORT", 'red))
sorter.set_strategy(shell_sort)
do_tests()
