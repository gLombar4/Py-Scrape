from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Scrapers.web_driver import driver_instance as driver
from Scrapers.web_driver import search
import pyshorteners
import time


class ebay_scraper:    
    
    # returns a dictionary of the top search results for "Monster High Dolls" on ebay
    def find_listings():
        print("Navigating to ebay...")
        ebay_sanitized = search.strip().replace(" ", "+")
        driver.get(f"https://www.ebay.com/sch/i.html?_nkw={ebay_sanitized}&_sacat=0&_from=R40&_trksid=m570.l1313")
        wait = WebDriverWait(driver, 3600)
        
        main_content = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.srp-results.srp-list.clearfix"))
        )
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
        # Scroll down to the bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
                # Wait to load the new content
                time.sleep(2) # A brief sleep is often necessary for the content to render

                # Calculate new scroll height and compare with the last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight / 2")
                if new_height == last_height:
                        break # If heights are the same, we've reached the bottom
                last_height = new_height

        # All content should now be loaded, proceed with scraping/interaction
        
        listings = {}
        
        shortener = pyshorteners.Shortener()
        
        
        for i in range(1, 11):
                current_doll = wait.until(
                        lambda driver:  main_content.find_element(By.CSS_SELECTOR, f'[data-view="mi:1686|iid:{i}"]')
                )
                # current_doll = main_content.find_element(By.CSS_SELECTOR, f'[data-view="mi:1686|iid:{i}"]')
                
                text = (current_doll.find_element
                        (By.CSS_SELECTOR, 
                         ("div.su-card-container__content > " +
                          "div.su-card-container__header > " + 
                          "a.s-card__link > " + 
                          "div.s-card__title > " + 
                          "span.su-styled-text.primary.default"))
                        .text)
                print("Found text")
                
                price = (current_doll.find_element
                         (By.CSS_SELECTOR, 
                          ("div.su-card-container__content > " + 
                           "div.su-card-container__attributes.su-card-container__attributes--has-secondary > " + 
                           "div.su-card-container__attributes__primary > " + 
                           "div.s-card__attribute-row > " + 
                           "span.su-styled-text.primary.bold.large-1.s-card__price"))
                         .text)
                print("Found price")
                
                link = (current_doll.find_element
                        (By.CSS_SELECTOR, 
                         ("div.su-card-container.su-card-container--horizontal > " +
                          "div.su-card-container__content > " + 
                          "div.su-card-container__header > " +
                          "a.s-card__link"))
                        .get_attribute("href"))
                print("Found link")
                
                # img = (current_doll.find_element
                #        (By.CSS_SELECTOR, 
                #         ("div.su-card-container__media > " + 
                #          "div.s-card__media-wrapper > " +
                #          "div.su-media.su-media--image > " + 
                #          "div.su-media__primary > " + 
                #          "div.su-media__image > " +
                #          "a.s-card__link.image-treatment > " +
                #          "img.s-card__image"))
                #        .get_attribute("src"))
                img = current_doll.find_element(By.CSS_SELECTOR, "img.s-card__image").get_attribute("src")
                print("Found image\n")

                try:
                        print("Shortening link...")
                        link = shortener.tinyurl.short(link)
                        listings.update({text: [price, link, img]})
                except Exception as e:
                        print(e)                    
                
        print("Listings for ebay found")     
        return listings
    
    listings = find_listings()

        

    