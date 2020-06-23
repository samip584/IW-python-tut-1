def sum(d):
  summ = 0
  for key, value in d.items():
    summ += d[key]
  return summ


def main():
  dict = {1:1,2:2, 3:3, 4:5, 6:7, 8:9}
  print(sum(dict))
  

if __name__ == "__main__":
  main()