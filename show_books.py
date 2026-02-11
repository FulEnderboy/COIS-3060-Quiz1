print('Library Catalog')
print('=' * 50)

with open('books.txt', 'r') as f:
    if f.readline() == "":
        print("The catalog is empty. Add some books!")
    for line in f:
        print(line.strip())