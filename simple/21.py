def get_list(list):
  list.sort(key = lambda x: x[-1:])
  return(list)

def main():
  print(get_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

if __name__ == "__main__":
    main()
