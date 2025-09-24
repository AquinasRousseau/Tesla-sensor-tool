
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/sensor_check")
def sensor_check(speed: float, distance: float):
    # Fake sensor data processing with your loop logic
    data = pd.DataFrame({"speed": [speed], "distance": [distance]})
    for index, row in data.iterrows():
        if row['distance'] > row['speed'] * 2:
            status = "safe"
        else:
            status = "danger!"
    return {"speed": speed, "distance": distance, "verdict": status}
