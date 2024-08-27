
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting List in a Dictionary
travel_log_using_lists = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Pulling an item from a List that is in a Dictionary
print(travel_log_using_lists["France"][1])

# Nesting List in a List
nested_list = ["A", "B", ["C", "D"]]

# Pulling an item from a List that is in a List
print(nested_list[2][1])

# Nesting Dictionary in a Dictionary
travel_log_using_dictionaries = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 1,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 2,
    },
}

# Pulling an item from a List in a Dictionary in another Dictionary
print(travel_log_using_dictionaries["Germany"]["cities_visited"][2])
