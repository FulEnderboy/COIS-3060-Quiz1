print('Library Catalog')
print('=' * 50)

with open('books.txt', 'r') as f:
    for line in f:
        print(line.strip())