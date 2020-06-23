def character_count(string):
  str_cnt = {}
  for letter in string:
    if letter not in str_cnt:
      str_cnt[letter] = 1
    else:
      str_cnt[letter] =  str_cnt[letter] + 1
  return(str_cnt)
  
def main():
    string = input()
    print(character_count(string))

if __name__ == "__maisn__":
    main()
