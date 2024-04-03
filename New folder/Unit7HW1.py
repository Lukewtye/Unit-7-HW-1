'''
Name: Luke Tye
Date: 3/19/24
Assignment: Unit 7 HW 1
'''

from pathlib import Path
def problem_1():
    path = Path("my_learning.txt")
    contents = path.read_text()
    print(contents) #Print the whole file

    lines = contents.splitlines()#Print one line at a time
    for line in lines:
        print(line)

def problem_2():
    path = Path("my_learning.txt")
    contents = path.read_text()
    csharpversion = contents.replace('Python', 'c-sharp')
    print (csharpversion)
    
def problem_3():
    #Reading line by line
  path = Path('pi_digits.txt')
  contents = path.read_text()

  for line in contents.splitlines():
    print(line)

  pi_string = ''
  for line in contents.splitlines():
    pi_string += line.lstrip()
  print(pi_string)
  print(f"This is pi to {len(pi_string)-2} decimal places")

  #ASk a user for their birthday in mmddyy form
  #Tell them if their birthday is in pi_string or not  

  try:
    birthday = (input("what is your birthday in mmddyy form with no slashes"))
  except ValueError:
    ("Incorrect form")
  path = Path('million_digits_pi.txt')
  contents = path.read_text()
  if str(birthday) in contents:
    print("Your birthday is in the file!")
  else:
    print("Your birthday is not in the file.")



if __name__ == '__main__':
    problem_1()
    problem_2()
    problem_3()