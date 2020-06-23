def joined_str(string1, string2):
  temp1 = string2[:2] + string1[2:]
  temp2 = string1[:2] + string2[2:]
  temp = temp1+ " "+ temp2
  return(temp)
  

def main():
  string1 = input()
  string2 = input()
  print(joined_str(string1, string2))

if __name__ == "__main__":
    main()