import re

def extract_urls(google_html):

  with open(google_html, 'r', encoding='utf-8') as f:
      file_content = f.read()

  pattern = r'data-sokoban-feature="(.*?)"><div class="(.*?)"><a href="(?=https://)(.*?)" data-jsarwt='

  links = re.findall(pattern, file_content)

  # Extract only the URLs from the list of links
  urls = [link[2] for link in links if not link[2].startswith("https://www.google.com/")]

  # Save the URLs to a text file
  with open("urls.txt", "w") as f:
      f.write("\n".join(urls))