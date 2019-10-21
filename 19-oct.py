'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def checkAddition(numbers, k):
  for (i, number1) in enumerate(numbers):
    for (j, number2) in enumerate(numbers):
      if (j != 0):   
        if number1 + number2 == k:
          return True
    numbers = numbers[1:]
  return False

print(checkAddition([10, 15, 3, 7], 25))
