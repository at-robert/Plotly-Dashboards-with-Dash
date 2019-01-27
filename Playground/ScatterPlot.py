
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)
data = [go.Scatter(x=random_x,y=random_y,mode='markers',)]
layout = go.Layout(title='Hello Scatter Plot',
                    xaxis={'title':'My X axis'},
                    yaxis=dict(title='My Y axis'),
                    hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(data, filename='scatter.html')