def generatedic(num):
  dic ={}
  for i in range(1, num+1):
    dic[i] = i*i 
  return dic
def main():
  num = int(input())
  print(generatedic(num))
  

if __name__ == "__main__":
  main()