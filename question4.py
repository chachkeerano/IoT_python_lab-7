# Question 4: Ask the user for a number and check if it exists in the set.

my_set = {10, 20, 30, 40, 50}
print("The set is:", my_set)

try:
    user_number = int(input("Enter a number: "))

    if user_number in my_set:
        print(user_number, "exists in the set.")
    else:
        print(user_number, "does not exist in the set.")
except ValueError:
    # This runs if the user types letters or leaves it empty
    print("Invalid input! Please enter a whole number.")
