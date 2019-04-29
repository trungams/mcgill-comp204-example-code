#!/usr/bin/env python3

"""This file contains example code for lists and tuples in Python
"""


if __name__ == '__main__':
    # Lists are created using square brackets.
    # Be careful when naming variable, you don't want to override
    # the 'list' keyword in Python
    my_list = [1, -2, 3.0, 1, 'and a string!']
    my_list2 = list()       # this creates an empty list
    my_list3 = []           # this also creates an empty list

    # list comprehension
    my_list4 = [i**2 for i in range(10)]

    # my_list4 is similar to
    for i in range(10):
        my_list2.append(i**2)

    # another example: creating a list of even numbers from 1 to 100
    for i in range(1, 101):
        if i % 2 == 0:
            my_list3.append(i)

    # this can be done using list comprehension as well
    my_list5 = [i for i in range(1, 101) if i % 2 == 0]


    # Tuples are ordered containers of multiple elements
    my_tuple1 = (1, 2, 2.0, True, "False")

    # to create a tuple with only 1 element, you need a comma
    my_tuple2 = ("hello",)

    # tuples are immutable, so once created, you cannot change its content
    try:
        my_tuple1[0] = True
    except TypeError:
        print("Error caught when trying to update a tuple")

    # you can create a tuple from a list
    my_tuple3 = tuple([1,2,3,4,5])

    # you can unpack a tuple, the same way you would do with list
    a, b, c = (1, 2, 3)
    print(a, b, c)


    # Dictionary provides a key-value mapping in Python
    # this creates an empty dictionary, similar to doing dict()
    my_dictionary1 = {}

    # add a new key-value pair to the dictionary
    my_dictionary1["key_1"] = "value_1"

    # look up a key-value pair in the dictionary
    print(my_dictionary1["key_1"])
    print(my_dictionary1.get("key_1"))

    # get() methods will return None if the key does not exist
    print(my_dictionary1.get("key_dne"))

    # you can also specify a certain value that you would like to get
    # if the key does not exist
    print(my_dictionary1.get("key_dne", "hello there"))     # prints "hello there" if key_dne does not exist, else prints the corresponding value

    # please note that the get() method cannot be used to assign values to a key

    # for updating a key-value pair in a dictionary, you can use the assignment operator
    # it will overwrite the existing value
    my_dictionary1["key_1"] = "new_value_1"
    print(my_dictionary1.get("key_1"))

    # if you don't want it to overwrite, use setdefault()
    my_dictionary1.setdefault("key_1", "newer_value_1")
    print(my_dictionary1.get("key_1"))

    # if you have two dictionaries and want to merge them, use update()
    my_dictionary2 = {"key_2": "value_2"}
    my_dictionary1.update(my_dictionary2)
    print(my_dictionary1)

    # dictionary comprehension in Python is also a thing
    # suppose that we have a list of 2-tuples
    list_to_dict = [('math', 10), ('chemistry', 9), ('biology', 7)]
    # we can create a dictionary where name of subject is key and the number is value
    to_dict = {key: value for key, value in list_to_dict}
    print(to_dict)


    # Practice problem: given a list of patients and diseases in the format:
    # [(patient_id_1, disease_id_1), (patient_id_2, disease_id_2), ...]
    # How do we get:
    # - List of unique patient IDs? of unique disease IDs?
    # - Patients who have disease A?
    # - Patients who have both A and B?
    # - Patients who only have C?

    lst = [(1, 'A'), (2, 'A'), (3, 'B'),
           (1, 'B'), (2, 'C'), (4, 'C')]

    # unique patient ids and diseases ids
    unique_patients = set([t[0] for t in lst])
    unique_diseases = set([t[1] for t in lst])

    # create sets of patients who have A, B, and C
    has_A = set([t[0] for t in lst if t[1] == 'A'])
    has_B = set([t[0] for t in lst if t[1] == 'B'])
    has_C = set([t[0] for t in lst if t[1] == 'C'])

    # patients who have both A and B
    both_a_and_b = has_A.intersection(has_B)

    # patients who only have C
    only_C = has_C - (has_A | has_B)

