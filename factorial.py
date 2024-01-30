from math import factorial


class Factorial:
   def __init__(self, num):
      self.num=num

   def factorial(self,num):
      """
      Calculate n!. n! = 1 * 2 * 3 * … * (n-1) * n,  0! = 1. n >= 0.
      """
      if num == 0:
        return 1
      factor=1
      for i in range(1, num+1):
        factor=factor*i
      return factor


def main():

    factor=Factorial(int(input()))
    print(factor.factorial(factor.num))

if __name__ == "__main__":
    main()