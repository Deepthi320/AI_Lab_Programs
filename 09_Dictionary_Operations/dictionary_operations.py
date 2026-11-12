# Initialize a dictionary
my_dict = {
    "name": "Ram",
    "age": 25,
    "city": "Bellary",
    "profession": "Engineer"
}

# 1. Accessing values using [] (key)
def access_by_key(my_dict, key):
    try:
        value = my_dict[key]
        print(f"Value for key '{key}': {value}")
    except KeyError:
        print(f"Key '{key}' not found in the dictionary.")

# 2. Traversing the dictionary and printing key-value pairs
def traverse_dict(my_dict):
    print("Traversing the dictionary:")
    for key in my_dict:
        print(f"{key}: {my_dict[key]}")

# 3. Using the keys() method to get all keys
def get_keys(my_dict):
    keys = my_dict.keys()
    print(f"Keys in the dictionary: {list(keys)}")

# 4. Using the values() method to get all values
def get_values(my_dict):
    values = my_dict.values()
    print(f"Values in the dictionary: {list(values)}")

# 5. Using the items() method to get key-value pairs
def get_items(my_dict):
    items = my_dict.items()
    print("Key-Value pairs in the dictionary:")
    for key, value in items:
        print(f"{key}: {value}")

# Demonstrating dictionary operations
print("Initial Dictionary:", my_dict)

# Access a specific value using a key
access_by_key(my_dict, "name")
access_by_key(my_dict, "age")
access_by_key(my_dict, "country")

# Traversing the dictionary
traverse_dict(my_dict)

# Using dictionary methods
get_keys(my_dict)
get_values(my_dict)
get_items(my_dict)
