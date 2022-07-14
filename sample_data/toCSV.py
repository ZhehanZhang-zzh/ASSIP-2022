import json
import pandas as pd
keyword_name = 'makeupCollab'
for i in range(14):
    i = (i+1)*50    
    with open('makeupCollab' + str(i) + '.json') as json_file:
        data = json.load(json_file)

        df = pd.json_normalize(data.values())
        df.to_csv('makeupCollab' + str(i) + '.csv', index=False)