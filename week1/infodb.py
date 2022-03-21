InfoDb = []
InfoDb.append({  
               "Name": "Jean",  
               "Grade": "Junior",  
               "Sport": "Basketball",   
               "TopClasses":["AP Stats", "AP Bio", "AP English"]  
              })
InfoDb.append({  
               "Name": "Connor",  
               "Grade": "Junior",  
               "Sport": "Football",   
               "TopClasses":["AP Calculus", "AP Physics", "AP Computer Science"]  
              }) 
InfoDb.append({  
               "Name": "Jun",  
               "Grade": "Junior",  
               "Sport": "Basketball",   
               "TopClasses":["AP Calculus", "AP Bio", "AP Computer Science"]  
              }) 
InfoDb.append({  
               "Name": "Aidan",  
               "Grade": "Sophomore",  
               "Sport": "Track",   
               "TopClasses":["AP Calculus", "AP Physics", "AP Computer Science"]  
              }) 
def print_data(n):
    print(InfoDb[n]["Name"], "is a ", InfoDb[n]["Grade"], "and loves", InfoDb[n]["Sport"])
    print("\t", "Top 3 Classes: ", end="")
    print(", ".join(InfoDb[n]["TopClasses"]))
    print("\t", "Favorite Class: ", end="")
    print(InfoDb[n].get("TopClasses")[0])
    print()
  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

def main():
  print("For loop")
  for_loop()
  print("While loop")
  while_loop(0)
  print("Recursive loop")
  recursive_loop(0)
