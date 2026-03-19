import sys
from tkinter import *
from tkinter import ttk
import tkinter as tk
import ctypes
import webbrowser
from PIL import ImageTk
from urllib.request import urlopen

# from ebay_scraper import ebay_scraper
# from mercari_scraper import mercari_scraper

if 'win' in sys.platform: # Ensure this only runs on Windows
    ctypes.windll.shcore.SetProcessDpiAwareness(1) # Set DPI awareness

# ebay = ebay_scraper()

# ebay_listings = ebay.listings

# for key, value in ebay_listings.items():
#     print(f"Product: \n\t{key}\nPrice: \n\t{value[0]}\nLink:\n\t{value[1]}\n")

root= Tk()
root.title("MH Listings")

#notebook for tabs
book = ttk.Notebook(root)
book.pack(fill=BOTH, expand=1)

#outer frame for ebay
ebay_frame = Frame(book, bg="lightblue")
ebay_frame.pack(fill=BOTH, expand=True)

book.add(ebay_frame, text="Ebay")

#outer frame for mercari
mercari_frame = Frame(book, bg="lightblue")
mercari_frame.pack(fill=BOTH, expand=True)

book.add(mercari_frame, text="Mercari")



#canvas inside outer frame (side=LEFT very important)
canvas = Canvas(ebay_frame, bg="green")
canvas.pack(side=LEFT, fill=BOTH, expand=YES)


#place scrollbar inside ebay frame
scrollbar = Scrollbar(ebay_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

#inner frame for listings
frame = tk.Frame(canvas, bg="lightblue", padx=10, pady=10)

#put inner frame in canvas
canvas.create_window((0,0), window=frame, anchor=NW)


canvas.configure(yscrollcommand=scrollbar.set)
canvas.configure(scrollregion=canvas.bbox("all"))
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

for i in range(1,50):
    label_example = Label(frame, bg="blue", padx=10, pady=10)
    label_example.pack()



# image_list = []
# for key, value in ebay_listings.items():
    
#     # product_label = Label(frame, bg="lightblue", text=f"Product: \n{key}\nPrice: \n{value[0]}\nLink:\n{value[1]}")
#     product_label = Label(frame, bg='lightblue', text= f"Product: \n{key}\n")
#     product_label.pack()
    
#     price_label = Label(frame, bg='lightblue', text = f"Price: \n{value[0]}\n")
#     price_label.pack()
    
#     link_label = Label(frame, bg='lightblue', text = f"Link: \n{value[1]}", cursor='hand2', fg="blue")
#     link_label.pack()
#     link_label.bind("<Button-1>", lambda e, specific_url=f"{value[1]}": webbrowser.open_new(specific_url))
    
#     img = ImageTk.PhotoImage(file=urlopen(value[2]))
#     image_label = ttk.Label(frame, image=img)
#     image_label.pack(pady=50)
#     image_list.append(img)


root.mainloop()


