
import random

def generate_random_integers(count):
    random_integers = []
    for _ in range(count):
        random_int = random.randint(1, 100)
        random_integers.append(random_int)
    return random_integers

def print_odd_values(numbers):
    odd_values = [num for num in numbers if num % 2 != 0]
    print("Odd values:", ", ".join(str(num) for num in odd_values))

# Generate 100 random integers
random_numbers = generate_random_integers(100)

# Print only the odd values
print_odd_values(random_numbers)
