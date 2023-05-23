import tkinter as tk
from holdings import update_holdings

# Create the GUI window
window = tk.Tk()
window.title('SPY Index Fund Holdings')

# Create a listbox to display the holdings
holdings_list = tk.Listbox(window, width=50)
holdings_list.pack()

# Create a button to fetch the holdings
button = tk.Button(window, text='Get Current Holdings', command=lambda: update_holdings(holdings_list))
button.pack(pady=10)

# Start the GUI event loop
window.mainloop()