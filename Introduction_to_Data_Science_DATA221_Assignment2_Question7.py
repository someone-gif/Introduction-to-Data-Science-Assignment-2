from bs4 import BeautifulSoup
import requests

# Fetch the data with proper headers
url_of_the_data_science_wikipedia_page = "https://en.wikipedia.org/wiki/Data_science"

#usualy the wikipedia denies acesss so I used the user agent to make it work
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

#headers=headers for the user agent
data_science_wikipedia_page = requests.get(url_of_the_data_science_wikipedia_page, headers=headers).text

# Parse the HTML
parsed_data_science_wikipedia_html_document = BeautifulSoup(data_science_wikipedia_page, "html5lib")

# Get the page title using the title tag
title_of_the_data_science_wikipedia_page = parsed_data_science_wikipedia_html_document.find('title')
print("Page Title:", title_of_the_data_science_wikipedia_page)

# Get first paragraph 
content_inside_div_of_the_data_science_wikipedia_html_document = parsed_data_science_wikipedia_html_document.find('div', id='mw-content-text')
all_paragraphs_of_the_data_science_wikipedia_page = content_inside_div_of_the_data_science_wikipedia_html_document.find_all('p')

 # Find first paragraph   
for current_paragraph in all_paragraphs_of_the_data_science_wikipedia_page:
    text_of_the_current_paragraph = current_paragraph.get_text(strip=True)
    if len(text_of_the_current_paragraph) >= 50:  
        print("First paragraph:")
        print(text_of_the_current_paragraph)
        break