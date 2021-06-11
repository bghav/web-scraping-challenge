from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os


def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://redplanetscience.com/
     # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)

html = browser.html
news_soup = bs(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

news_title = slide_elem.find('div', class_='content_title').text()
news_title

news_p = slide_elem.find('div', class_='article_teaser_body').text()
news_p


 # URL of featured image
featured_image_url = '	https://spaceimages-mars.com/image/featured/mars2.jpg'

# Retrieve the Mars Facts
df = pd.read_html("https://galaxyfacts-mars.com")[0]
df

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# First, get a list of all of the hemispheres
links = browser.find_by_css('a.product-item img')

# Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
    hemisphere = {}
    
    # We have to find the elements on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item img')[i].click()
    
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    avg_temps = soup.find('div', id='weather')

    # Get the min avg temp
    min_temp = avg_temps.find_all('strong')[0].text

    # Get the max avg temp
    max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[4]["src"]
    marsh = hemisphere_image_urls + relative_image_path

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "marsh": marsh
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
