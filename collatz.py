#   collatz.py
#   James Yoo
#   Created: October 31, 2017

def collatz(n):
  steps = 0
  while n > 0:
    if n == 1:
      return steps
    elif n % 2 == 0:
      n = n / 2
      steps += 1
    elif n % 2 == 1:
      n = (3 * n) + 1
      steps += 1
    else:
      print("Error\n")
