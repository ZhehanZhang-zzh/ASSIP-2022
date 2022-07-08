import json
import pandas as pd

with open('game_valorant_videos.json') as json_file:
    data = json.load(json_file)

    df = pd.json_normalize(data.values())
    df.to_csv("game_valorant.csv", index=False)