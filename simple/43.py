def removefrom(tup, element): 
  my_list = list(tup)
  my_list.remove(element)
  return tuple(my_list) 
  
def main():
  tup = (1, 2, 3, 4) 
  print(removefrom(tup, 2)) 

if __name__ == "__main__":
  main()