import theapi


#NewsAPI: 

# GetEverything:
print(theapi.na_get_everything("bitcoin", 1, "en"))
# GetTopHeadlines:
print(theapi.na_get_top_headlines("bitcoin", "en", "business"))




#FoodAPI:

# SearchGroceryProducts:
print(theapi.fa_search_grocery_products("apple", 1))
# SearchRecipes:
print(theapi.fa_search_recipes("apple", 1))
# SearchIngredients:
print(theapi.fa_search_ingredients("apple", 1))




#PexelsAPI:

# SearchPhotos:
print(theapi.pa_search_photos("apple", 1))




#FixerAPI:

# GetLatestRates:   
print(theapi.fix_get_latest_rates("USD"))




#WeatherAPI:

# GetCurrentWeather:
print(theapi.wa_get_current_weather("New York"))