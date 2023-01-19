#Develop a data ingestion pipeline to ingest emission Data

import pandas as pd 
import numpy as np
import requests
url = "https://example.com/emissionData"
response = requests.get(url)
df = pd.read_csv(response.content)
print(df.head())
cleanedDf = df.dropna()
print(cleanedDf.head())
cleanedDf.to_csv('emissionData.csv', index=False)
