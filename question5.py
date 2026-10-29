# Question 5: Predict the length of the set and explain why.

values = {1, 2, 2, 3, 3, 3, 4}

print("Set:", values)
print("Length of the set:", len(values))

# Explanation:
# A set stores only unique elements. Even though we wrote 2 twice and 3 three
# times, Python keeps just one copy of each. So the set becomes {1, 2, 3, 4}
# and its length is 4 (not 7).
print("Explanation: Sets remove duplicates automatically, so only 1, 2, 3 and 4 remain. That is why the length is 4.")
