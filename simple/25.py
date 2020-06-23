def is_emplty(list):
  for dict in list:
    if dict:
      return False
  return True


def main():
  print(is_emplty([{},{},{}]))
  print(is_emplty([{1,2},{},{}]))

if __name__ == "__main__":
    main()
