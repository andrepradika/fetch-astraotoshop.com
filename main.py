import requests
import pandas as pd

# API endpoint
url = "https://api.astraotoshop.com/v1/product-service/search/v2"

# Headers (if needed, update accordingly)
headers = {
    "Content-Type": "application/json"
}

# Initialize variables
all_products = []
page = 1
page_size = 50  # Fetch 50 items per request for efficiency

def fetch_data(page):
    payload = {
        "text": "",
        "page": page,
        "pageSize": page_size,
        "sort": None,
        "filter": {
            "priceMin": 0,
            "priceMax": 1000000000,
            "rating": None,
            "brandIds": [],
            "mainCategoryIds": [],
            "vehicleId": None,
            "myGarageId": "",
            "categoryId": ""
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Fetch first page to get total pages
initial_data = fetch_data(page)
total_pages = initial_data.get("total_page", 1)
all_products.extend(initial_data.get("data", []))

# Loop through all pages
for page in range(2, total_pages + 1):
    print(f"Fetching page {page}/{total_pages}...")
    data = fetch_data(page)
    all_products.extend(data.get("data", []))

# Extract relevant fields
products = []
for item in all_products:
    product = {
        "ID": item["id"],
        "URL Key": item["urlKey"],
        "Name": item["name"],
        "Original Price": item.get("priceOriginal"),
        "Price": item.get("price"),
        "Available Quantity": item.get("availableQty"),
        "Merchant Name": item.get("merchantName"),
        "Brand Name": item.get("brandName"),
        "Currency": item.get("currency"),
        "Rating": item.get("rating"),
        "SKU": item.get("sku"),
        "Total Sold": item.get("total_sold"),
        "Created At": item.get("created_at"),
        "Updated At": item.get("updated_at"),
        "Main Image URL": next((media["url"] for media in item.get("product_media", []) if media.get("is_main")), None),
        "Categories": ", ".join(category["categories_name"] for category in item.get("product_categories", [])),
    }
    products.append(product)

# Create DataFrame
df = pd.DataFrame(products)

# Save to CSV and XLSX
df.to_csv("output/astraotoshop_data.csv", index=False)
df.to_excel("/output/astraotoshop_data.xlsx", index=False)

print("Data saved successfully!")
