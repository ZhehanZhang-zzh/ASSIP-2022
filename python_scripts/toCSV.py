import json
import pandas as pd

with open('channels.json') as json_file:
    data = json.load(json_file)

    df = pd.json_normalize(data.values())
    df.to_csv("channels.csv", index=False)