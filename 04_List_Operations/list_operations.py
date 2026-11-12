list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']

# 1. Nested List
nested_list = [list1, list2]
print("1. Nested List:", nested_list)

# 2. Length of a list
print("2. Length of list1:", len(list1))
print("Length of list2:", len(list2))

# 3. Concatenation of two lists
concatenated_list = list1 + list2
print("3. Concatenated List:", concatenated_list)

# 4. Membership
print("4. Is 3 in list1?", 3 in list1)
print("Is 'x' in list2?", 'x' in list2)

# 5. Iteration through the list
print("5. Elements of list1:")
for item in list1:
    print(item, end=" ")
print()

# 6. Indexing
print("6. Element at index 2 in list1:", list1[2])
print("Element at index -1 (last element) in list2:", list2[-1])

# 7. Slicing
print("7. Slice list1 from index 1 to 3:", list1[1:4])
print("Slice list2 from start to index 2:", list2[:3])

# 8. Append
list1.append(6)
print("8. List1 after appending 6:", list1)

# 9. Insert
list2.insert(2, 'x')
print("9. List2 after inserting 'x' at index 2:", list2)

# 10. Deletion
list1.remove(3)
print("10. List1 after removing 3:", list1)

# 11. Pop
popped_item = list2.pop()
print("11. List2 after popping:", list2)
print("Popped item:", popped_item)

# 12. Sorting
list1.sort()
print("12. Sorted List1:", list1)

# 13. Reverse
list1.reverse()
print("13. Reversed List1:", list1)

# 14. List comprehension
squares = [x**2 for x in list1]
print("14. List of squares from List1:", squares)
