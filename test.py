import pandas as pd


df = pd.read_csv('output_market_basket.csv')
df1 = df[['antecedents', 'consequents', 'support','confidence','lift']]
# print(df1.head())
df2 = df1.loc[df['antecedents'] == "Apple"]
df2 = df2.sort_values(by='lift', ascending=False)
# print(df2)

data = df2.to_dict('records')

temp = []
final_op = []

for i in data:
    if i.get('consequents') in temp:
        continue
    final_op.append(i)

    if len(final_op) > 2:
        break

print(final_op)