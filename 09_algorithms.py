#!/usr/bin/env python3

"""This file contains implementations of simple seaching and sorting
algorithms, namely linear, binary search, insertion and selection sort
"""

from random import shuffle


def linear_search(lst, target):
    """Implementation of linear search"""

    # a counter to show performance
    counter = 0
    for element in lst:
        counter += 1
        if target == element:
            print("FOUND", target, f"after {counter} iterations!")
            return
    print("Not found :(")


def binary_search(lst, target):
    """Implementation of iterative binary search"""

    # a counter to show performance
    counter = 0
    low = 0
    high = len(lst)-1

    while low <= high:
        counter += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            print("FOUND", target, f"after {counter} iterations!")
            return
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("Not found :(")


def insertion_sort(lst):
    length = len(lst)
    for i in range(length):
        j = i-1
        key = lst[i]
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


def selection_sort(lst):
    length = len(lst)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if lst[j] <= lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == '__main__':
    my_list = [i for i in range(10000)]

    print("Using linear search..")
    linear_search(my_list, 4242)

    print("Using binary search..")
    my_list.sort()
    binary_search(my_list, 4242)

    shuffle(my_list)
    print("Shuffled list:")
    print(my_list, sep=", ")
    print("Using insertion sort:")
    my_list = insertion_sort(my_list)
    print(my_list, sep=", ")

    shuffle(my_list)
    print("Shuffled list:")
    print(my_list)
    print("Using selection sort:")
    my_list = selection_sort(my_list)
    print(my_list)


