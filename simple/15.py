def insaert(string1, string2):
  return(string1[:int(len(string1)/2)] + string2 + string1[int(len(string1)/2):])

def main():
  print(insaert('[[]]', 'Python'))
  print(insaert('{{}}', 'PHP'))

if __name__ == "__main__":
    main()
