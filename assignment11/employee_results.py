import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../db/lesson.db")
#Task 1
task1 = """
        SELECT last_name, SUM(price * quantity) AS revenue 
        FROM employees e
        JOIN orders o 
        ON e.employee_id = o.employee_id 
        JOIN line_items l 
        ON o.order_id = l.order_id 
        JOIN products p 
        ON l.product_id = p.product_id 
        GROUP BY e.employee_id;
"""
employee_results = pd.read_sql(task1,conn)
print(employee_results)

employee_results.plot(x="last_name",y="revenue",kind="bar",color="green",title="Employee Results")
plt.show()