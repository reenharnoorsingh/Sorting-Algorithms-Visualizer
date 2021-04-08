# Sorting Algorithms Visualizer in Python
from tkinter import *  # importing tkinter
from tkinter import ttk
import random  # importing random to have a random set of values when visualized

# tkinter layout
tkinterRoot = Tk()
tkinterRoot.title('Sorting Algorithms Visualizer')
tkinterRoot.maxsize(900, 600)
tkinterRoot.config(bg='black')

# base layout
user_frame = Frame(tkinterRoot, width=600, height=200, bg='grey')   #frame is used to organize layout
user_frame.grid(row=0, column=0, padx=10, pady=5)   #adds padding etc

user_canvas = Canvas(tkinterRoot, width=600, height=380, bg='white') #canvas is used to draw graphs or plots
user_canvas.grid(row=1, column=0, padx=10, pady=5)

#User Area
#Label(user_frame, text="Algorithm: ")

#runs the tkinter code and compiles it
tkinterRoot.mainloop()
