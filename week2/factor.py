class factor:
  
  def findTheFactors(value, number):
    
    print("OOP Factors of {0} are:".format(number))
    
    for value in range(1, number + 1):
      
      if number % value == 0:
        
        print("{0}".format(value), end=" ")
        
    print()

def factorsmenu():
  
  print("Hello user")
  
  num = int(input("Enter a value for its factors: "))
  
  findTheFactors(num)
  
  mat = factor()
  
  mat.findTheFactors(num)
  

def findTheFactors(number):
  
  print("Imp Factors of {0} are:".format(number))
  
  for value in range(1, number + 1):
    
    if number % value == 0:
      
      print("{0}".format(value), end=" ")
      
  print()