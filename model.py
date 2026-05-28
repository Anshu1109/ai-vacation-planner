import pandas as pd
import random

# Load dataset
data = pd.read_csv("dataset/destinations.csv")

def recommend_destination(user_type, user_budget, user_season):

    filtered = data[
        (data["Type"] == user_type) &
        (data["Budget"] == user_budget) &
        (data["Season"] == user_season)
    ]

    if filtered.empty:
        filtered = data[data["Type"] == user_type]

    if filtered.empty:
        return {
            "Destination": "No match found",
            "Activities": "Try different options",
            "Hotel": "N/A",
            "Travel_Mode": "N/A"
        }

    result = filtered.sample().iloc[0]

    return {
        "Destination": result["Destination"],
        "Activities": result["Activities"],
        "Hotel": result["Hotel"],
        "Travel_Mode": result["Travel_Mode"]
    }