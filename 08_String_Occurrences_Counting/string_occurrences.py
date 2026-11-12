def count_occurrences(s1, s2):
    count = s2.count(s1)
    return count

# Test the function
s1 = input("Enter the substring to find (s1): ")
s2 = input("Enter the main string (s2): ")

occurrences = count_occurrences(s1, s2)

print(f"The substring '{s1}' occurs {occurrences} time(s) in the string '{s2}'.")
