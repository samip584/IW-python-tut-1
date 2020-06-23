def generatedic(num1, num2):
  dic ={}
  for i in range(num1, num2+1):
    dic[i] = i*i 
  return dic
def main():
  print(generatedic(1, 15))
  

if __name__ == "__main__":
  main()