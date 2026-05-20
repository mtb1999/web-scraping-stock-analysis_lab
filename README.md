# Netflix Stock Data Web Scraping

## Lab Overview

In this lab, we extract historical Netflix stock data from a web page using web scraping. Not all stock data is available through an API, so this project uses Python, `requests`, `BeautifulSoup`, and `pandas` to collect stock data directly from an HTML table.

The current code downloads an HTML page, parses it with `BeautifulSoup`, extracts the historical Netflix stock table, stores the result in a Pandas DataFrame, and prints the first 10 rows.

## What We Will Do

- Use `requests` to download the Netflix stock data web page.
- Use `BeautifulSoup` with the `html5lib` parser to read the HTML content.
- Locate the table body containing historical stock rows.
- Extract the following columns: Date, Open, High, Low, Close, and Volume.
- Store the scraped rows in a Pandas DataFrame.
- Print the first 10 rows of the DataFrame from `main.py`.

## Project Files

- `main.py` — creates the Netflix DataFrame, calls the scraping and parsing functions, and prints the first 10 rows.
- `data_gathering.py` — contains `html_scraping()`, which downloads the web page and returns a parsed BeautifulSoup object.
- `data_extracting.py` — contains `parse_table()`, which extracts table rows and adds them to the DataFrame.
- `requirements.txt` — lists the Python packages needed for this lab.

## Lab Requirements

### Software Requirements

- Python 3.x
- Jupyter Notebook or a Python script editor
- Internet connection
- VS Code or another code editor

### Python Libraries

The following Python libraries will be used:

- `requests` — to download the web page content
- `beautifulsoup4` — to parse and extract data from HTML
- `pandas` — to organize and clean the extracted data
- `html5lib` — the HTML parser used by the current code
- `lxml` — included as an optional parser dependency
- `plotly` — installed for future visualization work

It is recommended to create and activate a virtual environment before installing the project requirements.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Then install all required libraries from the requirements file:

```bash
pip install -r requirements.txt
```

## How to Run the Project

After installing the requirements, run:

```bash
python main.py
```

The script will print the first 10 rows of the scraped Netflix stock data.

## Expected Lab Steps

1. Import the required Python libraries.
2. Create an empty Netflix DataFrame with the columns Date, Open, High, Low, Close, and Volume.
3. Define the Netflix stock data URL.
4. Send an HTTP request to download the page.
5. Use `BeautifulSoup` to parse the HTML content.
6. Find the table body that contains the historical stock prices.
7. Convert the extracted values into a Pandas DataFrame.
8. Display the first 10 rows of the scraped data.

## Expected Output

By the end of this lab, we should have a table containing historical Netflix stock data with these columns:

- Date
- Open price
- High price
- Low price
- Close price
- Volume

## Learning Objectives

After completing this lab, we will be able to:

- Understand why web scraping is useful when API data is unavailable.
- Use `requests` to retrieve web page content.
- Use `BeautifulSoup` to parse HTML.
- Extract financial data from HTML tables.
- Structure scraped data using `pandas`.
- Prepare historical stock data for further analysis.

## Git Setup and Push

This project includes a `.gitignore` file so temporary files like `.venv` and `__pycache__` are not pushed to GitHub.

To push this project to GitHub:

```bash
git init
git add .
git commit -m "Initial stock web scraping lab"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your GitHub repository URL.

## Notes

This lab is for educational purposes only. When scraping websites, always review the website's terms of service and avoid sending too many requests in a short period of time.
