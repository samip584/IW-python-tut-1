def mul(d):
  prod = 1
  for key, value in d.items():
    prod *= d[key]
  return prod


def main():
  dict = {1:1,2:2, 3:3, 4:5, 6:7, 8:9}
  print(mul(dict))
  

if __name__ == "__main__":
  main()