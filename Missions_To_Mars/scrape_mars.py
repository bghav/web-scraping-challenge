from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

def scrape_headline(browser):
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

    return news_title, news_p

def scrape_moonimg(browser):
     # URL of page to be scraped
    url = 'https://spaceimages-mars.com//'
    browser.visit(url)
    
    # URL of featured image
    featured_image_url = '	https://spaceimages-mars.com/image/featured/mars2.jpg'
    browser.visit(featured_image_url)
    
    return featured_image_url

def scrape_mfacts(browser):
    
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)
    
    mars_facts = pd.read_html("https://galaxyfacts-mars.com")[0]

    return mars_facts

def scrape_hemisphere(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_image_urls = []
    links = browser.find_by_css('a.product-item img')

    for i in range(len(links)):
        hemisphere = {}
            
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css('a.product-item img')[i].click()
            
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
            
        hemisphere['title'] = browser.find_by_css('h2.title').text
            
    return hemisphere
            
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title,news_p =scrape_headline(browser)
    featured_image_url = scrape_moonimg(browser)
    mars_facts = scrape_mfacts(browser)
    hemisphere = scrape_hemisphere(browser)
    
    mars_dict={
    "news_title":news_title,
    "news_p":news_p,
    "featured_image_url":featured_image_url,
    "mars_facts":mars_facts,
    "hemisphere":hemisphere
    }
    return mars_dict
