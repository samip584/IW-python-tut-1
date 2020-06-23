def get_cases(string):
  return(string.upper(), string.lower())

def main():
  string = input()
  print(get_cases(string))

if __name__ == "__main__":
    main()