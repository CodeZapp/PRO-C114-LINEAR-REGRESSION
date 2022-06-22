import pandas as pd
import plotly.express as px
df = pd.read_csv('main.csv')
TOEFLScore = df['TOEFL Score'].tolist()
chancesOfAdmit = df['Chance of Admit'].tolist()
fig = px.scatter(x = TOEFLScore, y = chancesOfAdmit)
fig.show()
m = 0.01
c = -2.5
y = []
for x in TOEFLScore:
    yValue = m * x + c
    y.append(yValue)
fig = px.scatter(x = TOEFLScore, y = chancesOfAdmit)
fig.update_layout(shapes = [
    dict(type = 'line', 
    y0 = min(y), y1 = max(y),
    x0 = min(TOEFLScore), x1 = max(TOEFLScore)
    )
])
fig.show()
x = 600
y = m * x + c
print(f'Chances of admit of someone based on their TOEFL Score {x} is {y}')
import numpy as np
TOEFLScoreArray = np.array(TOEFLScore)
chanceOfAdmitArray = np.array(chancesOfAdmit)
m, c = np.polyfit(TOEFLScoreArray, chanceOfAdmitArray, 1)
y = []
for x in TOEFLScoreArray:
  yValue = m * x + c
  y.append(yValue)
fig = px.scatter(x = TOEFLScoreArray, y = chanceOfAdmitArray)
fig.update_layout(shapes = [
    dict(
      type = 'line',
      y0 = min(y), y1= max(y),
      x0 = min(TOEFLScoreArray), x1 = max(TOEFLScoreArray)
    )
])
fig.show()
x = 600
y = m * x + c
print(f'Chances of admit of someone based on their TOEFL Score {x} is {y}')