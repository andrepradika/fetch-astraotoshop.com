# Astra Otoshop Product Scraper

This Python script fetches product data from the Astra Otoshop API, extracts relevant details, and saves them as CSV and XLSX files.

## Features

- Fetches all available product data dynamically by iterating through API pages.
- Extracts key product details including name, price, SKU, brand, category, and images.
- Saves data in CSV and XLSX formats for easy analysis.

## Requirements

Ensure you have the following dependencies installed:

```bash
pip install requests pandas openpyxl
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/andrepradika/fetch-astraotoshop.com
   cd fetch-astraotoshop
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. The extracted data will be saved as:

   - `astraotoshop_data.csv`
   - `astraotoshop_data.xlsx`

## API Details

- **Endpoint**: `https://api.astraotoshop.com/v1/product-service/search/v2`
- **Method**: POST
- **Response**: JSON containing product details

## Output Fields

The script extracts and saves the following fields:

- ID
- Name
- Original Price
- Price
- Available Quantity
- Merchant Name
- Brand Name
- Currency
- Rating
- SKU
- Total Sold
- Created At
- Updated At
- Main Image URL
- Categories

## License

MIT License

## Author

andrepradika