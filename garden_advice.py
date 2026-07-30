# Advice for each season, keyed by season name.
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
    "spring": "Watch for weeds and start planting new seedlings.\n",
    "autumn": "Clear fallen leaves and mulch your beds.\n",
}

# Advice for each plant type, keyed by plant type name.
PLANT_TYPE_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Keep soil well-drained and harvest regularly.",
}


def get_season_advice(season):
    """Look up advice for the given season, with a fallback message."""
    return SEASON_ADVICE.get(season, "No advice for this season.\n")


def get_plant_type_advice(plant_type):
    """Look up advice for the given plant type, with a fallback message."""
    return PLANT_TYPE_ADVICE.get(plant_type, "No advice for this type of plant.")


def get_advice(season, plant_type):
    """Combine season and plant type advice into a single message."""
    return get_season_advice(season) + get_plant_type_advice(plant_type)


def main():
    season = input("Enter the season (summer/winter/spring/autumn): ")
    plant_type = input("Enter the plant type (flower/vegetable/herb): ")
    print(get_advice(season, plant_type))


if __name__ == "__main__":
    main()

# TODO: Recommend plants based on the entered season.
