# List comprehension
menu = [
    "Chai",
    "Coffee",
    "Tea"
]

tea = [tea for tea in menu if "Chai" in tea]
print(tea)

# Set comprehension


menu = [
    "Chai",
    "Coffee",
    "Tea",
    "chai",
]

tea = {tea for tea in menu if "Chai" in tea}
print(tea)

unique_tea = {chai for chai in menu}
print(unique_tea)

recipie = {
    "masala chai": ["spicy", "sweet", "hot"],
    "Elachi chai": ["elaichi", "sweet"],
    "spicy chai": ["tasty", "sweet", "hot"],
}

unique_chai = {spices for ingredient in recipie.values() for spices in ingredient}
print(unique_chai)

# Dictionary comprehension

tea_prices_rs = {
    "Chai": 20,
    "Coffee": 30,
    "Lemon_tea": 25,
}

Tea_prices_usd = {tea:price /80 for tea, price in tea_prices_rs.items()}
print(Tea_prices_usd)

#Generator comprehension
daily_sales = [100, 200, 300, 400, 500]

total_cup = (sale for sale in daily_sales if sale > 200)
print(sum(total_cup))
print(list(total_cup))