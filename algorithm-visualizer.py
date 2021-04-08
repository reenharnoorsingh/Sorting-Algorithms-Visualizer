# Sorting Algorithms Visualizer in Python
from tkinter import *  # importing tkinter
from tkinter import ttk
import random  # importing random to have a random set of values when visualized

# tkinter layout
root = Tk()
root.title('Sorting Algorithms Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

# base layout
user_frame = Frame(root, width=600, height=200, bg='grey')
user_frame.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()
