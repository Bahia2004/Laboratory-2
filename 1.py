numbers = [1, 4, 7, 10, 13, 16]

sum_even = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        sum_even += numbers[i]

print("Sum of even numbers:", sum_even)