# tuple is ordered
# tuple is immutable
# tuple can contain duplicate values

# set is unordered
# set is mutable (changeable)
# set can not contain duplicate elements

# List is ordered
# List is changable
# List can contain duplicate elements

# dict is ordered
# dict is mutable (changable)
# dict can not contain duplicate keys

# list task 1
# user_list = input('Enter elements seperated by spaces: ')
# element = input('Enter the element: ')
# print(user_list.split().count(element))

# list task 2
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(number) for number in user_input.split()]
# print(sum(user_list))

# list task 3
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(number) for number in user_input.split()]
# print(max(user_list))

# list task 4
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(number) for number in user_input.split()]
# print(min(user_list))

# list task 5
# user_input = input('Enter elements seperated by spaces: ')
# element = input('Enter the element: ')
# print(element in user_input.split())

# list task 6
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# if user_list == []:
#     print(None)
# else:
#     print(user_list[0])

# list task 7
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# if user_list == []:
#     print(None)
# else:
#     print(user_list[-1])

# list task 8
# user_input = input('Enter elements seperated by spaces: ')
# print(user_input.split()[:3])

# list task 9
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_list.reverse()
# print(user_list)

# list task 10
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_list.sort()
# print(user_list)

# list task 11
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# print(list(set(user_list)))

# list task 12
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# element = input('Enter the element: ')
# index = int(input('Enter the index: '))
# user_list.insert(index, element)
# print(user_list)

# list task 13
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# element = input('Enter the element: ')
# print(user_list.index(element))

# list task 14
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# print(user_list == [])

# list task 15
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(num) for num in user_input.split()]
# number_of_evens = 0
# for num in user_list:
#     if num % 2 == 0:
#         number_of_evens = number_of_evens + 1
# print(number_of_evens)

# list task 16
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(num) for num in user_input.split()]
# number_of_odds = 0
# for num in user_list:
#     if num % 2 != 0:
#         number_of_odds = number_of_odds + 1
# print(number_of_odds)

# list task 17
# user_input1 = input('Enter elements of the first list seperated by spaces: ')
# user_input2 = input('Enter elements of the second list seperated by spaces: ')
# print(user_input1.split() + user_input2.split())

# list task 18
# IF THERE IS NO DIFFERENCE IN ORDER
# user_input_list = input('Enter elements of the list seperated by spaces: ')
# user_input_sublist = input('Enter elements of the sublist seperated by spaces: ')
# user_list = user_input_list.split()
# user_sublist = user_input_sublist.split()
# if set(user_sublist) == (set(user_sublist) & set(user_list)):
#     i = 0
#     for element in list(set(user_sublist)):
#         if user_sublist.count(element) <= user_list.count(element):
#             i = i + 1
#     if i == len(set(user_sublist)):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

# IF THERE IS DIFFERENCE IN ORDER
# user_input_list = input('Enter elements of the list seperated by spaces: ')
# user_input_sublist = input('Enter elements of the sublist seperated by spaces: ')
# user_list = user_input_list.split()
# user_sublist = user_input_sublist.split()
# n = 0
# for i in range(len(user_list) - len(user_sublist) + 1):
#     if user_sublist == user_list[i: i + len(user_sublist)]:
#         n = n + 1
# if n > 0:
#     print(True)
# else:
#     print(False)

# list task 19: Replace Element: Given a list, replace the first occurrence of a specified element with another element.
# user_input = input('Enter elements of the list seperated by spaces: ')
# user_list = user_input.split()
# specefied_element = input('Enter the specified element: ')
# another_elemenet = input('Enter the another element: ')
# user_list[user_list.index(specefied_element)] = another_elemenet
# print(user_list)

# list task 20: Find Second Largest: From a given list, find the second largest element.
# user_input = input('Enter elements of the list seperated by spaces: ')
# user_list = [int(x) for x in user_input.split()]
# max_num = max(user_list)
# for num in user_list:
#     if max_num in user_list:
#         user_list.remove(max_num)
# print(max(user_list))

# list task 21: Find Second Smallest: From a given list, find the second smallest element.
# user_input = input('Enter elements of the list seperated by spaces: ')
# user_list = [int(x) for x in user_input.split()]
# min_num = min(user_list)
# for num in user_list:
#     if min_num in user_list:
#         user_list.remove(min_num)
# print(min(user_list))

