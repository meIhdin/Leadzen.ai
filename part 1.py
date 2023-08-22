import http.client
import urllib.parse
import ssl
import csv
import time

base_url = "www.amazon.in"
search_query = "bags"
pages_to_scrape = 20

data = []

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

for page_number in range(1, pages_to_scrape + 1):
    query_params = {
        "k": search_query,
        "page": page_number,
        "crid": "2M096C61O4MLT",
        "qid": "1653308124",
        "sprefix": "ba%2Caps%2C283",
        "ref": "sr_pg_1"
    }
    query_string = urllib.parse.urlencode(query_params)

    connection = http.client.HTTPSConnection(base_url, context=context)
    url = f"/s?{query_string}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        connection.request("GET", url, headers=headers)
        response = connection.getresponse()

        if response.status == 200:
            data = response.read().decode("utf-8")
            connection.close()

            # Parse data using regex as before

            # Add a delay between requests to avoid overloading the server
            time.sleep(2)

        else:
            print(f"Failed to retrieve page {page_number}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Write data to CSV
csv_file = "amazon_products.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product URL", "Product Name", "Product Price", "Product Rating", "Number of Reviews"])
    writer.writerows(data)

print(f"Scraped data has been saved to {csv_file}")
