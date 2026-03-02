from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def build_datapath(dataset):
    return {
        key: os.path.join(PROJECT_ROOT, "data", filename) for key, filename in dataset.items()
    }


# define datasets
datasets = build_datapath({
    # Frequency: 10 min / Dataset: weather
    "weather_10_min": "weather.csv",
})