# list task 22: Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.
# user_input = input('Enter elements of the list seperated by spaces: ')
# even_numbers = [num for num in [int(x) for x in user_input.split()] if num % 2 == 0]
# print(even_numbers)

# list task 23: Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.
# user_input = input('Enter elements seperated by spaces: ')
# odd_numbers = [num for num in [int(x) for x in user_input.split()] if num % 2 == 1]
# print(odd_numbers)

# list task 24: List Length: Determine the number of elements in the list.
# user_input = input('Enter elements seperated by spaces: ')
# print(len(user_input.split()))

# list task 25: Create a Copy: Create a new list that is a copy of the original list.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_copy = user_list.copy()
# print(user_copy)

# list task 26: Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# if len(user_list) % 2 == 0:
#     print(user_list[(len(user_list) // 2 - 1) : (len(user_list) // 2 + 1)])
# else:
#     print(user_list[(len(user_list) - 1) // 2])

# list task 27: Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(num) for num in user_input.split()]
# print(max(user_list))

# list task 28: Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [int(num) for num in user_input.split()]
# print(min(user_list))

# list task 29: Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# index = int(input('Enter the index: '))
# user_list.pop(index)
# print(user_list)

# list task 30: Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_copy = user_list.copy()
# user_list.sort()
# print(user_copy == user_list)

# list task 31: Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = list(set(user_input.split()))
# number = int(input('Enter the number: '))
# print(number * user_list)

# list task 32: Merge and Sort: Given two lists, create a new sorted list that merges both lists.
# user_input1 = input('Enter elements of the first seperated by spaces: ')
# user_input2 = input('Enter elements of the second seperated by spaces: ')
# merge = user_input1.split() + user_input2.split()
# merge.sort()
# print(merge)

# list task 33: Find All Indices: Given a list and an element, find all the indices of that element in the list.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# element = input('Enter the element: ')
# i = 0
# while i < len(user_list):
#     if user_list[i] == element:
#         print(i)
#     i = i + 1

# list task 34: Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# num = int(input('Number of positions to rotate: '))
# print(user_list[-num:] + user_list[:-num])

# list task 35: Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).
# start = int(input())
# end = int(input())
# print(list(range(start, end + 1)))

# list task 36: Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [float(x) for x in user_input.split()]
# sum = 0
# for num in user_list:
#     if num > 0:
#         sum = sum + num
# print(sum)

# list task 37: Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = [float(x) for x in user_input.split()]
# sum = 0
# for num in user_list:
#     if num < 0:
#         sum = sum + num
# print(sum)

# list task 38: Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_copy = list(user_list)
# user_copy.reverse()
# print(user_copy)
# print(user_list == user_copy)

# list task 39: Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# num = int(input('Enter the number: '))
# nested_list = [user_list[i:i + num] for i in range(0, len(user_list), num)]
# print(nested_list)

# list task 40: Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# new_list = []
# for element in user_list:
#     if element not in new_list:
#         new_list.append(element)
# print(new_list)

# tuple task 1: Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# element = input('Enter the element: ')
# i = 0
# for e in user_tuple:
#     if e == element:
#         i = i + 1
# print(i)

# tuple task 2: Max Element: From a given tuple, determine the largest element.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(float(x) for x in user_input.split())
# print(max(user_tuple))

# tuple task 3: Min Element: From a given tuple, determine the smallest element.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(float(x) for x in user_input.split())
# print(min(user_tuple))

# tuple task 4: Check Element: Given a tuple and an element, check if the element is present in the tuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# element = input('Enter the element: ')
# print(element in user_tuple)

# tuple task 5: First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# if user_tuple == ():
#     print(None)
# else:
#     print(user_tuple[0])

# tuple task 6: Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# if user_tuple == ():
#     print(None)
# else:
#     print(user_tuple[-1])

# tuple task 7: Tuple Length: Determine the number of elements in the tuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# print(len(user_tuple))

# tuple task 8: Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# print(user_tuple[:3])

# tuple task 9: Concatenate Tuples: Given two tuples, create a new tuple that combines both.
# user_input1 = input('Enter elements of the first seperated by spaces: ')
# user_input2 = input('Enter elements of the second seperated by spaces: ')
# print(tuple(user_input1.split()) + tuple(user_input2.split()))

# tuple task 10: Check if Tuple is Empty: Determine if a tuple has any elements.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# print(user_tuple != ())

# tuple task 11: Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# element = input('Enter the element: ')
# for i in range(len(user_tuple)):
#     if user_tuple[i] == element:
#         print(i)


