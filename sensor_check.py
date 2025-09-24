
    

import pandas as pd

# Fake sensor data – speed in mph, distance in feet
data = pd.DataFrame({
    'speed': [30, 45, 20],
    'distance': [100, 150, 50]
})

# Loop through each row and check if safe
for index, row in data.iterrows():
    if row['distance'] > row['speed'] * 2:
        status = "safe"
    else:
        status = "danger!"
    print(f"Speed {row['speed']} mph | Distance {row['distance']} ft | Verdict: {status}")
