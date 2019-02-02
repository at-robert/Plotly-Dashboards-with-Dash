#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()


# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        marks={i: '{}'.format(i) for i in range(10)},
        min=0,
        max=10,
        step=1,
        value=5,
    ),
    html.Div(style={'paddingTop':35}),
    dcc.Slider(
        id='my-slider1',
        marks={i: '{}'.format(i) for i in range(-10,0)},
        min=-10,
        max=0,
        step=1,
        value=-5,
    ),
    # html.Hr(),  # add a horizontal rule
    html.Div(style={'paddingTop':35}),
    html.Div(id='slider-output-container', style={'paddingTop':35})
])


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value'),
     dash.dependencies.Input('my-slider1','value')])
def update_output(value,value1):
    return '"{} * {} = {}"'.format(value,value1,value*(value1))


# Create a Dash callback:

# Add the server clause:
if __name__ == '__main__':
    app.run_server()