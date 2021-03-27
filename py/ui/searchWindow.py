import tkinter as tk

#   This class allows the user to search for books in the library catalogue by title or by author.
#   The constructor must be passed a list of Book objects.
class SearchWindow:
    def __init__(self, bookList):
        #   Set up mainWindow.
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Search Library Catalogue")

        #   Create frames.
        self.searchFrame = tk.Frame(self.mainWindow)
        self.resultsFrame = tk.Frame(self.mainWindow)
        self.resultsLabelRow = tk.Frame(self.resultsFrame)
        
        #   Initialize variables.
        self.searchOption = tk.IntVar()
        self.searchOption.set(0)
        self.searchEntry = tk.StringVar()
        self.bookList = bookList
        self.resultsRowWidth = 150
        
        self.createSearchFrameWidgets()
        self.packSearchFrameWidgets()

        self.resultsList = tk.Listbox(self.resultsFrame, height = 22, width = self.resultsRowWidth, 
                                        font = "Courier")
        self.resultsList.pack()

        #   Pack frames.
        self.searchFrame.pack()
        self.resultsFrame.pack()

        tk.mainloop()

    def createSearchFrameWidgets(self):
        self.searchLabel = tk.Label(self.searchFrame, text = "Search by")
        self.searchTitleRb = tk.Radiobutton(self.searchFrame, text = "Title", 
                                                variable = self.searchOption, value = 0)
        self.searchAuthorRb = tk.Radiobutton(self.searchFrame, text = "Author", 
                                                variable = self.searchOption, value = 1)
        self.searchBox = tk.Entry(self.searchFrame, width = 40, textvariable = self.searchEntry)
        self.searchButton = tk.Button(self.searchFrame, text = "Search", command = self.search)

    def packSearchFrameWidgets(self):
        self.searchLabel.pack(side = "left")
        self.searchTitleRb.pack(side = "left")
        self.searchAuthorRb.pack(side = "left")
        self.searchBox.pack(side = "left")
        self.searchButton.pack(side = "left")

    def createResultsLabelRowWidgets(self):
        self.resultsTitleLabel = tk.Label(self.resultsLabelRow, text = "Title\t\t\t\t")
        self.resultsAuthorLabel = tk.Label(self.resultsLabelRow, text = "Author\t\t\t")
        self.resultsNumCopiesLabel = tk.Label(self.resultsLabelRow, text = "Number of Copies Available")

    def packResultsLabelRowWidgets(self):
        self.resultsTitleLabel.pack(side = "left")
        self.resultsAuthorLabel.pack(side = "left")
        self.resultsNumCopiesLabel.pack(side = "left")

    def search(self):
        self.resultsList.delete(0, self.resultsList.size())
        self.copiesWidth = 18
        self.titleWidth = 80
        self.authorWidth = self.resultsRowWidth - self.copiesWidth - self.titleWidth

        title = "TITLE"
        title = title + (self.titleWidth - len(title)) * " "
        author = "AUTHOR"
        author = author + (self.authorWidth - len(author)) * " "
        self.resultsList.insert(1, title + author + "# COPIES AVAILABLE")
        self.resultsList.insert(2, "")

        searchEntry = self.searchEntry.get()
        if searchEntry == "":
            self.showNoResults()
        else:
            i = 3
            if self.searchOption.get() == 0:
                for book in self.bookList:
                    if searchEntry.lower() in book.title.lower():
                        self.insert(book, i)
                        i += 1
            elif self.searchOption.get() == 1:
                for book in self.bookList:
                    if searchEntry.lower() in book.author.lower():
                        self.insert(book, i)
                        i += 1

            if i == 3:
                self.showNoResults()
            
    def showNoResults(self):
        noResult = "No Search Results"
        numSpaces = (self.resultsRowWidth - len(noResult)) // 2
        space = numSpaces * " "
        self.resultsList.insert(3, space + noResult + space)

    def insert(self, book, i):
        title = book.title + (self.titleWidth - len(book.title)) * " "
        author = book.author + (self.authorWidth - len(book.author)) * " "
        self.resultsList.insert(i, title + author + str(book.numAvailableCopies))