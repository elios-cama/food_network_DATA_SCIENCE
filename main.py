import requests
from bs4 import BeautifulSoup
import csv

# Define the base URL pattern
base_url = "https://locavor.fr/producteurs-en-circuits-courts-par-departement/cote-d-or?p="

# Initialize an empty list to store shop information
shop_info = []

# Set the total number of pages or stop condition
total_pages = 10  # Change this to the total number of pages you want to scrape

# Loop through the pages
for page_number in range(1, total_pages + 1):
    # Construct the URL for the current page
    url = f"{base_url}{page_number}"

    # Send an HTTP GET request to the current page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <div> elements with class "col cardwidth"
        shop_elements = soup.find_all('div', class_='col cardwidth')

        # Iterate through the shop elements on the current page
        for shop in shop_elements:
            # Find the shop name within the <strong> element
            shop_name = shop.find('strong').text.strip()

            # Find the category names within the <img> elements
            categories = [img['title'] for img in shop.find_all('img', title=True)]

            # Append the shop name and categories as a tuple to the list
            shop_info.append((shop_name, ', '.join(categories)))
    else:
        print(f"Failed to retrieve page {page_number}. Status code:", response.status_code)

# Define the CSV file name
csv_file = 'shop_data.csv'

# Write the data to the CSV file with UTF-8 encoding
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['name', 'category'])
    
    # Write the data rows
    writer.writerows(shop_info)

print(f"Data has been saved to {csv_file}.")
