from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the browser
browser = webdriver.Chrome()

# Load the page
url = "https://www.ilgiornale.it/news/politica/rula-talebana-dello-ius-soli-e-chi-critica-nazista-1442362.html"
browser.get(url)

# Click the "show more comments" button
show_more_button = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.comments__trigger"))
)
show_more_button.click()

# Wait for the comments section to load
comments_section = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "ilg_comments"))
)

# Extract all comments with date and username
comments = comments_section.find_elements_by_css_selector("div.comment")

# Save the comments to a file
with open("commenti.txt", "w") as file:
    for comment in comments:
        user = comment.get_attribute("data-user")
        date = comment.find_element_by_css_selector("div.comment__date").text
        body = comment.find_element_by_css_selector("div.comment__body").text
        file.write(f"{user} - {date}\n{body}\n\n")

# Close the browser
browser.quit()
