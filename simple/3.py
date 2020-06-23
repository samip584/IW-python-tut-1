def convert_str(string):
  first = string[0]
  temp = first
  for i in range(1, len(string)):
    if string[i] == first:
      temp = temp + '$'
    else:
      temp = temp + string[i]
  return(temp)

def main():
  string = input()
  print(convert_str(string))

if __name__ == "__main__":
    main()