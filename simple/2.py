def get_str(string):
  if len(string)< 2:
    return("Empty String")
  else: 
    string_to_show = string[:2] + string[-2:]
    return(string_to_show)

def main():
  string = input()
  print(get_str(string))


if __name__ == "__main__":
    main()
