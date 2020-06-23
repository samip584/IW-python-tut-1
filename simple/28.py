def add(dict, key, value):
  dict[key] = value
  return(dict)

def main():
  dict = {0: 10, 1: 20}
  print(add(dict, 2, 30))
  

if __name__ == "__main__":
  main()
