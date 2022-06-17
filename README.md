![alt text](https://github.com/johnyg127/TheAPI/raw/main/TheAPI.png)

# Run Example Code

> ## Step 1
> ### Install Required Packages
```py
pip3 install -r requirements.txt
```
> ## Step 2
> ### Add API Keys To The .env File

> ## Step 3
> ### Run Example File
```py
python3 example.py
```

# Use In Code

> ## Step 1
> ### Install Required Packages
```py
pip3 install -r requirements.txt
```
> ## Step 2
> ### Drag The "theapi.py" File To Your Project
> ### Add API Keys To .env
> ### Drag The ".env" File To Your Project


> ## Step 3
> ### In Your Own File, In The Beginning Type The Following:
```py
import theapi
```

> ## Step 4
> ### Choose An API Which You Would Like To Use, And Add It To Your Code:
> #### NewsAPI
```py

# GetEverything:
print(theapi.na_get_everything("bitcoin", 1, "en"))
# GetTopHeadlines:
print(theapi.na_get_top_headlines("bitcoin", "en", "business"))
```
> #### FoodAPI
```py
# SearchGroceryProducts:
print(theapi.fa_search_grocery_products("apple", 1))
# SearchRecipes:
print(theapi.fa_search_recipes("apple", 1))
# SearchIngredients:
print(theapi.fa_search_ingredients("apple", 1))
```
> #### PexelsAPI
```py
# SearchPhotos:
print(theapi.pa_search_photos("apple", 1))
```
> #### FixerAPI
```py
# GetLatestRates:   
print(theapi.fix_get_latest_rates("USD"))
```
> #### WeatherAPI
```py
# GetCurrentWeather:
print(theapi.wa_get_current_weather("New York"))
```
# ❗ IMPORTANT! Make Sure To Add An API Key For Every API Which You Use And Requires One!
