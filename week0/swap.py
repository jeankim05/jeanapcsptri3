def swap():
    num1 = int(input("Enter your first number "))
    num2 = int(input("Enter your second number "))
    temp = num1
    num1 = num2
    num2 = temp
    print("Your numbers have been swapped!")
    print(f"Your first number is {num1}")
    print(f"Your second number is {num2}")

swap()