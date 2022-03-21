def fibonaccisequence(n):
   if n <= 1:
       return n
   else:
       return(fibonaccisequence(n-1) + fibonaccisequence(n-2))
def display():
  terms = int(input("How many terms of the sequence do you want?"))
  try:
    print("Fibonacci sequence:")
    for i in range(terms):
      print(fibonaccisequence(i))
  except:
    terms <= 0
    print("Plese enter a positive integer")
  