# tuple task 12: Find Second Largest: From a given tuple, find the second largest element.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(float(x) for x in user_input.split())
# user_list = list(set(user_tuple))
# user_list.sort()
# print(user_list[-2])

# tuple task 13: Find Second Smallest: From a given tuple, find the second smallest element.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(float(x) for x in user_input.split())
# user_list = list(set(user_tuple))
# user_list.sort()
# print(user_list[1])

# tuple task 14: Create a Single Element Tuple: Create a tuple that contains a single specified element.
# element = input('Enter the element: ')
# single_element_tuple = (element,)
# print(single_element_tuple)

# tuple task 15: Convert List to Tuple: Given a list, create a tuple containing the same elements.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())

# tuple task 16: Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_tuple = tuple(user_list)
# user_list.sort()
# print(tuple(user_list) == user_tuple)

# tuple task 17: Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(float(x) for x in user_input.split())
# start = int(input())
# end = int(input())
# subtuple = user_tuple[start : end]
# print(max(subtuple))

# tuple task 18: Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(float(x) for x in user_input.split())
# start = int(input())
# end = int(input())
# subtuple = user_tuple[start : end]
# print(min(subtuple))


# tuple task 19: Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# element = input('Enter the element: ')
# user_list = list(user_tuple)
# user_list.remove(element)
# print(tuple(user_list))

# tuple task 20: Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# num = int(input())
# my_tuple = tuple(user_tuple[i: i + num] for i in range(0, len(user_tuple), num))
# print(my_tuple)

# tuple task 21: Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(int(x) for x in user_input.split())
# new_list = []
# for element in user_tuple:
#     for i in range(element):
#         new_list.append(element)
# print(tuple(new_list))]

# tuple task 22: Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# start = int(input())
# end = int(input())
# new_list = []
# for i in range(start, end + 1):
#     new_list.append(i)
# print(tuple(new_list))

# tuple task 23: Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# user_list = list(user_tuple)
# user_list.reverse()
# print(tuple(user_list))

# tuple task 24: Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# user_list = list(user_tuple)
# user_list.reverse()
# print(tuple(user_list) == user_tuple)

# tuple task 25: Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# user_input = input('Enter elements seperated by spaces: ')
# user_tuple = tuple(user_input.split())
# new_list = []
# for element in user_tuple:
#     if element not in new_list:
#         new_list.append(element)
# print(tuple(new_list))

# set task 1: Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
# user_input1 = input('Enter elements of the first set seperated by spaces: ')
# user_input2 = input('Enter elements of the second set seperated by spaces: ')
# set1 = set(user_input1.split())
# set2 = set(user_input2.split())
# union_set = set1 | set2
# print(union_set)

# set task 2: Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
# user_input1 = input('Enter elements of the first set seperated by spaces: ')
# user_input2 = input('Enter elements of the second set seperated by spaces: ')
# set1 = set(user_input1.split())
# set2 = set(user_input2.split())
# intersection_set = set1 & set2
# print(intersection_set)

# set task 3: Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
# user_input1 = input('Enter elements of the first set seperated by spaces: ')
# user_input2 = input('Enter elements of the second set seperated by spaces: ')
# set1 = set(user_input1.split())
# set2 = set(user_input2.split())
# difference_set = set1.difference(set2)
# print(difference_set)

# set task 4: Check Subset: Given two sets, check if one set is a subset of the other.
# user_input1 = input('Enter elements of the first set seperated by spaces: ')
# user_input2 = input('Enter elements of the second set seperated by spaces: ')
# set1 = set(user_input1.split())
# set2 = set(user_input2.split())
# intersection_set = set1 & set2
# if set1 == intersection_set or set2 == intersection_set:
#     print(True)
# else: 
#     print(False)

# set task 5: Check Element: Given a set and an element, check if the element exists in the set.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# element = input('Enter the element: ')
# print(element in user_set)

# set task 6: Set Length: Determine the number of unique elements in a set.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# print(len(user_set))

# set task 7: Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# print(set(user_list))

# set task 8: Remove Element: Given a set and an element, remove the element if it exists.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# element = input('Enter the element: ')
# user_set.remove(element)
# print(user_set)

# set task 9: Clear Set: Create a new empty set from an existing set.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# user_set.clear()
# print(user_set)

# set task 10: Check if Set is Empty: Determine if a set has any elements.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# print(len(user_set) > 0)

