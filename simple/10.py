def trump_str(string):
  temp = ''
  for i in range(len(string)):
    if i%2 == 0:
      temp = temp + string[i]
  return(temp)

def main():
  string = input()
  print(trump_str(string))

if __name__ == "__main__":
    main()