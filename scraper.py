import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_douban_top250():
    movies = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    for start in range(0, 250, 25):  # 每页25部，共10页
        url = f"https://movie.douban.com/top250?start={start}"
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        
        for item in soup.select(".item"):
            title = item.select_one(".title").text
            rating = item.select_one(".rating_num").text
            year = item.select_one(".bd p").text.strip().split("\n")[1].strip()[:4]
            quote = item.select_one(".inq")
            
            movies.append({
                "title": title,
                "rating": float(rating),
                "year": year,
                "quote": quote.text if quote else ""
            })
        
        print(f"已爬取 {start + 25} 部...")
        time.sleep(1)  # 控制请求频率，避免被封
    
    return pd.DataFrame(movies)

df = scrape_douban_top250()
df.to_csv("movies.csv", index=False, encoding="utf-8-sig")
print(df.head())