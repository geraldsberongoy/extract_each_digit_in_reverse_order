# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# Pseudocode
# number = 7536
# number = str(number)
# reversed = number[::-1]
# print reverse with .join to add spaces between

# # # CODE # # #

number = 7536
reversed = str(number)[::-1]

print(f"The given number is: {number}\n")
print("The reversed number is:", " ".join(reversed))