# Practice 1: Create a program that asks the user for their age and then calculates how many years it will take for them to turn 100.

# userAge = int(input("Enter your age: "))
# toHundred = 100 - userAge
# print(f"You will turn 100 in {toHundred} years")


# Practice 2: Write a program that calculates the total price of items in a shopping cart, where the prices are integers.

# item1 = 75;
# item2 = 78;

# total = item1 + item2;

# # printing the total item 
# print(f"The total item price is {total}$")

# Practice 1: Write a program that calculates the area of a circle given its radius.
# import math
# radius = float(input("Enter the radius: "))
# areaOfRadius = math.pi * radius ** 2;
# print(f"The area of the circle is {areaOfRadius:.2f}"); 

# Practice 2: Create a simple calculator that performs division between two floating-point numbers.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = num1 / num2;
# print(f"Result: {result}")

# Practice 1: Write a program that takes a string input from the user and reverses it.
# name = input("Enter you name: ")
# reverse = name[::-1];
# print(reverse)

# Practice 2: Write a program that capitalizes the first letter of each word in a given sentence.
# sentense = "Amar sonar bangla ami tomai valobashi";
# capitalize_sen = sentense.title();
# print(capitalize_sen);

# Practice 1: Create a list of 5 numbers and find their sum.

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers);
# print(total)

# Practice 1: Write a program that stores 3 student names in a tuple and prints each name.
# students = ["Alice", "Bob", "Charlie"]
# students.append("Rakib")
# print(students)

# Practice 1: Write a program that stores 3 student names in a tuple and prints each name.
students = ("Alice", "Bob", "Charlie")
for std in students:
    print(std)
