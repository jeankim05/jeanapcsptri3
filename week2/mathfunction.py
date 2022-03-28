def findthegreatestcommondenominator(firstnumber, secondnumber):
  
    if firstnumber == 0:
      
        return firstnumber
      
    while secondnumber != 0:
      
        if firstnumber > secondnumber:
          
            firstnumber = firstnumber - secondnumber
          
        else:
          
            secondnumber = secondnumber - firstnumber
          
    return firstnumber

class greatestcommondenominator:
  
  def __init__(value,number1,number2):
    
    value.number1 = number1
    
    value.number2 = number2
    
  def __class__(value):
    
    if number1 == 0:
      
      value.number1 = number1
      
    if number1 > number2:
      
      value.number1 = number1 - number2
      
    if number2 > number1:
      
      value.number2 = number2 - number1
      
    return number1
           
def greatestcommondenominator():
  
    a = int(input("Enter the first number to find the greatest common denominator: "))
  
    b = int(input("Enter a second number to find the greatest common denominator: "))
  
    greatestcommondenominator = findthegreatestcommondenominator(a, b)
  
    print("The greatest common denominator of {0} and {1} is: {2}".format(a, b, greatestcommondenominator))
  
    print()