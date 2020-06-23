def add_tags(tag, content):
  return('<'+tag+'>'+content+'</'+tag+'>')

def main():
  print(add_tags('i', 'Python'))

if __name__ == "__main__":
    main()
