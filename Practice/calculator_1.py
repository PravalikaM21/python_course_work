import os
import time
def addition():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums)
def subtraction():
    It then subtracts the second number from the first and returns the result.
    n_1 = float(input("Enter first number: "))
    n_2 = float(input("Enter second number: "))
    return n_1 - n_2
def multiplication():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    result = 1
    for num in nums:
        result *= num
    return result
def division():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if n2 == 0:
        print("Invalid entry")
        return "Invalid entry"
    print(n1 / n2)
    return n1 / n2
def average():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums) / len(nums)
def factorial(num):
    answer = 1
    for i in range(num):
        answer *= i + 1
    return answer
def complex_arithmetic():
    print("Enter '1' for complex addition")
    print("Enter '2' for complex subtraction")
    print("Enter '3' for complex multiplication")
    print("Enter '4' for complex division")
    choice = input("enter your choice")
    if choice == "1":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sum = 0
        imag_sum = 0
        for i in range(0, len(nums) - 1, 2):
            real_sum += nums[i]
        for i in range(2, len(nums) - 1, 2):
            imag_sum += nums[i]
        imag_sum += nums[-1]
        return f"{real_sum}+ i{imag_sum}"

    elif choice == "2":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sub = nums[0]
        imag_sub = nums[1]
        for i in range(2, len(nums) - 1, 2):
            real_sub -= nums[i]
        for i in range(3, len(nums) - 1, 2):
            imag_sub -= nums[i]
        imag_sub -= nums[-1]
        return f"{real_sub}+ i{imag_sub}"

    elif choice == "3":
        nums = list(
            map(
                int,
                input(
                    "Enter all numbers separated by space maximum 4 elements: "
                ).split(),
            )
        )
        real = nums[0] * nums[2] - nums[1] * nums[3]
        imag = nums[0] * nums[3] + nums[2] * nums[1]
        return f"{real}+ i{imag}"

    elif choice == "4":
        nums = list(
            map(
                int,
                input(
                    "Enter all numbers separated by space maximum 4 elements: "
                ).split(),
            )
        )
        real = (nums[0] * nums[2] + nums[1] * nums[3]) / (nums[2] ** 2 + nums[3] ** 2)
        imag = (nums[1] * nums[2] - nums[0] * nums[3]) / (nums[2] ** 2 + nums[3] ** 2)
        return f"{real}+ i{imag}"
def binomial(num):
    result = factorial(num[0]) / (factorial(num[1]) * factorial(num[0] - num[1]))
    return result
c = 0
while c != "-1":
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")
    print("Enter '6' for factorial")
    print("Enter '7' for complex arithmetic")
    print("ENter '8'  for binomial")
    print("Enter '-1' to exit.\n")
    c = input("Your choice is: ")
    if c == "1":
        res = addition()
    elif c == "2":
        res = subtraction()
    elif c == "3":
        res = multiplication()
    elif c == "4":
        res = division()
        if res == "Invalid entry":
            continue
    elif c == "5":
        res = average()
    elif c == "6":
        num = int(input("enter the number: "))
        if num < 0:
            print("Invalid entry")
            continue
        res = factorial(num)
    elif c == "7":
        os.system("cls||clear")
        res = complex_arithmetic()
    elif c == "8":
        num = list(map(int, input("Enter the number separated by space").split()))
        if num[0] < num[1]:
            print("Invalid entry")
            continue
        res = binomial(num)
    elif c == "-1":
        print("Thank you for using the calculator!")
        break
    else:
        print("Sorry, invalid option!")
    os.system("cls||clear")
    print(f"The answer is {res}")
    time.sleep(2)
    os.system("cls||clear")
