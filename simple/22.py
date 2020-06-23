def remove_dup(list):
  temp = []
  for element in list:
    if element not in temp:
      temp.append(element)
  return(temp)

def main():
  print(remove_dup(["samip", "pratik", "someone", "samip", "pratik"]))

if __name__ == "__main__":
    main()
