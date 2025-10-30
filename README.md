practice assigment 02 for ST2195 
# ST2195 Assignment 2 – Web Scraping (Python & R)

## 📘 Overview
This assignment demonstrates how to programmatically scrape data from the web using both **Python** and **R**, then save and verify the output as CSV files.

The chosen example comes from the Wikipedia page on [Delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values).  
Both scripts extract a small sample CSV snippet from the page’s `<pre>` text blocks, save it as a `.csv` file, and reload it to confirm successful scraping.

## 🐍 Python Script (`python_csv/scrape_csv.py`)
- Uses **`requests`**, **`BeautifulSoup`**, and **`pandas`**
- Adds a browser-like *User-Agent header* to avoid a 403 error
- Finds and extracts the first `<pre>` block that looks like a CSV
- Saves it to `wikipedia_example.csv`
- Reads it back with `pandas` and prints the first few rows

### Run command
```bash
python3 scrape_csv.py
