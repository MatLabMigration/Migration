import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[1, 4, 9, 16, 25],
                    mode='lines+markers',
                    name='Line with Markers'
                )
            ],
            'layout': go.Layout(
                title='Simple Line Plot',
                xaxis={'title': 'X Axis'},
                yaxis={'title': 'Y Axis'},
            )
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
