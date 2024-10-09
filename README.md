# Microcenter Scraper
* This Python script scrapes product data from Microcenter's website, allowing users to search for PC components based on a keyword (e.g., "1 tb ssd") and retrieve information such as product name, price, stock, and a link to the product.

## Features
* Enter a search query to retrieve a list of products from Microcenter.
* Displays product name, price, stock position, and a direct link to the product page.

## Installation
1. Clone the repository:
```
git clone https://github.com/sayuj1998/PCBuilderBot.git
```
2. Install required dependencies:
```
pip install requests
```

## Usage
1. Run the script: 
```
python microcenter_scraper.py
```
2. Input your desired search query (e.g., "1 tb ssd") to fetch product details from Microcenter.

## Example
```
microcenter = Microcenter()
microcenter.search("1 tb ssd")
```
Output:
```
Product: Samsung 1TB SSD
Price: $99.99
Stock: 6
Link: https://www.microcenter.com/samsung-1tb-ssd
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product: Samsung 2TB SSD
Price: $129.99
Stock: 15
Link: https://www.microcenter.com/samsung-2tb-ssd
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

