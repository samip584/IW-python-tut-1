def positive_vibe(string):
  first = "not"
  second = "poor"
  replace = "good"
  list = []
  d = 0
  for i in range(len(string)):
    if string[i] == ' ':
      list.append(string[d:i])
      d = i+1
  list.append(string[d:i+1])

  for i in range(len(list)):
    if list[i] == first:
      temp = string[i:]
      for j in range( len(temp)):
        if list[j] == second:
          temp_list = string[:i]
          temp.append(replace)
          for k in list[j:]:
            temp.append[k]
          break




def main():
  string = input()
  print(positive_vibe(string))

if __name__ == "__main__":
    main()