

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt



def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one('div.list_text')
        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        #news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        #news_p
    except AttributeError:
        return None, None
    return news_title, news_p


def featured_image(browser):
    # ### Featured Images

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        #img_url_rel
    except AttributeError:
        return None


    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    return img_url


def mars_facts():
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
            return None

    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    return df.to_html(classes=['table', 'table-hover', 'success', 'table-striped'])


def mars_hemisphere(browser):

    # # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    h_soup = soup(browser.html, 'html.parser')

    h_item= h_soup.find_all('div', class_='item')

    hemi = {}
    for i in h_item:

        title=i.find('h3').get_text()
        #print(title)
        
        #Go to the title link
        browser.find_by_text(title).click()
    
        #Parse the visited page
        img_soup=soup(browser.html, 'html.parser')
        #Save first image from the list 
        img=img_soup.find_all('li')[0].a
        #Navigate back 
        browser.back()
        
        hemi = {
            'img_url': f'https://marshemispheres.com/{img["href"]}',
            'title': title
        }
        hemisphere_image_urls.append(hemi)
        
        #hemisphere_image_urls

    return hemisphere_image_urls

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "hemispheres":mars_hemisphere(browser),
      "last_modified": dt.datetime.now()
    }
    
    browser.quit()

    return data


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())