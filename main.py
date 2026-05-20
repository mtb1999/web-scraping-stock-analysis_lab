import pandas as pd
from data_gathering import html_scraping
from data_extracting import parse_table 


netflix_df = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
url_Netflix = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

netflix_soup = html_scraping(url_Netflix)
netflix_df = parse_table(netflix_soup, netflix_df)

print(netflix_df.head(10))