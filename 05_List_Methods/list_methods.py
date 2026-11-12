# Initialize a list
my_list = [10, 20, 30, 40, 50]

# 1. Add an element at a specific position using 'insert'
def add_element(my_list, index, element):
    my_list.insert(index, element)
    print(f"List after adding element {element} at index {index}: {my_list}")

# 2. Append an element at the end using 'append'
def append_element(my_list, element):
    my_list.append(element)
    print(f"List after appending element {element}: {my_list}")

# 3. Extend the list by adding elements from another list using 'extend'
def extend_list(my_list, new_elements):
    my_list.extend(new_elements)
    print(f"List after extending with elements {new_elements}: {my_list}")

# 4. Delete an element at a specific index using 'del'
def delete_element(my_list, index):
    try:
        del my_list[index]
        print(f"List after deleting element at index {index}: {my_list}")
    except IndexError:
        print(f"Index {index} out of range! List unchanged: {my_list}")

# Testing the list methods
print(f"Initial list: {my_list}")
add_element(my_list, 2, 25)
append_element(my_list, 60)
extend_list(my_list, [70, 80])
delete_element(my_list, 1)
