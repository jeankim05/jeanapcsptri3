class Factorial:
    def __init__(number):
        pass
    def __call__(number, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * number(n - 1)

def menu():
    num = int(input("Please enter a value for factorial: "))
    try:
        factorial_of = Factorial() # instantiate object while running the method from the factorial class
        print("Factorial value is", factorial_of(num))   # also prints the nth term
    except:
        print("Sorry, there was an error")   # no negative numbers