# Correcting Code Exercise 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 1
rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = "rethgiferiF"
word = "Firefighter"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Program 1
def calculate_average(numbers):
	total = 0
	for num in numbers:
		total += num
	average = total / len(numbers)
	return average

# Program 2
def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

# Program 3
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print("Squared Numbers:", squared_numbers)

# Program 4
def is_prime(n):
	prime = True
	for i in range(2, n):
		if n % i == 0:
			prime = False
		return prime


# Program 5
def print_pattern(rows):
	for i in range(1, len(rows) + 1):
		for j in range(1, i):
			print(j, end="")
			print()

# Program 6
def find_max(numbers):
	max_num = 0
	for num in numbers:
		if num > max_num:
			max_num = num
		return max_num

# Program 7
def reverse_string(s):
	reversed_s = ""
	for char in s:
		reversed_s = char + reversed_s
	return reversed_s

# Program 8
def power_of_two(n):
	powers = [2 ** i for i in range(1, n+1)]
	return powers

# Program 9
def count_vowels(word):
	vowels = "aeiou"
	count = 0
	for char in word:
		if char.lower() in vowels:
			count += 1
	return count

# Program 10
def find_average(nums):
	total = 0
	count = 0
	for num in nums:
		total += num
		count += 1
	average = total / count
	return average

print(calculate_average(numbers))
print(factorial(n))
print(is_prime(n))
print(print_pattern(rows))
print(find_max(numbers))
print(reverse_string(s))
print(power_of_two(n))
print(count_vowels(word))
print(find_average(nums))