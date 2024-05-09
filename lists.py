shopping = ['eggs', 'avocados', 'soda']
amount = [12, 5, 1,'eggs', 'avocados', 'soda']

print(shopping)
print(amount[4])
print(amount[-3])

todolist = ['get quarters', 'do laundry', 'take a walk','get a haircut','make some tea','complete lists chapter','call mom','watch my hero academia']
print(todolist[0], todolist[1])
print(todolist[3:6])

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]
print(min(lego_parts))
print(max(lego_parts))

books = ['zero to one', 'the lean startup', 'the mom test', 'make it stick', 'life in code']
# methods
books.append('zero to sold')
books.remove('the lean startup')
books.pop(0)
books.sort()
# print(books)

for i in range(len(books)):
  print(books[i])