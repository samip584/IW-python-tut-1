def add_to_str(string):
  if len(string)< 3:
    return(string)
  elif string[-3:].lower() == 'ing':
    return(string + 'ly')
  else:
    return(string+'ing')
    
def main():
  string = input()
  print(add_to_str(string))

if __name__ == "__main__":
    main()