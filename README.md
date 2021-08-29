# Module-10-Challenge-Mission-To-Mars


### Resources
- Data source: https://redplanetscience.com, https://spaceimages-mars.com, https://galaxyfacts-mars.com, https://marshemispheres.com/
- Software: Python 3.7.10, Jupyter Notebook 6.3.0, HTML 5, Bootstrap 3
- key libraries: Splinter, BeautifulSoup, Pandas, MongoDB, Flask


## Overview

 This project puts together a Mars news, facts and information scrapped from many web pages. The application is wto get the latest news and updates with the click of a button, eally useful tool for someone who wants to keep up with the Mission to Mars. The scrapping results are presented on a totally responsive page to be accessible from any device. 



## Results

**Home Page Mars Scrapping**

![Mars Scrapping Home page](https://github.com/Mejikano/Module-10-Challenge-Mission-To-Mars/blob/main/Resources/mars_scrapping_home.png)

**Enhanced Mars facts table**

![Mars Facts](https://github.com/Mejikano/Module-10-Challenge-Mission-To-Mars/blob/main/Resources/enhanced_mars_facts.png)

Note: Mars Facts html table comes from a panda´s function therefore classes required for Bootstrap styling cannot be inserted directly into the html pages: index.html. Panda to_html function allows classes attribute as a list or tuple passing parameters; refer below snippet. 


``` 
return df.to_html(classes=['table', 'table-hover', 'success', 'table-striped'])
```

scraping.py,  mars_facts() function

```
def mars_facts():
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
            return None

    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    return df.to_html(classes=['table', 'table-hover', 'success', 'table-striped'])
```

**Mars Hemispheres**

![Mars Facts](https://github.com/Mejikano/Module-10-Challenge-Mission-To-Mars/blob/main/Resources/mars_hemisphere.png)
