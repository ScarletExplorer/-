# TODO Найдите количество книг, которое можно разместить на дискете
Pages = 100
lines = 50
symbols = 25
Memory_in_MB = 1.44
Memory_book_in_MB = ((symbols*lines*Pages)*4)/1024/1024
number_of_books = int(Memory_in_MB//Memory_book_in_MB)

print("Количество книг, помещающихся на дискету:", number_of_books)
