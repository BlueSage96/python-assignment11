import plotly.express as px
import plotly.data as pldata
import pandas as pd

#Task 3
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

#Cleanup
df['strength'] = (df['strength']).astype(str).str.replace("-",".",regex=False).str.replace("+",".",regex=False)
df['strength'] = pd.to_numeric(df['strength'],downcast="float",errors="coerce")

# Scatter plot
wind = px.scatter(df, x="strength",y="frequency",color="direction",title="Wind Strength vs Wind Frequency")
wind.write_html("wind.html",auto_open=True)