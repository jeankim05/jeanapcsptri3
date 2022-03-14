import time
ans = True
while ans:
    print(“”"
    1. Ship Pattern
    2. Build a Christmas Tree
    3. Number Swap
    4. Exit/Quit
    “”")
    ans = input(“What would you like to do? “)
    def ocean_print():
      # print ocean
      print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
      print(“\n\n\n\n”)
      print(OCEAN_COLOR + ”  ” * 35)
    # print ship with colors and leading spaces
    def ship_print(position):
        print(ANSI_HOME_CURSOR)
        print(RESET_COLOR)
        sp = ” ” * position
        print(sp + ”    |\   “)
        print(sp + ”    |/   “)
        print(SHIP_COLOR, end=“”)
        print(sp + “\__ |__/ “)
        print(sp + ” \____/  “)
        print(RESET_COLOR)
    # ship function, iterface into this file
    def ship():
        # only need to print ocean once
        ocean_print()
        # loop control variables
        start = 0  # start at zero
        distance = 60  # how many times to repeat
        step = 2  # count by 2
        # loop purpose is to animate ship sailing
        for position in range(start, distance, step):
            ship_print(position)  # call to function with parameter
            time.sleep(.1)
    if ans==“1":
      ANSI_CLEAR_SCREEN = u”\u001B[2J”
      ANSI_HOME_CURSOR = u”\u001B[0;0H\u001B[2"
      OCEAN_COLOR = u”\u001B[44m\u001B[2D”
      SHIP_COLOR = u”\u001B[32m\u001B[2D”
      RESET_COLOR = u”\u001B[0m\u001B[2D”
      ship()
    elif ans==“2”:
      def triangleShape(n):
        for i in range(n):
            for j in range(n-i):
                print(’ ‘, end=’ ‘)
            for k in range(2*i+1):
                print(‘*’,end=' ‘)
            print()
    # Generating Pole Shape
      def poleShape(n):
        for i in range(n):
            for j in range(n-1):
                print(’ ‘, end=’ ‘)
            print(‘* * *’)
    # Input and Function Call
      row = int(input(‘Enter number of rows: ’))
      triangleShape(row)
      triangleShape(row)
      poleShape(row)
    elif ans==“3":
      import random
      age1 = float(input(“Choose first age: “))
      age2 = float(input(“Choose second age: “))
      if age1 < age2:
          print(age1, age2)
      else:
          print(age2, age1)
    else:
      ans = False
      print(“See you later!“)