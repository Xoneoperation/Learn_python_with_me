for value in range(1, 11):
    print(value + 1)
numbers = list(range(1,22))
print(numbers)
even_numbers = list(range(2, 22, 2))
print(even_numbers)
squares = []
for values in range(1, 22):
    square = values ** 2
    squares.append(square)
print(squares)
squares = [value ** 2 for value in range(1,22)]


