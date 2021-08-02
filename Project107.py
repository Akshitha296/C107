import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data107.csv")

print(df.groupby("level")["attempt"].mean())

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean() 

fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")

fig.show()
