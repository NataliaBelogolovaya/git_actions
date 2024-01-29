def factorial(num):
  """
  Calculate n!. n! = 1 * 2 * 3 * … * (n-1) * n,  0! = 1. n >= 0.
  """
  if num == 0:
    return 1
  factor=1
  for i in range(1,num+1):
    factor=factor*i
  return factor

def main():
    n = int(input())
    print(factorial(n))

if __name__ == "__main__":
    main()