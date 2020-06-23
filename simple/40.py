def add(tup):
  temp = 0
  for t in tup:
    temp += t
  return(temp)

def main():
  tuplex = (4, 8, 3) 
  print(add(tuplex))
  

if __name__ == "__main__":
  main()