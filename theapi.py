#Required Packages:
from dotenv import dotenv_values
import requests
import json

#API Packages:
from newsapi import NewsApiClient

#Config For .env:
config = dotenv_values(".env")

#API Initialization:
newsapi = NewsApiClient(api_key=config["newsapiKEY"])


#NewsAPI Functions:
def na_get_everything(query, page, language):
    return newsapi.get_everything(q=query,
    language=language,
    sort_by='relevancy',
    page=page)
def na_get_top_headlines(query, language, category):
    return newsapi.get_top_headlines(q=query,
    language=language, category=category)

#FoodAPI Functions:
def fa_search_grocery_products(query, number):
    return json.loads(requests.get("https://api.spoonacular.com/food/products/search?query=" + query + "&number=" + str(number) +"&apiKey=" + config["foodapiKEY"]).text)
def fa_search_recipes(query, number):
    return json.loads(requests.get("https://api.spoonacular.com/recipes/complexSearch?query=" + query + "&number=" + str(number) + "&apiKey=" + config["foodapiKEY"]).text)
def fa_search_ingredients(query, number):
    return json.loads(requests.get("https://api.spoonacular.com/food/ingredients/search?query=" + query + "&number=" + str(number) + "&apiKey=" + config["foodapiKEY"]).text)

#PexelsAPI Functions:
def pa_search_photos(query, per_page):
    return json.loads(requests.get(f'https://api.pexels.com/v1/search?query={query}e&per_page={per_page}').text)


#FixerAPI Functions:
def fix_get_latest_rates(symbols):
    return json.loads(requests.get(f'https://api.apilayer.com/fixer/latest?symbols={symbols}', headers={"apikey":config["fixerapiKEY"]}).text)


#WeatherAPI Functions:
def wa_get_current_weather(query):
    return json.loads(requests.get(f'http://api.weatherapi.com/v1/current.json?key={config["weatherapiKEY"]}&q={query}').text)
