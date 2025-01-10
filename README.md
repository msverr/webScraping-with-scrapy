# Web Scraping Project: Books Scraper

This project is a web scraper built with Python's Scrapy library. It scrapes data from [books.toscrape.com](http://books.toscrape.com), a website that provides information about various books. The scraper extracts details such as book titles, prices, ratings, and other relevant metadata.

## Features

- **Web Scraping with Scrapy**: The main scraping logic is implemented using Scrapy, a powerful web scraping framework for Python.
- **Data Storage**: 
  - **JSON**: The extracted data is saved in a structured JSON format for easy access and manipulation.
  - **MySQL Database**: The scraper also stores the data in a MySQL database named `books`, making it easier to perform queries and manage large datasets.
- **Random API Headers**: To ensure that requests made to the website are not blocked, the project uses [scrapeops.io](https://www.scrapeops.io/) to generate random headers for each API request.

## Requirements

- Python 3.x
- Scrapy
- MySQL
- scrapeops.io API (for random header generation)

## Installation

1. Install the necessary Python libraries:
   ```bash
   pip install scrapy
   pip install mysql-connector
   pip install scrapeops