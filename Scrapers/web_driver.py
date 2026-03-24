from selenium import webdriver
from selenium.webdriver.firefox.options import Options
class web_driver:
  def __init__(self):
    print("Starting web browser...")
    options = Options()
    options.add_argument("--headless=new")
    options.page_load_strategy = 'normal'
    self.driver = webdriver.Firefox(options=options)
    print("Web browser session started.")
    
  
  def get_driver(self):
    return self.driver
  
search = input("Please enter the item you want to search for: ")
driver_instance = web_driver().get_driver()
    
  
  