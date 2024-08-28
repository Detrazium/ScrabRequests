import pandas as pd
from pathlib import Path

datad = Path('data')

ddf = pd.concat([pd.read_csv(f) for f in datad.glob('*.csv')], ignore_index=True)
ddf.to_csv('data/result_L.csv', index=False)