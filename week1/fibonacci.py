def fibonaccisequence(n):
   if n <= 1:
       return n
   else:
       return(fibonaccisequence(n-1) + fibonaccisequence(n-2))
def display():
  terms = int(input("How many terms do you want in your sequence?"))
  try:
    print("Complete Fibonacci Sequence:")
    for i in range(terms):
      print(fibonaccisequence(i))
  except:
    terms <= 0
    print("Please enter a positive number!")
  