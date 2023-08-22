import requests
from bs4 import BeautifulSoup
import csv
import time

input_csv_file = "amazon_products.csv"
output_csv_file = "amazon_products_output.csv"

data = []

# Load data from the input CSV file
with open(input_csv_file, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)

# Function to fetch product details from a URL
def fetch_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Use BeautifulSoup to extract description, ASIN, product description, and manufacturer
        description = "TODO"
        asin = "TODO"
        product_description = "TODO"
        manufacturer = "TODO"

        return description, asin, product_description, manufacturer

    else:
        print(f"Failed to retrieve product page: {url}")
        return None, None, None, None

# Process each product in the data list
for item in data:
    product_url = item[1]

    # Fetch additional product details
    description, asin, product_description, manufacturer = fetch_product_details(product_url)
    
    # Update the data list with additional information
    item.extend([description, asin, product_description, manufacturer])

    # Add a delay between requests to avoid overloading the server
    time.sleep(2)

# Write data to the output CSV file
with open(output_csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header + ["Description", "ASIN", "Product Description", "Manufacturer"])
    writer.writerows(data)

print(f"Scraped data with additional information has been saved to {output_csv_file}")
