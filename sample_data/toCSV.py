import json
import pandas as pd
keyword_name = 'jamesCharlesCollab'
for i in range(14):
    i = (i+1)*50    
    with open(keyword_name + str(i) + '.json') as json_file:
        data = json.load(json_file)

        df = pd.json_normalize(data.values())
        df.to_csv(keyword_name + str(i) + '.csv', index=False)