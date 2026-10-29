# Question 2: Convert a list into a set to remove duplicates.

numbers = [2, 4, 2, 6, 4, 8, 8]
print("Original list:", numbers)

# A set can't hold duplicate values, so converting the list removes them.
unique_numbers = set(numbers)
print("Set after removing duplicates:", unique_numbers)
