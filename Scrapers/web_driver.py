from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class web_driver:
  def __init__(self):
    options = Options()
    # options.add_argument("--headless=new")
    options.page_load_strategy = 'normal'
    self.driver = webdriver.Firefox(options=options)
    
  
  def get_driver(self):
    return self.driver
  
search = input("Please enter the item you want to search for: ")
driver_instance = web_driver().get_driver()
    
  
  