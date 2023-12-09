def two_positive(a, b, c):
    positive_count = sum(x > 0 for x in (a, b, c))
    return positive_count == 2

# Example usage:
result = two_positive(2, 4, -3)
print(result)  # Output: True

result = two_positive(-4, 6, 8)
print(result)  # Output: True

result = two_positive(4, -6, 9)
print(result)  # Output: True

result = two_positive(-4, 6, 0)
print(result)  # Output: False

result = two_positive(4, 6, 10)
print(result)  # Output: False

result = two_positive(-14, -3, -4)
print(result)  # Output: False
