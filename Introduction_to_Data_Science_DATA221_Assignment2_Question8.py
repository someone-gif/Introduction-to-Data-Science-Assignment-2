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

# Get first paragraph 
content_inside_div_of_the_data_science_wikipedia_html_document = parsed_data_science_wikipedia_html_document.find('div', id='mw-content-text')
all_section_headings_from_main_content_area = content_inside_div_of_the_data_science_wikipedia_html_document.find_all('h2')

# Forbidden words
forbidden_words = ['References', 'External links', 'See also', 'Notes']

# Extract clean headings
headings_of_the_wikipedia_page = []
for current_h2_tag in all_section_headings_from_main_content_area:
    # Get text and remove [edit] links
    fetched_text = current_h2_tag.get_text(strip=True)
    fetched_text = fetched_text.replace('[edit]', '').strip()
    headings_of_the_wikipedia_page.append(fetched_text)
    
    # Skip if contains forbidden words
    for word in forbidden_words:
        if word in headings_of_the_wikipedia_page:
            headings_of_the_wikipedia_page.remove(fetched_text)

# Save to file
with open('C:/Users/zaint/DATA221_SEMESTER1/headings.txt', 'w') as current_saved_file:
    for current_heading in headings_of_the_wikipedia_page:
        current_saved_file.write(current_heading + '\n')

for current_heading in headings_of_the_wikipedia_page:
    print(current_heading)
