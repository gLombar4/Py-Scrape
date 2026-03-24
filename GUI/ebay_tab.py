import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import *
from PIL import ImageTk
from Scrapers.ebay_scraper import ebay_scraper
from urllib.request import urlopen


class EbayTabFrame(tk.Frame):
  def __init__(self, parent, controller=None,):
      super().__init__(parent)
  
      #canvas inside outer frame (side=LEFT very important)
      canvas = Canvas(self, yscrollincrement=100)
      canvas.pack(side=LEFT, fill=BOTH, expand=YES)


      #place scrollbar inside ebay frame
      scrollbar = Scrollbar(self, orient=VERTICAL, command=canvas.yview, jump=True)
      scrollbar.pack(side=RIGHT, fill=Y)

      #inner frame for listings
      frame = tk.Frame(canvas, padx=10, pady=10)

      #put inner frame in canvas
      canvas.create_window((0,0), window=frame, anchor=NW)


      canvas.configure(yscrollcommand=scrollbar.set)
      canvas.configure(scrollregion=canvas.bbox("all"))
      canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
      
      
      ebay_listings = ebay_scraper.listings
      image_list = []
      for key, value in ebay_listings.items():
          
          product_label = Label(frame, text= f"Product: \n{key}\n")
          product_label.pack()
          
          price_label = Label(frame, text = f"Price: \n{value[0]}\n")
          price_label.pack()
          
          link_label = Label(frame, text = "Click here for link", cursor='hand2', fg="blue")
          link_label.pack()
          link_label.bind("<Button-1>", lambda e, specific_url=f"{value[1]}": webbrowser.open_new(specific_url))
        #   url = value[2]
          img = ImageTk.PhotoImage(file=urlopen(value[2]))
          image_label = ttk.Label(frame, image=img)
          image_label.image = img
          image_label.pack(pady=50)
          image_list.append(img)
