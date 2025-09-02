import pandas as pd
# SERIES
prices=[2999,39485,67899,4938,4955]
products = ["wireless Earbuds","smartphone","laptop","smartwatch","Bluetooth speaker"]
product_prices = pd.Series(prices,index=products)
print(product_prices)
print("Mean:",product_prices.mean())

print("Sum:",product_prices.sum())

print("Max:",product_prices.max())

print("Min:",product_prices.min())

print("Head/(starting rows):\n",product_prices.head(3))

print("tail/(ending rows):\n",product_prices.tail(2))
#Apply and Map
print(product_prices.apply(lambda x: f'{x-(x*0.2)}'))

print(product_prices.map(lambda x: f'{x}.00'))

print("Sort by values:\n",product_prices.sort_values())

print("Sort by index:\n",product_prices.sort_index())

print("Sort by index:\n",product_prices.sort_index(ascending=False))

print("value Counts:\n",product_prices.value_counts())

# DATAFRAME
data={
    "product":["wireless Earbuds","smartphone","laptop","smartwatch","Bluetooth speaker"],
    "brand":["SoundMax","TechNova","Bytecore","TimeTrack","EchnoBoom"],
    "price":[2999,38774,3874,3834,40000],
    "Stock":[50,30,40,20,60],
    "BestSeller":[True,False,False,True,True],
}
df = pd.DataFrame(data)
print(df)
print("head (first 2 rows)\n",df.head(2))
print("Tail(last 3 rows)\n",df.tail(3))
print("Shape of Dataframe",df.shape)
print("Columns in Dataframe",df.columns)
print("Index of Dataframe",df.index)
print("DataFrame Info")
print(df.info())

print("Statistical Summary:\n",df.describe())

print(df)
print(df.loc[1,"product"])
print(df.loc[3,"Stock"])
print(df.loc[3,"BestSeller"])

print(df.iloc[1,0])
print(df.iloc[3,1])
print(df.iloc[4,2])

print("Select 4 th row \n",df.iloc[4]) #To select entire row
print("Select 3 th row \n",df.iloc[3])

print(df)
print("-----Using loc----\n",df.loc[df['BestSeller']== True])
print("-----Using loc----\n",df.loc[df['Stock']<30])
