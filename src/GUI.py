import tkinter as tk
from tkinter import font 
from calendarTides import createCalendar
from datetime import datetime
from PIL import Image

def parseAndCreateCalendar(month, year, fileName):
    monthNum, datetime_month, yearNum = None, None, None # Get month and year based on what was inputted
    if (month==""): # If no month given, use current month
        month = datetime.strftime(datetime.today(), "%B")
        monthNum = datetime.today().month
    else:
        datetime_month = datetime.strptime(month, "%B")
        monthNum = datetime_month.month

    if (year==""):
        yearNum = datetime.today().year
    else:
        yearNum = int(year)

    if (fileName==""): # Update file path if none given
        fileName = month + " Calendar Tide Chart"
    
    if (fileName[-4:-1]!=".png"):
        fileName += ".png"
    
    createCalendar(monthNum, yearNum, fileName) 
    image = Image.open(fileName) # Open file 
    image.show()


def setupGUI(root):
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    appFont = font.Font(family="Oxygen", size=10, weight="bold") # TODO make sure others can get this font
    appFontLarge = font.Font(family="Oxygen", size=20, weight="bold")

    label = tk.Label(
        text="Tide Window Calendar Generator",
        fg="black",  # Set the text color to white
        bg="gray",  # Set the background color to black
        font = appFontLarge,
    ).grid(row=0, column=0, sticky='nsew', columnspan=2)

    monthEntryLabel = tk.Label(text="Please Enter Month (default is current month): ", bg="gray", fg="black", font=appFont)
    monthEntryLabel.grid(row=1, column=0, sticky='nsew', ipadx=10, ipady=10, padx=10, pady=10)
    monthEntry = tk.Entry(root, justify='center', font=appFont)
    monthEntry.grid(row=1, column=1, sticky='nsew', ipadx=10, ipady=10, padx=10, pady=10)

    filePathLabel = tk.Label(text="File Path (default is Month Calendar Tides.png): ", bg="gray", fg="black", font=appFont)
    filePathLabel.grid(row=2, column=0, sticky='nsew', ipadx=10, ipady=10, padx=10, pady=10)
    filePathEntry = tk.Entry(root, justify='center', font=appFont)
    filePathEntry.grid(row=2, column=1, sticky='nsew', ipadx=10, ipady=10,  padx=10, pady=10)

    yearLabel = tk.Label(text="Please Enter Year (default is current year): ", bg="gray", fg="black", font=appFont)
    yearLabel.grid(row=3, column=0, sticky='nsew', ipadx=10, ipady=10, padx=10, pady=10)
    yearEntry = tk.Entry(root, justify='center', font=appFont)
    yearEntry.grid(row=3, column=1, sticky='nsew', ipadx=10, ipady=10, padx=10, pady=10)

    generateButton = tk.Button(
        text="Generate",
        relief=tk.RAISED,
        borderwidth=1,
        width=25,
        height=5,
        bg="gray",
        fg="black",
        font=appFont,
        command=lambda: parseAndCreateCalendar(monthEntry.get(), yearEntry.get(), filePathEntry.get())
    ).grid(row=4, column=0, columnspan=2, sticky='ns', ipadx=10, ipady=10, padx=10, pady=10)

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("700x500")
    root.title("Calendar Tide Window Generator")

    setupGUI(root)

    # Configure the grid layout for the root window
    root.mainloop