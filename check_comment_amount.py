import requests
from bs4 import BeautifulSoup

def check_comment_amount(url):

  # Make a GET request to the URL and fetch the HTML content
  response = requests.get(url)
  html_content = response.content

  # Parse the HTML content with Beautiful Soup
  soup = BeautifulSoup(html_content, "html.parser")

  # Find the HTML tag that contains the amount of comments
  comments_link = soup.find("a", {"class": "comments-link"})

  # Extract the comment amount from the HTML tag
  comments_text = comments_link.text
  comments_num = comments_text.split()[0]

  # Print the amount of comments
  print(comments_num)