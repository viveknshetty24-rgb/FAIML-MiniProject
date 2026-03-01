from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access database
db = client["Electric_Vehicle_project"]

# Access collection
collection = db["ElectricVehicle_data"]

# Fetch data
data = list(collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

print(df.head())
