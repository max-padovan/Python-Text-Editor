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
pageCanvas = tk.Canvas(pageFrame, bg = "#FFFFFF", scrollregion = (0, 0, 1000, 3508), width = 1000, height = 1000)
pageCanvas.create_line(0, 0, 1000, 3508, fill = 'green', width = 10)

pageCanvas.xview_moveto(0)
pageCanvas.yview_moveto(0)




pageCanvas.place(relx = 0.5, rely = 0, anchor = 'n')


VscrollBar = ttk.Scrollbar(pageFrame, orient = "vertical", command = pageCanvas.yview)
pageCanvas.configure(yscrollcommand = VscrollBar.set)
VscrollBar.place(relx = 1, relheight = 1, anchor = "ne")

HscrollBar = ttk.Scrollbar(pageFrame, orient = "horizontal", command = pageCanvas.xview)
pageCanvas.configure(xscrollcommand = HscrollBar.set)
HscrollBar.place(relx = 0, rely = 1, relwidth = 1, anchor = "sw")



bottomFrame = ttk.Frame(window, borderwidth = 1, relief = tk.GROOVE)
bottomFrame.place(relx      = 0,
                  rely      = 1,
                  relwidth  = 1,
                  relheight = (bottomBarHeight / window.winfo_height()))

window.bind("<Configure>", on_configure)
window.mainloop()