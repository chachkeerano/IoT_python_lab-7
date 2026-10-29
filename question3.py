# Question 3: Create a set of five numbers, add 10, and remove one existing number.

numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# Add 10 to the set
numbers.add(10)
print("After adding 10:", numbers)

# Remove one existing number (3 is in the set, so remove() is safe here)
numbers.remove(3)
print("After removing 3:", numbers)
