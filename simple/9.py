def change_str(string):
  return(string[-1:]+string[1:len(string)-1]+string[0])

def main():
  string = input()
  print(change_str(string))

if __name__ == "__main__":
    main()