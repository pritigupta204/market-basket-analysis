import pandas as pd


df = pd.read_csv('output_market_basket.csv')

print(type(list(df['antecedents'].unique())))