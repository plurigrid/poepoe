# Web Scraper

This is a web scraping tool built with Python and Scrapy to extract data from Poe.com. The tool is capable of handling infinite scroll back and dynamic content. The scraped data is stored in a structured JSON format.

## Tech Stack

- Python
- Scrapy

## Features

- Extract specific conversation on Poe.com
- Account for infinite scroll back
- Handle dynamic content
- Store scraped data in a structured format in JSON

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Install the dependencies using Poetry:

```bash
poetry install
```

## Usage

To run the scraper, use the following command:

```bash
scrapy runspider web_scraper/scrapy_spider.py
```

The scraped data will be stored in a JSON file in the project directory.

## Rules

We have implemented a rule to prevent logging of customer data. The rule is defined in the `.rules/prevent-customer-logs.md` file. Please make sure to follow this rule to maintain our SOC2 certification.

## Clojure Version

We also have a Clojure version of the web scraper. You can find it in the `web_scraper/clojure_version.clj` file. To run the Clojure version, use the following command:

```bash
clojure web_scraper/clojure_version.clj
```

The scraped data will also be stored in a JSON file in the project directory.