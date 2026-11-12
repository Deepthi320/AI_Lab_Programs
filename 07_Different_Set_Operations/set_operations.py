# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# 1. Union of sets
def union_sets(setA, setB):
    union_result = setA.union(setB)
    print(f"Union of setA and setB: {union_result}")

# 2. Intersection of sets
def intersection_sets(setA, setB):
    intersection_result = setA.intersection(setB)
    print(f"Intersection of setA and setB: {intersection_result}")

# 3. Difference of sets (setA - setB)
def difference_sets(setA, setB):
    difference_result = setA.difference(setB)
    print(f"Difference of setA and setB (setA - setB): {difference_result}")

# 4. Symmetric Difference of sets
def symmetric_difference_sets(setA, setB):
    symmetric_difference_result = setA.symmetric_difference(setB)
    print(f"Symmetric difference of setA and setB: {symmetric_difference_result}")

# 5. Check if setA is a subset of setB
def subset_check(setA, setB):
    is_subset = setA.issubset(setB)
    print(f"Is setA a subset of setB?: {is_subset}")

# 6. Check if setA is a superset of setB
def superset_check(setA, setB):
    is_superset = setA.issuperset(setB)
    print(f"Is setA a superset of setB?: {is_superset}")

# 7. Check if two sets are disjoint
def disjoint_check(setA, setB):
    is_disjoint = setA.isdisjoint(setB)
    print(f"Are setA and setB disjoint?: {is_disjoint}")

# Perform and display all set operations
print(f"Set A: {setA}")
print(f"Set B: {setB}\n")

union_sets(setA, setB)
intersection_sets(setA, setB)
difference_sets(setA, setB)
symmetric_difference_sets(setA, setB)
subset_check(setA, setB)
superset_check(setA, setB)
disjoint_check(setA, setB)
