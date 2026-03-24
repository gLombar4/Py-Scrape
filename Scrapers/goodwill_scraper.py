from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Scrapers.web_driver import driver_instance as driver
from Scrapers.web_driver import search

import time

class goodwill_scraper:
    def find_listings(): 
        print("Navigating to shopgoodwill...")  
        goodwill_sanitized = search.strip().replace(" ", "%20") 

        driver.get(f"https://shopgoodwill.com/categories/listing?st={goodwill_sanitized}&sg=&c=&s=&lp=0&hp=999999&sbn=&spo=false&snpo=false&socs=false&sd=false&sca=false&caed=3%2F6%2F2026&cadb=7&scs=false&sis=false&col=1&p=1&ps=40&desc=false&ss=0&UseBuyerPrefs=true&sus=false&cln=1&catIds=&pn=&wc=false&mci=false&hmt=false&layout=grid&ihp=true")
        wait = WebDriverWait(driver, 10)

        try:
            main_content = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.p-grid.p-nogutter.grid.grid-nogutter"))
            )
        except:
            print("Searched for listings for 10s and could not find any for Goodwill.")
            return
        
        divList = wait.until(
        lambda driver: main_content.find_elements(By.TAG_NAME, "div")
        )
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
            time.sleep(2) # A brief sleep is often necessary for the content to render
            new_height = driver.execute_script("return document.body.scrollHeight / 2")
            if new_height == last_height:
                break # If heights are the same, we've reached the bottom
            last_height = new_height

        

        print("Listings loaded")

        listings = {}
        dolls = 1
        for i in range(0, len(divList)):
            divList = wait.until(
                lambda driver: main_content.find_elements(By.TAG_NAME, "div")
            )
            if dolls == 11:
                break
            if(divList[i].get_attribute("class") == "p-col-12 item-col p-md-4 ng-star-inserted"):

                doll = divList[i]
                text = doll.find_element(By.CSS_SELECTOR, "a.feat-item_name.ng-star-inserted").text

                link = doll.find_element(By.CSS_SELECTOR, "a.feat-item_name.ng-star-inserted").get_attribute("href")
                link = link.replace("\\", "/")

                price = doll.find_element(By.CSS_SELECTOR, "p.feat-item_price").text

                img = doll.find_element(By.TAG_NAME, "img").get_attribute("src")

                listings.update({text: [price, link, img]})
                print(f'\rFound info for item: {dolls}', end='', flush=True)
                dolls += 1
                if(dolls == 11):
                    break

        driver.quit()
        print("\nListings for goodwill found")                   
        return listings
    
    listings = find_listings()

