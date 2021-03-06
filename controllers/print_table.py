from tkinter import *
from pandastable import Table, TableModel
from ml_test import n

class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Table app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            df = n.head(10)
            print(df.shape)
            self.table = pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
            pt.show()
            return

app = TestApp()

app.mainloop()
