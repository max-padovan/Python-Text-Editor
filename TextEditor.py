import tkinter as tk
from tkinter import ttk

barHeight = 150
bottomBarHeight = 25
pageWidth = 900

def on_configure(event):
    # Update the position of frame whenever the window is resized
    window.update_idletasks() #This ensures that all current tasks are completed before retriving window height
    pageFrame.place_configure(rely      = (barHeight / window.winfo_height()),
                              relheight = (1 - (barHeight + bottomBarHeight) / window.winfo_height()))
    
    bottomFrame.place_configure(rely      = (1 - bottomBarHeight / window.winfo_height()),
                                relheight = (bottomBarHeight / window.winfo_height()))

window = tk.Tk()
window.title("Text Editor")
window.geometry("1280x720")

barFrame = ttk.Frame(window, borderwidth = 1, relief = tk.GROOVE)
barFrame.place(relx      = 0,
               rely      = 0,
               relwidth  = 1,
               relheight = (barHeight / window.winfo_height()))

pageFrame = ttk.Frame(window, borderwidth = 1, relief = tk.GROOVE)
pageFrame.place(relx      = 0,
                rely      = (barHeight / window.winfo_height()),
                relwidth  = 1,
                relheight = (1 - (barHeight + bottomBarHeight) / window.winfo_height()))

#Add scrolling pages, search for scrolling in tkinter on youtube
pageCanvas = tk.Canvas(pageFrame, width = pageWidth, height = 300, bg = "#FFFFFF")
pageCanvas.place(relx = 0.5, rely = 0, anchor = "n")


pageFrame.grid_rowconfigure(0, weight = 1)
pageFrame.grid_columnconfigure(0, weight = 1)

VscrollBar = ttk.Scrollbar(pageFrame, orient = "vertical")
VscrollBar.grid(row = 0, column = 1, sticky = "ns")

HscrollBar = ttk.Scrollbar(pageFrame, orient = "horizontal")
HscrollBar.grid(row = 1, column = 0, sticky = "ew")



bottomFrame = ttk.Frame(window, borderwidth = 1, relief = tk.GROOVE)
bottomFrame.place(relx      = 0,
                  rely      = 1,
                  relwidth  = 1,
                  relheight = (bottomBarHeight / window.winfo_height()))

window.bind("<Configure>", on_configure)
window.mainloop()