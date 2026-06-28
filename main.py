import pandas as pd

# creating the dataframes
df_0 = pd.read_csv('data/daily_sales_data_0.csv')
df_1 = pd.read_csv('data/daily_sales_data_1.csv')
df_2 = pd.read_csv('data/daily_sales_data_2.csv')

df = pd.concat([df_0, df_1, df_2], ignore_index = True)

# filtering only the pink morsel
pink_df = df[df['product'] == 'pink morsel']

pink_df['price'] = pink_df['price'].str.replace('$', '').str.replace('.', '')

pink_df['price'] = pink_df['price'].astype('float')

# adjusting the price columns and removing the unnecessary columns
pink_df['price'] = pink_df['price'] /100

pink_df['sales'] = pink_df['price'] * pink_df['quantity']

pink_df = pink_df.drop(columns=['product', 'price', 'quantity'])

# reordering the columns
pink_df = pink_df[['sales', 'date', 'region']]

#print(pink_df.sample(5))
#exporting as csv
pink_df.to_csv('pink_df.csv', index =False)
print('created pink_df.csv')
