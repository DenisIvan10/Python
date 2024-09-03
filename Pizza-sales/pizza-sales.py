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

#Replace NaN values with 0
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
#The most purchased pizza is the one priced at 22 lei, with nearly 14,000 orders, meaning 14,000 customers wanted this pizza. The least purchased one is priced at 24 lei, with approximately 1,000 orders, showing a difference of 140%.

#Data only from 2015
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

#From the graph we can see that in the 7th month, July, the biggest profit of 71027.45 was made, and in the 10th month, October, the smallest of 62566.50
#Among these, the profit varied by a few thousand lei from month to month until August, in which there is a slightly longer decline until month 10, since from month 11 it starts to return to normal
#Even if the profit varies, it always remained between 6000 and 7000


order_frequency = big_df.groupby(big_df['date'].dt.to_period('M')).size()

plt.figure(figsize=(10, 6))
plt.plot(order_frequency.index.to_timestamp(), order_frequency.values, marker='o', color='b', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Number of Orders')
plt.title('Order Frequency Over Time')
plt.show()
#Profit varies from month to month
#From 2015-01 it decreased in 2015-02, and in 2015-03 it increased again, better than in the first month and this determines the fluctuation of the profit of these pizzerias
#The highest point reaching the moment 2015-07, after which there was a fairly obvious decline until 2015-10, as I explained in the previous graph
#The year ended with a much lower profit than it started, even though a month before there was a considerable increase


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

