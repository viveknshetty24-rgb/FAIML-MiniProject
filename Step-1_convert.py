import pandas as pd

df = pd.read_csv("electric_vehicles_spec_2025.csv")

# Convert to JSON
df.to_json("Electric_vehicle.json", orient="records")

print("CSV converted to JSON successfully!")
