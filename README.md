# Web Scraping Assignment

## Project Description

This project demonstrates web scraping using Python, Requests, and BeautifulSoup.

The program:

* Scrapes book titles from BooksToScrape
* Extracts product prices
* Compares prices with a target value
* Downloads product images
* Saves images locally

## Technologies Used

* Python
* Requests
* BeautifulSoup4

## How to Run

### Install Dependencies

```bash
pip install requests beautifulsoup4
```

### Run the Program

```bash
python web_scrapping.py
```

## Features Implemented

* Sending HTTP requests
* Parsing HTML content
* Extracting product information
* Price comparison
* Downloading images
* Error handling using try-except

## Output

The program displays:

* Book Title
* Price
* Price Comparison Result
* Image Download Status

Downloaded images are stored inside the `images` folder.

