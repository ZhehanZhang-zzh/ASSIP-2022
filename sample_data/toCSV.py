import json
import pandas as pd

<<<<<<< HEAD
with open('beauty_tati.json') as json_file:
    data = json.load(json_file)

    df = pd.json_normalize(data.values())
    df.to_csv("beauty_tati.csv", index=False)
=======
with open('beauty_makeup.json') as json_file:
    data = json.load(json_file)

    df = pd.json_normalize(data.values())
    df.to_csv("beauty_makeup.csv", index=False)
>>>>>>> 44749f7899c7be6b58fbab096946d96505aaf1cc
