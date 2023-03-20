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

# Extract all comment bodies
comment_bodies = comments_section.find_elements_by_css_selector("div.comment__body")

# Save the comment bodies to a file
with open("commenti.txt", "w") as file:
    for body in comment_bodies:
        file.write(body.text + "\n")

# Close the browser
browser.quit()
