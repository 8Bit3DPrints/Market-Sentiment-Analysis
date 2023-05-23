import tkinter as tk
from holdings import Holdings

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('SPY Index Fund Holdings')

        self.holdings = Holdings()

        self.holdings_list = tk.Listbox(self.window, width=50)
        self.holdings_list.pack()

        button = tk.Button(self.window, text='Get Current Holdings', command=self.update_holdings)
button.pack(pady=10)

