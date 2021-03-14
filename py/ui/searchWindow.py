import tkinter as tk

class SearchWindow:
    def __init__(self):
        #   Set up mainWindow.
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Search Library Catalogue")

        #   Create frames.
        self.searchFrame = tk.Frame(self.mainWindow)
        self.resultsFrame = tk.Frame(self.mainWindow)
        self.resultsLabelRow = tk.Frame(self.resultsFrame)
        
        #   Initialize search variables.
        self.searchOption = tk.IntVar()
        self.searchOption.set(0)
        self.searchEntry = tk.StringVar()

        self.createSearchFrameWidgets()
        self.packSearchFrameWidgets()

        self.resultsTitleLabel = tk.Label(self.resultsLabelRow, text = "Title\t\t\t\t")
        self.resultsAuthorLabel = tk.Label(self.resultsLabelRow, text = "Author\t\t\t")
        self.resultsNumCopiesLabel = tk.Label(self.resultsLabelRow, text = "Number of Copies Available")
        
        self.resultsTitleLabel.pack(side = "left")
        self.resultsAuthorLabel.pack(side = "left")
        self.resultsNumCopiesLabel.pack(side = "left")

        #   Pack frames.
        self.searchFrame.pack()
        self.resultsLabelRow.pack()
        self.resultsFrame.pack()

        tk.mainloop()

    def createSearchFrameWidgets(self):
        self.searchLabel = tk.Label(self.searchFrame, text = "Search by")
        self.searchTitleRb = tk.Radiobutton(self.searchFrame, text = "Title", 
                                                variable = self.searchOption, value = 0)
        self.searchAuthorRb = tk.Radiobutton(self.searchFrame, text = "Author", 
                                                variable = self.searchOption, value = 1)
        self.searchBox = tk.Entry(self.searchFrame, width = 10, textvariable = self.searchEntry)
        self.searchButton = tk.Button(self.searchFrame, text = "Search", command = self.search)

    def packSearchFrameWidgets(self):
        self.searchLabel.pack(side = "left")
        self.searchTitleRb.pack(side = "left")
        self.searchAuthorRb.pack(side = "left")
        self.searchBox.pack(side = "left")
        self.searchButton.pack(side = "left")

    def search(self):
        print(str(self.searchEntry))