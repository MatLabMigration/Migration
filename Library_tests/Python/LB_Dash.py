import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# Generate random data points
num_points = 20
x = np.arange(1, num_points + 1)
y1 = np.random.randint(5, 15, num_points)  # Oxygen levels
y2 = np.random.randint(70, 120, num_points)  # Blood pressure

# Create Dash app
app = dash.Dash(__name__)

# Define layout of the app
app.layout = html.Div([
    html.H1("Zuurstof en bloeddruk (Dash)"),
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                # Scatter plot for oxygen levels
                go.Scatter(
                    x=x,
                    y=y1,
                    mode='markers+lines',
                    name='Zuurstof',
                    marker=dict(color='blue', size=8)
                ),
                # Scatter plot for blood pressure
                go.Scatter(
                    x=x,
                    y=y2,
                    mode='markers+lines',
                    name='Bloeddruk',
                    marker=dict(color='red', size=8)
                )
            ],
            'layout': {
                'xaxis': {'title': 'Tijd'},
                'yaxis': {'title': 'Waarde'},
                'legend': {'x': 0, 'y': 1},
                'hovermode': 'closest'
            }
        }
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
