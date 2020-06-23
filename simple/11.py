def give_count(string):
  list = []
  d = 1 #considering the last sentence does not have space
  for i in range(len(string)):
    if string[i] == ' ':
      d = d+1
  return(d)




def main():
  string = input()
  print(give_count(string))

if __name__ == "__main__":
    main()