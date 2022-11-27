#Nesting
capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

#Nesting a list in a dicitionary

travel_log1 = {
    "France": ["Paris", "Lille","Dijon"], # Value and list at the end
    "Germany": ["Berlin","Hamburg","Stuttgart"],
}

#Dictionary within a dictionary - Example
travel_log = {
    "France": {"Cities_visited": ["Paris", "Lille","Dijon"], "total_visits": 12}, #A key with a dictionary with a list within it
    "Germany":{"Cities_visited":  ["Berlin","Hamburg","Stuttgart"], "money_spend_in_euro": 1800},
}
