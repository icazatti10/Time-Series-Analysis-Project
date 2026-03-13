from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def build_datapath(dataset):
    return {
        key: os.path.join(PROJECT_ROOT, "data", filename) for key, filename in dataset.items()
    }


# define datasets
datasets = build_datapath({
    # Frequency: 10 min / Dataset: weather / A.Icazatti
    "weather_10_min": "weather.csv",
    "weather_15_min_v1": "NEW-DATA-1.T15.txt",
    "weather_15_min_v2": "NEW-DATA-2.T15.txt",
    "snow_daily": "BogusSnowDaily.csv",
    "power_5_min": "household_power_consumption.txt",
    "electricity_1_h": "electricity.csv",
    "stock": "stock.csv"
})
