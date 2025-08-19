for number in range(1, 21):
    print(number)

numbers = list(range(1, 10))
for number in numbers:
    print(number)
minimum_number = min(numbers)
maximum_number = max(numbers)
print(f"The minimum number is {minimum_number}.\n The maximum number is {maximum_number}.")
odd_numbers = list(range(1, 21, 2))
print(f"The odd numbers are:{odd_numbers}")
digits = []
for value in range(3,30):
    multiples_of_three = value * 3
    digits.append(multiples_of_three)

print(digits)
cubes = [value ** 3 for value in range(1,11)]
print(cubes)

