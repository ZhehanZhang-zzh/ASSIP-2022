import json
import pandas as pd

project_file = "beauty_fenty.csv"

with open('beauty_fenty.json') as project_file:    
    data = json.load(project_file)  

df = pd.json_normalize(data)
df.to_csv(project_file, encoding='utf-8')