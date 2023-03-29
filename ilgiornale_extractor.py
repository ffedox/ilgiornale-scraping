import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import filedialog

def check_comment_amount_ilgiornale(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    comments_link = soup.find("a", {"class": "comments-link"})
    comments_text = comments_link.text
    comments_num = comments_text.split()[0]
    return comments_num

def get_comment_count():
    url = url_entry.get()
    comments_num = check_comment_amount_ilgiornale(url)
    result_label.config(text=f"Number of comments: {comments_num}")

def clean_files(destination_directory):
    for filename in os.listdir(destination_directory):
        if filename.endswith("_" + ".txt"):
            print(f"Eliminando {filename} (duplicato)")
            os.remove(os.path.join(destination_directory, filename))

def format_date_in_filename(filename):
    
    italian_months = {
        'Gen': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'Mag': '05',
        'Giu': '06',
        'Lug': '07',
        'Ago': '08',
        'Set': '09',
        'Ott': '10',
        'Nov': '11',
        'Dic': '12'
    }

    parts = filename.split("_")
    date = parts[-1][:-4]

    if len(date) == 8:
        day = '0' + date[:1]
        month = italian_months[date[1:4]]
        year = date[-2:]
    else:
        day = date[:2]
        month = italian_months[date[2:5]]
        year = date[-2:]

    formatted_date = f"{day}{month}{year}"

    if len(parts) == 4:
        new_filename = f"{parts[0]}_{parts[1]}_{parts[2]}_{formatted_date}.txt"
    else:
        new_filename = f"{parts[0]}_{parts[1]}_{formatted_date}.txt"

    new_filename = new_filename.replace(" ", "_")
    return new_filename

def format_dates_in_destination(destination_directory):
    for filename in os.listdir(destination_directory):
        new_filename = format_date_in_filename(filename)
        old_file_path = os.path.join(destination_directory, filename)
        new_file_path = os.path.join(destination_directory, new_filename)
        os.rename(old_file_path, new_file_path)

def extract_comments_ilgiornale(url, article_code, destination_directory):
    browser = webdriver.Chrome()

    try:
        browser.get(url)
        show_more_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.comments__trigger"))
        )
        show_more_button.click()

        comments_section = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ilg_comments"))
        )

        comments = comments_section.find_elements_by_css_selector("div.comment")

        for comment in comments:
            user = comment.get_attribute("data-user")
            date = comment.find_element_by_css_selector("div.comment__date").text
            body = comment.find_element_by_css_selector("div.comment__body").text
            formatted_date = "".join(date.split()[:3])
            counter = 2
            filename = f"{article_code}_{user}_{formatted_date}.txt"

            while os.path.exists(os.path.join(destination_directory, filename)):
                filename = f"{article_code}_{user}_{counter}_{formatted_date}.txt"
                counter += 1

            with open(os.path.join(destination_directory, filename), "w") as file:
                file.write(body)

    finally:
        browser.quit()

def modify_filenames_if_content_starts_with_at(destination_directory):
    # Loop over all the files in the directory
    for file_name in os.listdir(destination_directory):
        file_path = os.path.join(destination_directory, file_name)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()

            if content.startswith('@'):
                at_text = content.split()[0][1:]

                # Split the filename into parts
                parts = file_name.split("_")

                # Concatenate the string between "@" and the first whitespace to the second item in the list, with "X" as a separator
                parts[1] = f"{parts[1]}X{at_text}"

                # Reassemble the filename
                new_file_name = '_'.join(parts)

                # Rename the file
                new_file_path = os.path.join(destination_directory, new_file_name)
                os.rename(file_path, new_file_path)

def extract_comments_button():
    url = url_entry.get()
    article_code = code_entry.get()
    destination_directory = filedialog.askdirectory()
    extract_comments_ilgiornale(url, article_code, destination_directory)
    clean_files(destination_directory)
    format_dates_in_destination(destination_directory)
    modify_filenames_if_content_starts_with_at(destination_directory)

app = tk.Tk()
app.title("Il Giornale Comment Extractor")

tk.Label(app, text="URL:").grid(row=0, column=0, sticky=tk.W)
url_entry = tk.Entry(app)
url_entry.grid(row=0, column=1)

tk.Label(app, text="Article Code:").grid(row=1, column=0, sticky=tk.W)
code_entry = tk.Entry(app)
code_entry.grid(row=1, column=1)

# Create a button to check the comment count and output it
get_comments_button = tk.Button(app, text="Get Comment Count", command=get_comment_count)
get_comments_button.grid(row=3, column=1)

# Create a button to extract comments
extract_comments_button = tk.Button(app, text="Extract Comments", command=extract_comments_button)
extract_comments_button.grid(row=3, column=2)

result_label = tk.Label(app, text="")
result_label.grid(row=4, column=1)

app.mainloop()