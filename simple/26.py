def insert(list, string):
  temp = []
  for element in list:
    temp.append(string + str(element))
  return temp

def main():
  list = [1,2,3,4]
  string = "emp"
  print(insert(list, string))
  

if __name__ == "__main__":
  main()
