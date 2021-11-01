print("Exercise 1")
def get_narcissistic_numbers():
  count = 0
  current_number = 1
  while (count < 20):
    if is_narcissistic(current_number):
      count += 1
      print(current_number)
    current_number += 1
  print("Astalabista")
 
  
def is_narcissistic(number):
  original_number = number
  digit_length = count_digits(number)
  number_sum = 0
  while (number != 0):
    last_digit = number % 10
    number = number // 10
    number_sum += last_digit ** digit_length

  if (number_sum == original_number):
    return True
  else:
    return False


def count_digits(number):
  number_of_digits = 0
  while (number != 0):
    number = number // 10
    number_of_digits += 1
  
  return number_of_digits


get_narcissistic_numbers()




print("Exercise 2")
def prime_number_printer():
  counter = 0
  for i in range(1, 1000):
    if check_prime(i) == True:
      counter = counter + 1
      if  counter % 20 == 0:
        print(i)
      else: 
        print(i, " ", end='')
        
     # print(" ")


def check_prime(y):
  if y == 1:
    return False

  limit = range(2, y)
  for i in limit:
    if y % i == 0:
      return False
  return True
  

prime_number_printer()
#check_prime(1)


print("Exercise 3")
def com_divisor():
  x = int(input("Enter a postive integer: "))
  y = int(input("Enter another positive integer: "))

  gcd = 0
  smaller = x if y > x else y

  for i in range(1, smaller+1):
    if ((x%i == 0) and (y%i == 0)):
      gcd = i

  print("The Greatest Common Divisor is", gcd)

com_divisor()


print("Exercise 4")
import math

def sin_func():
  number = int(input("Enter a number in degrees: "))
  print(taylor(number))

def factorial(number):
  if number == 1:
    return 1
  else:
    return number * factorial(number-1)

def taylor(number):
  summation = 0
  number = math.radians(number)
  for n in range(16):
    summation += ((-1)**n/factorial(2*n + 1)) * number**(2*n + 1)
  
  return summation



sin_func()






