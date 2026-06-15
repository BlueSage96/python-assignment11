import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../db/lesson.db")

#Task 2
task2 = """
    SELECT o.order_id, SUM(price * quantity) as total_price
    FROM line_items l
    JOIN orders o
    ON o.order_id = l.order_id
    JOIN products p
    ON p.product_id = l.product_id
    GROUP BY o.order_id  
"""

df = pd.read_sql(task2,conn)

# Add 'total_price' column
def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()
df['cumulative'] = df.apply(cumulative, axis = 1)

df.plot(x="order_id",y="total_price",kind="line",title="Cumulative Revenue by Order ID")
plt.show()