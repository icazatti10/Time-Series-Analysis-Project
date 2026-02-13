from registry.data_registry import datasets
import pandas as pd

filename = datasets.get("weather_10_min")
df = pd.read_csv(filename)
print(df.head())