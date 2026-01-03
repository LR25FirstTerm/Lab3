import random
import time
import logging
logging.basicConfig(level = logging.INFO, filename = "py_log.log", filemode = "w", format = "%(asctime)s %(levelname)s %(message)s")


def bubble_sort(data):
    logging.info(f"Start bubble sort")
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    logging.info(f"End bubble sort")


def selection_sort(nums):
    logging.info(f"Start selection sort")
    k = 0
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    logging.info(f"End selection sort")


def insertion_sort(nums):
    logging.info(f"Start insertion sort")
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    logging.info(f"End insertion sort")

random_list = [random.randint(1, 100) for i in range(100)]
print('Not sorted list:', random_list)

list1 = random_list.copy()
bubble_sort(list1)
print("Sorted list:", list1)

list2 = random_list.copy()
selection_sort(list2)
print("Sorted list:", list2)

list3 = random_list.copy()
insertion_sort(list3)
print("Sorted list:", list3)