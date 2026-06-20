import requests
from bs4 import BeautifulSoup
import os


# List of product URLs
product_urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

# Target price for comparison
target_price = 55


def scrape_product(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title
        title = soup.find("h1").text

        # Extract price
        price_text = soup.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", ""))

        # Extract image URL
        image_relative = soup.find("img")["src"]
        image_url = "https://books.toscrape.com/" + image_relative.replace("../", "")

        # Download image
        image_data = requests.get(image_url).content

        os.makedirs("images", exist_ok=True)

        image_name = title.replace(" ", "_") + ".jpg"
        image_path = os.path.join("images", image_name)

        with open(image_path, "wb") as file:
            file.write(image_data)

        # Display details
        print("\n------------------------")
        print("Title :", title)
        print("Price :", price)
        print("Image URL :", image_url)

        # Price comparison
        if price <= target_price:
            print(f"Result : Price is below target (£{target_price})")
        else:
            print(f"Result : Price is above target (£{target_price})")

        print("Image downloaded successfully!")

    except Exception as e:
        print(f"Error processing {url}")
        print(e)


# Handle multiple URLs
for url in product_urls:
    scrape_product(url)