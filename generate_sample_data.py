import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("Generating synthetic e-commerce data...")

num_customers = 5000
states = ['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']
customers = pd.DataFrame({
    'CustomerID': range(1, num_customers + 1),
    'CustomerState': np.random.choice(states, num_customers)
})

categories = ['Electronics', 'Home Appliances', 'Clothing', 'Books', 'Sports', 'Toys']
products = pd.DataFrame({
    'ProductID': range(101, 151),
    'ProductCategory': np.random.choice(categories, 50),
    'BasePrice': np.random.uniform(15.0, 500.0, 50).round(2)
})

num_orders = 15000
start_date = datetime(2023, 1, 1)

order_data = []
for i in range(1, num_orders + 1):
    cust_id = random.randint(1, num_customers)
    prod_id = random.randint(101, 150)
    base_price = products.loc[products['ProductID'] == prod_id, 'BasePrice'].values[0]
    final_price = round(base_price * random.uniform(0.9, 1.1), 2)
    
    purchase_days_add = random.randint(0, 360)
    purchase_date = start_date + timedelta(days=purchase_days_add)
    
    est_delivery_days = random.randint(3, 10)
    est_delivery = purchase_date + timedelta(days=est_delivery_days)
    
    if random.random() < 0.9:
        actual_delivery = purchase_date + timedelta(days=random.randint(2, est_delivery_days))
    else:
        actual_delivery = est_delivery + timedelta(days=random.randint(1, 5))
        
    order_data.append([i, cust_id, prod_id, final_price, purchase_date, est_delivery, actual_delivery])

orders = pd.DataFrame(order_data, columns=[
    'OrderID', 'CustomerID', 'ProductID', 'Price', 
    'PurchaseDate', 'EstimatedDeliveryDate', 'DeliveryDate'
])

customers.to_csv('customers.csv', index=False)
products.to_csv('products.csv', index=False)
orders.to_csv('orders.csv', index=False)

print("Data generation complete! 3 CSV files created.")
