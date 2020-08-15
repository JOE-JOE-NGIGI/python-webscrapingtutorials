#Python script to scrape Flikar website to extract price,name and rating of laptops
#importing necessary libraries
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

# configure webdriver to use chrome browser
driver = webdriver.chrome("/usr/lib/chromium-browser/chromedriver")

#to open url
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

#Extracting data from the website
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)
