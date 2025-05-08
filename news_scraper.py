# news_scraper.py
import requests, json, time
import os
from dotenv import load_dotenv

# Load environment variables (if using .env)
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'

while True:
    res = requests.get(url).json()
    for article in res.get('articles', []):
        data = {
            'title': article['title'],
            'publishedAt': article['publishedAt'],
            'source': article['source']['name'],
            'description': article['description']
        }
        print(data)
        time.sleep(1)
