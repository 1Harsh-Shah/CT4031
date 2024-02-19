def multiply_numbers(numbers):

    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
my_list = [2, 3, 24, -5]
result = multiply_numbers(my_list)
print("Result:", result)
