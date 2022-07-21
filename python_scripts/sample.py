import argparse
import json
import numpy as np
import pprint
import csv
import pandas as pd

filename = '/Users/arnav/Desktop/YouTube Code/ASSIP-2022/full_data/gaming_filtered.csv'
csvfile = pd.read_csv(filename)
game_data = csvfile.sample(n=100)
game_data.to_csv('game_data1.csv')