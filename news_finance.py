import datetime, requests, yfinance
from alpaca_trade_api.rest import REST
from getpass import getpass
from transformers import pipeline

BASE_URL = "https://paper-api.alpaca.markets"
API_KEY = getpass('Enter your API KEY: ')
SECRET_KEY = getpass('Enter your SECRET KEY: ')

api = REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)


news = api.get_news('BTC/USD')

for story in news:
  print(story.headline)
  print(story.summary)
  for image in story.images:
    print(image['url'])

ticker = yfinance.Ticker("BTC-USD")
print(ticker.news)


classifier = pipeline('sentiment-analysis')
classifier('the fox crossed the road and got hit by a car and was injured')
for story in news:
  print(story.headline)
  print(classifier(story.summary))