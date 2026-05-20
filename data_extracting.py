import pandas as pd

def parse_table(netflix_soup, netflix_df):

    for row in netflix_soup.find('tbody').find_all('tr'):
        col= row.find_all('td')
        date = col[0].text
        open = col[1].text
        high = col[2].text
        low = col[3].text
        close = col[4].text
        volume = col[5].text
   
        netflix_df = pd.concat([netflix_df, pd.DataFrame([{"Date": date, "Open": open, "High": high, "Low": low, "Close": close, "Volume": volume}])], ignore_index=True)
        
    return netflix_df