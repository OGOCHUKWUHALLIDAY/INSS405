

def collect_numbers():
    numbers = []
    for i in range(10):
        number = float(input("Enter a number: "))
        numbers.append(number)
    return numbers

def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def calculate_sum(numbers):
    total = sum(numbers)
    return total

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        mid1 = sorted_numbers[length // 2 - 1]
        mid2 = sorted_numbers[length // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_numbers[length // 2]
    return median
# Collect numbers from users
input_numbers = collect_numbers()

# Calculate mean, sum, and median
mean = calculate_mean(input_numbers)
sum_of_numbers = calculate_sum(input_numbers)
median = calculate_median(input_numbers)

# Print the results
print("Mean:", mean)
print("Sum:", sum_of_numbers)
print("Median:", median)