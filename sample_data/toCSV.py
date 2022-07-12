import json
import pandas as pd

with open('beauty_makeupCollab.json') as json_file:
    data = json.load(json_file)

    df = pd.json_normalize(data.values())
    df.to_csv("beauty_makeupCollab.csv", index=False)