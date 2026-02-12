from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fetch the data with proper headers
url_of_the_data_science_wikipedia_page = "https://en.wikipedia.org/wiki/Machine_learning"

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
all_tables_from_main_content_area = content_inside_div_of_the_data_science_wikipedia_html_document.find_all('table')

target_table_with_enough_meaningful_elements = None
for current_table in all_tables_from_main_content_area:
    data_rows = []  # Reset for each table
    for current_row in current_table.find_all('tr'):  # Loop through ALL rows in THIS table
        if current_row.find_all(['td', 'th']):  # Has actual data cells
            data_rows.append(current_row)
    
    if len(data_rows) >= 3:  # Found table with ≥3 meaningful rows
        target_table_with_enough_meaningful_elements = current_table
        break

headers_of_the_rows = []
elements_with_th_tag = content_inside_div_of_the_data_science_wikipedia_html_document.find_all('th')

for current_element_with_th_tag in elements_with_th_tag:
    headers_of_the_rows.append(current_element_with_th_tag.get_text(strip=True))

# Extract all table data
table_data = []
all_rows = target_table_with_enough_meaningful_elements.find_all('tr') #tr is allthe rows 
number_of_colums = len(headers_of_the_rows)

for current_row in all_rows:
    row_cells = current_row.find_all(['td', 'th']) #colums
    row_data = []
    for current_cell in row_cells:
        row_data.append(current_cell.get_text(strip=True))
    # Pad with empty strings if row is short
    while len(row_data) < number_of_colums:
        row_data.append('')
    
    table_data.append(row_data)

# Create and save DataFrame
data_frame = pd.DataFrame(table_data, columns=headers_of_the_rows)
data_frame.to_csv('C:/Users/zaint/DATA221_SEMESTER1/wiki_table.csv')