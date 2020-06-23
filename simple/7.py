def return_longest(words):
  return(max(len(word) for word in words))

def main():
  words = ["hey", "their", "you"]
  print(return_longest(words))

if __name__ == "__main__":
    main()