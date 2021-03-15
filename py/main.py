from model.book import Book
from ui.searchWindow import SearchWindow

def main():
    twoDBookList = [ 
                    ["Harry Potter and the Philosopher's Stone", "J. K. Rowling", 2],
                    ["Harry Potter and the Chamber of Secrets", "J. K. Rowling", 5],
                    ["Harry Potter and the Prisoner of Azkaban", "J. K. Rowling", 1],
                    ["Harry Potter and the Goblet of Fire", "J. K. Rowling", 6],
                    ["Harry Potter and the Order of the Phoenix", "J. K. Rowling", 2],
                    ["Harry Potter and the Half-Blood Prince", "J. K. Rowling", 0],
                    ["Harry Potter and the Deathly Hallows", "J. K. Rowling", 3],

                    ["The Hobbit", "J. R. R. Tolkien", 4],
                    ["The Lord of the Rings Part I: The Fellowship of the Ring", "J. R. R. Tolkien",
                        1],
                    ["The Lord of the Rings Part II: The Two Towers", "J. R. R. Tolkien", 5],
                    ["The Lord of the Rings Part III: The Return of the King", "J. R. R. Tolkien",
                        7]
    ]
    bookList = []
    for book in twoDBookList:
        bookList.append(Book(book))

    for book in bookList:
        print("Title:", book.title)
        print("Author:", book.author)
        print("Number of Copies Available:", book.numAvailableCopies)
        print()

    window = SearchWindow(bookList)                

main()