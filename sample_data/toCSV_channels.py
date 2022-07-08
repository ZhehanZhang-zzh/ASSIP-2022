import json
import pandas as pd

with open('beauty_channels.json') as json_file:
    data = json.load(json_file)

    df = pd.json_normalize(data.values())
    df.to_csv("beauty_channels.csv", index=False)