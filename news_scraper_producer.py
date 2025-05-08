# news_scraper_producer.py
import requests, json, time
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

# Load environment variables (if using .env)
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:
    res = requests.get(url).json()
    for article in res.get('articles', []):
        data = {
            'title': article['title'],
            'publishedAt': article['publishedAt'],
            'source': article['source']['name'],
            'description': article['description']
        }
        producer.send('news', value=data)
        time.sleep(1)