# set task 11: Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.
# user_input1 = input('Enter elements of the first set seperated by spaces: ')
# user_input2 = input('Enter elements of the second set seperated by spaces: ')
# set1 = set(user_input1.split())
# set2 = set(user_input2.split())
# symmetric_set = set1 ^ set2
# print(symmetric_set)

# set task 12: Add Element: Given a set and an element, add the element to the set if it is not already present.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# element = input('Enter the element: ')
# user_set.add(element)
# print(user_set)

# set task 13: Pop Element: Given a set, remove and return an arbitrary element from the set.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# user_set.pop()
# print(user_set)

# set task 14: Find Maximum: From a given set of numbers, find the maximum element.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(float(x) for x in user_input.split())
# print(max(user_set))

# set task 15: Find Minimum: From a given set of numbers, find the minimum element.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(float(x) for x in user_input.split())
# print(min(user_set))

# set task 16: Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(int(x) for x in user_input.split())
# even_set = {x for x in user_set if x % 2 == 0}
# print(even_set)

# set task 17: Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(int(x) for x in user_input.split())
# even_set = {x for x in user_set if x % 2 == 1}
# print(even_set)

# set task 18: Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).
# start = int(input())
# end = int(input())
# set = set(range(start, end + 1))
# print(set)

# set task 19: Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
# user_input1 = input('Enter elements of the first list seperated by spaces: ')
# user_input2 = input('Enter elements of the second list seperated by spaces: ')
# user_list1 = user_input1.split()
# user_list2 = user_input2.split()
# merged_set = set(user_list1) | set(user_list2)
# print(merged_set)

# set task 20: Check Disjoint Sets: Given two sets, check if they have no elements in common.
# user_input1 = input('Enter elements of the first set seperated by spaces: ')
# user_input2 = input('Enter elements of the second set seperated by spaces: ')
# set1 = set(user_input1.split())
# set2 = set(user_input2.split())
# print((set1 & set2) == set())

# set task 21: Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_list = list(set(user_list))
# print(user_list)

# set task 22: Get Unique Elements in Order: Given a list, create a set that contains unique elements while maintaining their first appearance order.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# new_list = []
# for element in user_list:
#     if element not in new_list:
#         new_list.append(element)
# print(set(new_list))
# set is unoredered

# set task 23: Create Nested Sets: Create a set of sets, where each inner set contains a specified number of unique elements.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(user_input.split())
# user_list = list(user_set)
# new_list = []
# num = int(input('Enter the number: '))
# for i in range(0, len(user_list), num):
#     new_list.append(frozenset(user_list[i: i + num]))
# # print(new_list)
# new_set = set(new_list)
# print(new_set)

# set task 24: Count Unique Elements: Given a list, determine the count of unique elements using a set.
# user_input = input('Enter elements seperated by spaces: ')
# user_list = user_input.split()
# user_set = set(user_list)
# for element in user_set:
#     i = 0
#     for x in user_list:
#         if x == element:
#             i = i + 1
#     print(f'{element} - {i} times')


# a = list(map(int, input().split()))
# a.sort()
# b = []
# k = 1
# for i in range(1, len(a)):
#     if a[i-1] == a[i]:
#         k+=1
#     else:
#         d = [a[i-1], k]
#         b.append(d)
#         k = 1
# f = [a[len(a)-1], k]
# b.append(f)
# print(b) 

# set task 25: Generate Random Set: Create a set with a specified number of random integers within a certain range.
# user_input = input('Enter elements seperated by spaces: ')
# user_set = set(int(x) for x in user_input.split())
# num = int(input('Enter the number: '))
# print(set(list(user_set)[:num]))

# dictionary task 1: Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# value = input()
# if value == '':
#     print('value is empty')
# else:
#     print(thisdict[value])

# dictionary task 2: Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# key = input()
# if key in thisdict:
#     print(True)
# else:
#     print(False)

# dictionary task 3: Count Keys: Determine the number of keys in the dictionary.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = list(thisdict.keys())
# print(len(x))

# dictionary task 4: Get All Keys: Create a list that contains all the keys in the dictionary.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = list(thisdict.keys())
# print(x)

# dictionary task 5: Get All Values: Create a list that contains all the values in the dictionary.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = list(thisdict.values())
# print(x)

# dictionary task 6: Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
# dict1 = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2024
# }
# dict2 = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# dict2.update(dict1)
# print(dict2)

