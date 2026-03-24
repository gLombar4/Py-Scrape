import sys
import ctypes
from tkinter import *
from tkinter import ttk
print("Welcome to listing finder V1.0")
from GUI.ebay_tab import EbayTabFrame
from GUI.goodwill_tab import GoodwillTabFrame

if 'win' in sys.platform: # Ensure this only runs on Windows
    ctypes.windll.shcore.SetProcessDpiAwareness(1) # Set DPI awareness

root= Tk()
root.title("Listings")

#notebook for tabs
book = ttk.Notebook(root)
book.pack(fill=BOTH, expand=True)
ebay_tab_frame = EbayTabFrame(book)
goodwill_tab_frame = GoodwillTabFrame(book)
print("All listings found, display being created...")

book.add(ebay_tab_frame, text="Ebay")
book.add(goodwill_tab_frame, text="Goodwill")




root.mainloop()