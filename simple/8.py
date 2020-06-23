def return_removed(word, index):
  return(word[:index-1]+word[index:])

def main():
  word = (input("Enter word: "))
  index =int(input("Enter index: "))
  print(return_removed(word,index))

if __name__ == "__main__":
    main()