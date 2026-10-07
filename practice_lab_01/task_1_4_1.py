# 1. cube(n)
def cube(n):
    return n ** 3


# 2. factorial(n)
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# 3. count_pattern(pattern, lst)
def count_pattern(pattern, lst):
    count = 0

    for i in range(len(lst) - len(pattern) + 1):
        if lst[i:i + len(pattern)] == list(pattern):
            count = count + 1

    return count


# 4. Multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


# 5. Simple Calculator
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        print(num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero.")

    else:
        print("Invalid operator.")


# 6. Sort sentence alphabetically
def sort_sentence(sentence):
    words = sentence.split()
    words.sort()

    return " ".join(words)


# Testing

print("Cube:", cube(3))

print("Factorial:", factorial(5))

print(count_pattern(
    ('a', 'b'),
    ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')
))

print(count_pattern(
    ('a', 'b', 'a'),
    ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
))

print("\nMultiplication Table:")
multiplication_table(5)

print("\nSorted Sentence:")
print(sort_sentence("python is a powerful programming language"))


calculator()