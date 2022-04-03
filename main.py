# imports
import random
import time

from NotChangedOptimizationBubbleSort import NotChangedOptimizedBubbleSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from SortContext import SortContext


# random lists generation
random_1k_list = []
for i in range(1000):
    random_1k_list.append(random.randrange(1, 1000))

random_10k_list = []
for i in range(10000):
    random_10k_list.append(random.randrange(1, 10000))

random_100k_list = []
for i in range(100000):
    random_100k_list.append(random.randrange(1, 100000))


sequential_1k_list = []
for i in range(1000):
    sequential_1k_list.append(i)

sequential_10k_list = []
for i in range(10000):
    sequential_10k_list.append(i)

sequential_100k_list = []
for i in range(100000):
    sequential_100k_list.append(i)


############################## short sort execution
# bubble_sort = BubbleSort()
# insertion_sort = InsertionSort()
# selection_sort = SelectionSort()
#
# sorter = SortContext(bubble_sort)

# my_test = [19, 23, 20, 17, 10, 11, 3, 1, 0, 4]
# print(my_test.__str__())
# st1 = my_test.copy()
# sorter.get_strategy().sort(st1)
# print(st1.__str__())
#
# sorter.set_strategy(insertion_sort)
# print(my_test.__str__())
# st2 = my_test.copy()
# sorter.get_strategy().sort(st2)
# print(st2.__str__())
#
# sorter.set_strategy(selection_sort)
# print(my_test.__str__())
# st3 = my_test.copy()
# sorter.get_strategy().sort(st3)
# print(st3.__str__())


####################### big data sort execution
bubble_sort = NotChangedOptimizedBubbleSort()
insertion_sort = InsertionSort()
selection_sort = SelectionSort()

# BUBBLE
sorter = SortContext(bubble_sort)
# print(random_1k_list.__str__())
r1kl = random_1k_list.copy()
t1_1kl = time.perf_counter()
sorter.get_strategy().sort(r1kl)
t2_1kl = time.perf_counter()
# print(r1kl.__str__())
print("BUBBLE SORT -----------------random 1k----------------")
print(t2_1kl - t1_1kl)

# print(random_10k_list.__str__())
r10kl = random_10k_list.copy()
t1_10kl = time.perf_counter()
sorter.get_strategy().sort(r10kl)
t2_10kl = time.perf_counter()
print("IMPROVED BUBBLE SORT -----------------random 10k----------------")
print(t2_10kl - t1_10kl)
# print(r10kl.__str__())

# print(random_100k_list.__str__())
r100kl = random_100k_list.copy()
t1_100kl = time.perf_counter()
sorter.get_strategy().sort(r100kl)
t2_100kl = time.perf_counter()
print("IMPROVED BUBBLE SORT -----------------random 100k----------------")
print(t2_100kl - t1_100kl)
# print(r100kl.__str__())

# print(sequential_1k_list.__str__())
s_r1kl = sequential_1k_list.copy()
t1_sr1kl = time.perf_counter()
sorter.get_strategy().sort(s_r1kl)
t2_sr1kl = time.perf_counter()
print("IMPROVED BUBBLE SORT -----------------sequential 1k----------------")
print(t2_sr1kl - t1_sr1kl)
# print(s_r1kl.__str__())

# print(sequential_10k_list.__str__())
s_r10kl = sequential_10k_list.copy()
t1_sr10kl = time.perf_counter()
sorter.get_strategy().sort(s_r10kl)
t2_sr10kl = time.perf_counter()
print("IMPROVED BUBBLE SORT -----------------sequential 10k----------------")
print(t2_sr10kl - t1_sr10kl)
# print(s_r10kl.__str__())

# print(sequential_100k_list.__str__())
s_r100kl = sequential_100k_list.copy()
t1_sr100kl = time.perf_counter()
sorter.get_strategy().sort(s_r100kl)
t2_sr100kl = time.perf_counter()
print("IMPROVED BUBBLE SORT -----------------sequential 100k----------------")
print(t2_sr100kl - t1_sr100kl)
# print(s_r100kl.__str__())

# INSERTION
sorter.set_strategy(insertion_sort)


#SELECTION