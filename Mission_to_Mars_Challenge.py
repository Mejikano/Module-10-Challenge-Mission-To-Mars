#!/usr/bin/env python
# coding: utf-8

# In[104]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[105]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[106]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[107]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[108]:


slide_elem.find('div', class_='content_title')


# In[109]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[110]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[111]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[112]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[113]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[114]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[115]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[116]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[117]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[118]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[119]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[120]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
h_soup = soup(browser.html, 'html.parser')

h_item= h_soup.find_all('div', class_='item')

hemi = {}
for i in h_item:

    #print(i.prettify())
    title=i.find('h3').get_text()
    
    #print(title)
    
    browser.find_by_text(title).click()
    
    img_soup=soup(browser.html, 'html.parser')
    img=img_soup.find_all('li')[0].a
    
    #print(img['href'])
    
    browser.back()
    
    hemi = {
        'img_url': f'https://marshemispheres.com/{img["href"]}',
        'title': title
    }
    hemisphere_image_urls.append(hemi)
    


# In[121]:


hemisphere_image_urls


# In[122]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[123]:


# 5. Quit the browser
browser.quit()


# In[ ]:




