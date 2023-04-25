print("----Task 1-----")
print()
numbers = [int(input("Enter Number: ")) for _ in range(3)]
sum_of_numbers = sum(numbers)
print("Sum of the Numbers: " + str(sum_of_numbers))
print("----Task 2-----")
print()


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


if number1 > number2:
    print("First number is greater!")
elif number2 > number1:
    print("Second number is greater!")
else:
    print("Numbers are equal!")

if number1 > 10000 and number2 > 10000:

    print("Numbers are beeeeeeg!")
print("----Task 3-----")
print()

numbers = []
for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

largest_num = max(numbers)

print("The largest number is:", largest_num)

print("----Task 4-----")
print()


month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
    }

month = input("Input the name of Month: ")

days = month_days.get(month.lower())

if days:
    print(f"Number of days in {month}: {days} days")
else:
    print("Invalid month name!")


print("----Task 5-----")
print()


number = int(input("Enter a number: "))

# Check if the number is even and divisible by 3
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is even and divisible by 3.")
else:
    print(f"{number} is not even and divisible by 3.")
