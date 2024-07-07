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
                # First line
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[1, 4, 9, 16, 25],
                    mode='lines+markers',
                    name='Line with Markers'
                ),
                # Second line
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[1, 3, 6, 10, 15],
                    mode='lines',
                    name='Line without Markers',
                    line=dict(color='firebrick', width=2, dash='dash')
                ),
                # Third line
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[1, 2, 4, 8, 16],
                    mode='lines+markers',
                    name='Another Line with Markers',
                    marker=dict(symbol='star', size=10, color='orange')
                )
            ],
            'layout': go.Layout(
                title='Complex Line Plot',
                xaxis={'title': 'X Axis'},
                yaxis={'title': 'Y Axis'},
            )
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
