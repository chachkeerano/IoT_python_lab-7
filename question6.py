# Question 6: Practice union, intersection, difference and symmetric difference.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A =", A)
print("B =", B)
print()

# a) All unique elements in A and B (union)
print("a) Union (A | B):", A | B)

# b) Elements common to both sets (intersection)
print("b) Intersection (A & B):", A & B)

# c) Differences
print("c) A - B:", A - B)
print("   B - A:", B - A)
print("   Why they differ: A - B keeps the elements that are only in A,")
print("   while B - A keeps the elements that are only in B. The order")
print("   matters because each one starts from a different set.")

# d) Elements in either A or B, but not in both (symmetric difference)
print("d) Symmetric difference (A ^ B):", A ^ B)
