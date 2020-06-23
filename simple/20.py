def get_count(list):
  count = 0
  for element in list:
    if len(element) > 2:
      if element[0] == element[-1:]:
        count += 1
  return(count)

def main():
  print(get_count(['abc', 'xyz', 'aba', '1221']))

if __name__ == "__main__":
    main()
