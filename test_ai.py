from ai_recommender import generate_recommendations
sample = {
    "Total": 650,
    "Bill": 5200,
    "AC": 500,
    "Fans": 60,
    "Fridge": 40,
    "TV": 20,
    "LEDs": 10
}
response = generate_recommendations(sample)
print(response)