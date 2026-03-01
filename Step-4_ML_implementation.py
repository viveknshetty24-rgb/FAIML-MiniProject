# ------------------------------
# 1. Import Libraries
# ------------------------------
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ------------------------------
# 2. Connect to MongoDB
# ------------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["Electric_Vehicle_project"]
collection = db["ElectricVehicle_data"]

# ------------------------------
# 3. Fetch Data from MongoDB
# ------------------------------
data = list(collection.find())

# ------------------------------
# 4. Convert to DataFrame
# ------------------------------
df = pd.DataFrame(data)

print("First 5 rows from MongoDB:")
print(df.head())

# ------------------------------
# 5. Data Cleaning
# ------------------------------

# Remove unnecessary columns
df = df.drop(columns=["_id", "source_url"], errors='ignore')

# Remove rows with missing values
df = df.dropna()

# Convert categorical columns into numbers (One-Hot Encoding)
df = pd.get_dummies(df, drop_first=True)

# ------------------------------
# 6. Define Features & Target
# ------------------------------
# Target we decided → Driving Range
y = df["range_km"]

# All remaining columns are features
X = df.drop("range_km", axis=1)

# ------------------------------
# 7. Split Data
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------
# 8. Train Model
# ------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------
# 9. Predict
# ------------------------------
y_pred = model.predict(X_test)

# ------------------------------
# 10. Evaluate Model
# ------------------------------
score = r2_score(y_test, y_pred)

print("\nModel Performance")
print("R2 Score:", score)