# dictionary task 7: Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# key_to_revome = "brand"
# if key_to_revome not in thisdict:
#     print("key doesn't exist")
# else:
#     thisdict.pop(key_to_revome)
#     print(thisdict)

# dictionary task 8: Clear Dictionary: Create a new empty dictionary.
# empty_dict = dict()

# dictionary task 9: Check if Dictionary is Empty: Determine if a dictionary has any elements.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if len(thisdict) == 0:
#     print(False)
# else: 
#     print(True)

# dictionary task 10: Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# key = "brand"
# if key in thisdict:
#     print(f'[{key}, {thisdict[key]}]')
# else:
#     print('doesn\'t exist')

# dictionary task 11: Update Value: Given a dictionary, update the value for a specified key.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# key = "year"
# value = 2000
# thisdict.update({key: value})
# print(thisdict)

# dictionary task 12: Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1
# }
# value = 1
# new_list = list(thisdict.keys())
# n = 0
# for i in range(len(thisdict)):
#     if thisdict[new_list[i]] == value:
#         n = n + 1
# print(n)

# dictionary task 13: Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1
# }
# new_dict = dict()
# new_list = list(thisdict.keys())
# for i in range(len(thisdict)):
#     new_dict.update({thisdict[new_list[i]]: new_list[i]})
# print(new_dict)

# new_dict = {value: key for key, value in thisdict.items()}
# print(new_dict)

# dictionary task 14: Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1
# }
# valueby = 1
# new_dict = [key for key, value in thisdict.items() if value == valueby]
# print(new_dict)

# dictionary task 15: Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# key_list = ['a', 'b', 'c', 'd']
# value_list = [1, 2, 3, 4]
# new_dict = dict()
# for i in range(len(key_list)):
#     new_dict.update({key_list[i]: value_list[i]})
# print(new_dict)

# dictionary task 16: Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# new_list = [value for key, value in myfamily.items()]
# print(new_list)
# for i in range(len(new_list)):
#     if type(new_list[i]) == dict:
#         print(False)
#         break

# dictionary task 17: Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# nested_dict = {
#     "student1": {
#         "name": "John",
#         "grades": {
#             "math": 85,
#             "science": 90
#         }
#     },
#     "student2": {
#         "name": "Jane",
#         "grades": {
#             "math": 88,
#             "science": 95
#         }
#     }
# }

# print(f'Jane\'s grade in math is {nested_dict["student2"]["grades"]["math"]}')

# dictionary task 19: Count Unique Values: Given a dictionary, determine the number of unique values it contains.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1
# }
# new_set = set(thisdict.values())
# print(len(new_set))

# dictionary task 20: Sort Dictionary by Key: Create a new dictionary sorted by keys.
# thisdict = {
#     'f' : 1,
#     'b' : 2,
#     'e' : 1,
#     'd' : 3,
#     'c' : 1,
#     'a' : 1
# }
# new_list = list(thisdict.keys())
# new_list.sort()
# new_dict = dict()
# for i in range(len(new_list)):
#     new_dict.update({new_list[i]: thisdict[new_list[i]]})
# print(new_dict)

# dictionary task 21: Sort Dictionary by Value: Create a new dictionary sorted by values.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1,
#     'g' : 2
# }
# values_list = list(set(thisdict.values()))
# values_list.sort()
# new_dict = dict()
# for i in range(len(values_list)):
#     keys_list = {key: value for key, value in thisdict.items() if value == values_list[i]}
#     new_dict.update(keys_list)
# print(new_dict)

# dictionary task 22: Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1,
#     'g' : 2
# }
# meet_condition = 1
# new_dict = {key: value for key, value in thisdict.items() if value > meet_condition}
# print(new_dict)

# dictionary task 23: Check for Common Keys: Given two dictionaries, check if they have any keys in common.
# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# dict2 = {
#     'c': 4,
#     'd': 5,
#     'e': 6
# }
# common_keys = set(dict1.keys()) & set(dict2.keys())
# print(common_keys)

# dictionary task 24: Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
# key_value_pairs = (("a", 1), ("b", 2), ("c", 3))
# my_dict = dict(key_value_pairs)
# print(my_dict)

# dictionary task 25: Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
# thisdict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 1,
#     'd' : 3,
#     'e' : 1,
#     'f' : 1,
#     'g' : 2
# }
# new_list = list(thisdict.items())
# print(new_list[0])