def is_in(dic, key):
  if key in dic:
    return "already exists"
  else:
    return "does not exists"

def main():
  dic={"name":"samip", "age":21}
  print(is_in(dic, "hair"))
  print(is_in(dic, "name"))
  

if __name__ == "__main__":
  main()