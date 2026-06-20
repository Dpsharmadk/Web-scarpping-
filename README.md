# Web-scarpping
# Web Scraping Assignment

## Overview

This project is a Python-based web scraping application that extracts product information from a website. The program fetches webpage data, extracts product details, downloads product images, and compares product prices with a target price.

## Features

* Fetches webpage data using Python.
* Extracts product title.
* Extracts product price.
* Extracts product image URL.
* Downloads product images automatically.
* Compares product price with a target price.
* Handles multiple product URLs.

## Technologies Used

* Python 3
* Requests
* BeautifulSoup (bs4)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install required libraries:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script using:

```bash
python web_scrapping.py
```

## Expected Output

The program displays:

* Product Title
* Product Price
* Product Image URL
* Price comparison result
* Image download status

Example:

```text
Title: A Light in the Attic
Price: 51.77
Image URL: https://example.com/image.jpg
Result: Price is below target price
Image downloaded successfully!
```

## Project Structure

```text
WebScraping-DevPratapSharma/
│
├── web_scrapping.py
├── README.md
└── images/
```

## Author

Dev Pratap Sharma

## License

This project is created for educational and learning purposes.
