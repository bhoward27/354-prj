import tkinter as tk

class SearchWindow:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Search Library Catalogue")

        self.searchFrame = tk.Frame(self.mainWindow)
        
        self.searchOption = tk.IntVar()
        self.searchOption.set(0)
        self.searchEntry = tk.StringVar()

        self.searchLabel = tk.Label(self.searchFrame, text = "Search by")
        self.searchTitleRb = tk.Radiobutton(self.searchFrame, text = "Title", 
                                                variable = self.searchOption, value = 0)
        self.searchAuthorRb = tk.Radiobutton(self.searchFrame, text = "Author", 
                                                variable = self.searchOption, value = 1)
        self.searchBox = tk.Entry(self.searchFrame, width = 10, textvariable = self.searchEntry)
        self.searchButton = tk.Button(self.searchFrame, text = "Search", command = self.search)

        self.searchLabel.pack(side = "left")
        self.searchTitleRb.pack(side = "left")
        self.searchAuthorRb.pack(side = "left")
        self.searchBox.pack(side = "left")
        self.searchButton.pack(side = "left")

        self.searchFrame.pack()

        tk.mainloop()

    def search(self):
        print(str(self.searchEntry))