from pymongo import MongoClient
MONGO_URI = (
    "mongodb://localhost:27017/"
)
client = MongoClient(
    MONGO_URI
)
db = client["ecowatt_ai"]
collection = db["energy_reports"]
def save_report(data):
    collection.insert_one(data)
def get_reports():
    return list(
        collection.find()
    )