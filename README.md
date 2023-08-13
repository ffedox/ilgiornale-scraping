# Exctracting Comments with a Selenium Web Scraper

Scripts for extracting comments and articles from the website of the newspaper [Il Giornale](https://www.ilgiornale.it/).

## Contents

1. [Extract_article_ilgiornale.py](https://github.com/ffedox/ilgiornale_scraping/blob/main/extract_article_ilgiornale.py): script for extracting the text of an article given its URL.
2. [Extract_comments_ilgiornale.py](https://github.com/ffedox/ilgiornale_scraping/blob/main/extract_comments_ilgiornale.py): script for extracting the comments of an article given its URL.

## Getting the code

A copy of all the files can be downloaded by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/ffedox/ilgiornale_scraping

## Setup and installation
1. Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) <br />
`pip install beautifulsoup4` <br />
2. Install [Tkinter](https://docs.python.org/3/library/tkinter.html) <br />
`pip install tk`
3. Install [Selenium](https://www.selenium.dev/) <br />
`pip install selenium` <br />
4. Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) or install [Chromedriver-Autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/) <br />
`pip install chromedriver-autoinstaller` <br />
5. Add ChromeDriver [to system's PATH](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver) or include the path when instantiating `webdriver.Chrome` <br />
`driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe'` 
