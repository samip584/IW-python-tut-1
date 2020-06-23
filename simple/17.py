def prod(list):
  temp = 1
  for i in list:
    temp *= i
  return(temp)
def main():
  print(prod([1, 2, 3, 4, 5, 6]))

if __name__ == "__main__":
    main()
