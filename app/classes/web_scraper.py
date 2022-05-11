"""
Module with web scraper class who represents the web scraper client
"""

from dataclasses import dataclass
from app.classes.laptop import Laptop
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from typing import List
import os
import re

@dataclass(slots=True)
class WebScraper:
    """web scraper class"""

    selenium_driver: webdriver
    url: str 

    def __init__(self) -> None:
        """Initializer of the class"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # self.selenium_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options )
        self.selenium_driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=chrome_options )
        self.url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    
    def get_laptops_informations_from_url(self, manufacturer:str = "lenovo", sort:bool = True, ) -> List[Laptop]:
        """Gets laptops information from webscraper.io"""
        list_of_laptops: List[Laptop] = []
        self.selenium_driver.get(self.url)
        page_content = self.selenium_driver.page_source
        html_parsed = BeautifulSoup(page_content, features="html.parser")
        root_url = self.url.split('/test-sites')[0]
        # Iterates across all laptops
        for div_tag in html_parsed.findAll('div', attrs={'class':'thumbnail'}):
            div_caption = div_tag.find('div', attrs={'class':'caption'})
            if div_caption is not None:
                laptop_tag = div_caption.find('a', href=True, attrs={'class':'title'})
                laptop_name = laptop_tag.get('title')
                path_to_laptop = laptop_tag.get('href')
                laptop_link = None
                #Gets the link path of the laptop
                if path_to_laptop is not None:
                    laptop_link = root_url + laptop_tag.get('href')
                # Searches laptops with the manufacturer name
                if manufacturer.upper() in laptop_name.upper():
                    laptop_price = div_caption.find('h4', attrs={'pull-right price'}).text
                    laptop_description = div_caption.find('p', attrs={'description'}).text
                    div_ratings = div_tag.find('div', attrs={'class':'ratings'})
                    #Gets rating of the laptop
                    laptop_rating = len(div_ratings.findAll('span', attrs={'class':'glyphicon glyphicon-star'}))
                    #Gets the number of reviews for the laptop
                    laptop_number_of_reviews = int(
                        re.findall(
                            pattern='[0-9]+',
                            string=div_ratings.find('p', attrs={'class':'pull-right'}).text)[0])
                    list_of_laptops.append(Laptop(
                        name = laptop_name, 
                        description = laptop_description,
                        price = laptop_price,
                        number_of_reviews = laptop_number_of_reviews,
                        rating = laptop_rating,
                        link= laptop_link))
        if sort:
            #Sort laptop list
            list_of_laptops.sort(key= lambda laptop:laptop.price)
        return list_of_laptops
    