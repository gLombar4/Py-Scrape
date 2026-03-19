import sys
import ctypes
from tkinter import *
from tkinter import ttk
from GUI.ebay_tab import EbayTabFrame
from GUI.goodwill_tab import GoodwillTabFrame

if 'win' in sys.platform: # Ensure this only runs on Windows
    ctypes.windll.shcore.SetProcessDpiAwareness(1) # Set DPI awareness

root= Tk()
root.title("MH Listings")

#notebook for tabs
book = ttk.Notebook(root)
book.pack(fill=BOTH, expand=True)


ebay_tab_frame = EbayTabFrame(book)
goodwill_tab_frame = GoodwillTabFrame(book)

book.add(ebay_tab_frame, text="Ebay")
book.add(goodwill_tab_frame, text="Goodwill")




root.mainloop()