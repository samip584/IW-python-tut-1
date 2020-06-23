def is_emplty(list):
  if list:
    return("not empty")
  else:
    return("empty")

def main():
  print(is_emplty([]))
  print(is_emplty(["samip", "pratik", "someone", "samip", "pratik"]))

if __name__ == "__main__":
    main()
