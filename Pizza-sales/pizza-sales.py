import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile('./data-pizza.xlsx')
dfs = pd.read_excel(xls, sheet_name=None)

df_pizza_types = dfs["pizza_types"]
df_pizzas = dfs["pizzas"]
df_order_details = dfs["order_details"]
df_orders = dfs["orders"]

df_pizza_types_stats = df_pizza_types.describe()
df_pizza_types_info = df_pizza_types.info()

df_pizzas_stats = df_pizzas.describe()
df_pizzas_types_info = df_pizzas.info()

df_order_details_stats = df_order_details.describe()
df_order_details_info = df_order_details.info()

df_orders_stats = df_orders.describe()
df_orders_info = df_orders.info()

merge_df = pd.merge(df_orders, df_order_details, on='order_id')
merge_df2 = pd.merge(merge_df, df_pizzas, on='pizza_id')
big_df = pd.merge(merge_df2, df_pizza_types, on='pizza_type_id')

big_df_stats = big_df.describe()
big_df_info = big_df.info()

#Înlocuim valorile NaN cu 0
big_df.fillna(0, inplace=True)

ingredients_split = big_df['ingredients'].str.split(',').explode()
ingredient_counts = ingredients_split.value_counts()
most_common_ingredient = ingredient_counts.idxmax()
print("Cel mai folosit ingredient:", most_common_ingredient)

cheese_types = ingredients_split[ingredients_split.str.contains(r'\bcheese\b', case=False)]
num_cheese_types = cheese_types.nunique()
print("Numărul de tipuri de brânză:", num_cheese_types)
print("Tipurile de brânză găsite:")
for cheese_type in cheese_types.unique():
    print(cheese_type)


pizza_vandute = big_df.groupby(["pizza_type_id", "size"])["quantity"].sum()
print("Cantitatea de pizza vanduta: ")
print(pizza_vandute)
pizza_sales = big_df.groupby(["pizza_type_id", "size"])["price"].sum()
print("Total vanzari de pizza: ")
print(pizza_sales)

top_5_pizzas = big_df['pizza_type_id'].value_counts().nlargest(5)
print("Top 5 pizza vandute:")
print(top_5_pizzas)

top_5_nevadute = big_df['pizza_type_id'].value_counts().nsmallest(5)
print("Top 5 pizza nevandute:")
print(top_5_nevadute)

pizza_stats = big_df.groupby(["size"])["price"].describe()
print("Statisticile pentru fiecare marime de pizza:")
print(pizza_stats)


plt.hist(big_df['price'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Pizza Prices')
plt.show()
#Cea mai cumparat pizza este cea la 22 de lei fiind apropae de 14000 de aparitii, adica 14000 de clienti dorind aceasta pizza, iar cea mai putin cumparata fiind pe la 24 de lei, cu aproximativ 1000 de paratii, adica o difenta de 140%.

#Am date numai din anum 2015
total_revenue = big_df["price"].sum()
print("Total revenue 2015:")
print(total_revenue)


revenue_by_month = big_df.groupby(big_df['date'].dt.month)['price'].sum()
print("Profitul obtinut pe fiecare luna din 2015:")
print(revenue_by_month)

plt.figure(figsize=(10, 6))
revenue_by_month.plot(kind='bar', color='salmon')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Profitul obtinut pe fiecare luna din 2015')
plt.show()
#Din grafic putem observa ca in luna a 7 a adica luna iulie, s-a abtinut cel mia mare profit de 71027.45, iar in luna 10, octombrie, cel mai muc de 62566.50
#Intre acestea profitul a variat cu cateva mii de lei de la luna la luna pana in luna august in care este un declin putin mai de durata pana in luna 10, iafr din luna 11 incepe sa isi revina la normal
#Chiar daca variaza profitul a ramas mereu intre 6000 si 7000


order_frequency = big_df.groupby(big_df['date'].dt.to_period('M')).size()

plt.figure(figsize=(10, 6))
plt.plot(order_frequency.index.to_timestamp(), order_frequency.values, marker='o', color='b', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Number of Orders')
plt.title('Order Frequency Over Time')
plt.show()
#Profitul variata de la luna la luna
#Din 2015-01 a scazut in 2015-02, iar in 2015-03 a crescut la loc, mai bine decat in prima luna si acest lucru determina fluctuatia profitului aceste pizzeri
#Cel mai mare punct ajungand la momentul 2015-07 dupa care a avut loc un declin destul de evident pana in 2015-10, cum am explicat si in graficul anterior
#Anul s-a teminat cu un  profit mult mai mic decat a inceput, chiar daca cu o luna inainte a avut loc o crestere considerabila


total_orders = len(big_df["order_id"])
print("Total orders:")
print(total_orders)

orders_day = total_orders/365
print("Total orders per day:")
print(round(orders_day))


orders_by_date = big_df.groupby('date').size()
print("Totalul de comenzi pentru fiecare zi în parte:")
print(orders_by_date)

zi_comenzi = orders_by_date.idxmax()
print("Ziua cu cele mia multe comezi:")
print(zi_comenzi)

plt.figure(figsize=(10, 6))
plt.plot(orders_by_date.index, orders_by_date.values, marker='o', color='b', linestyle='-')
plt.xlabel('Zi')
plt.ylabel('Total comenzi')
plt.title('Totalul de comenzi pentru fiecare zi în parte')
plt.show()


revenue_by_day = big_df.groupby(big_df['date'].dt.day)['price'].sum()
print("Profitul obtinut pe fiecare zi din 2015:")
print(revenue_by_day)

zi_price = revenue_by_day.idxmax()
print("Ziua cu cel mai mult profit:")
print(zi_price)

# Calculate the time difference between consecutive orders
time_diff = big_df['date'].diff()

# Identify periods of time where no orders were placed
no_orders_periods = time_diff[time_diff > pd.Timedelta(days=1)]
print("Periods of time where no orders were placed:")
print(no_orders_periods)

