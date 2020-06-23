def concat(d1, d2, d3):
  d4 = dict(d1)
  d4.update(d2)
  d4.update(d3)
  return(d4)

def main():
  dic1={1:10, 2:20}
  dic2={3:30, 4:40}
  dic3={5:50,6:60}
  print(concat(dic1, dic2, dic3))
  

if __name__ == "__main__":
  main()
