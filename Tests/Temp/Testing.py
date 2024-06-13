import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import numpy as np
import dash_bootstrap_components as dbc

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define app layout
app.layout = dbc.Container([
  html.H1("Maternal-Fetal Simulation", className="mb-4"),

  dbc.Row([
    dbc.Col([
      html.Div([
        html.Label("Mother (1 = present; 0 = not present)"),
        dcc.Input(id='input-mother', type='number', value=1, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Uterus (1 = present; 0 = not present)"),
        dcc.Input(id='input-uterus', type='number', value=1, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Foetus (1 = present; 0 = not present)"),
        dcc.Input(id='input-foetus', type='number', value=1, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Umbilical (1 or 2)"),
        dcc.Input(id='input-umbilical', type='number', value=2, className="mb-3"),
      ]),
    ], md=3),
  ]),

  dbc.Row([
    dbc.Col([
      html.Div([
        html.Label("Brain (1 = present; 0 = not present)"),
        dcc.Input(id='input-brain', type='number', value=1, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("CAVmodel (1=TVE, 2=1fiber, 3=testcombi, 5=1fibernew)"),
        dcc.Input(id='input-CAVmodel', type='number', value=2, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Scen (0=normaal CTG; 1=vroege decels; 2=late decels; 3=variabele decels)"),
        dcc.Input(id='input-scen', type='number', value=2, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("HES (1=fluid bolus (500 mL HES); 0=not)"),
        dcc.Input(id='input-HES', type='number', value=0, className="mb-3"),
      ]),
    ], md=3),
  ]),

  dbc.Row([
    dbc.Col([
      html.Div([
        html.Label("Persen (1=meepersen; 0=niet)"),
        dcc.Input(id='input-persen', type='number', value=0, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Duty (1=wel; 0=geen duty cycles)"),
        dcc.Input(id='input-duty', type='number', value=0, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Ncyclemax (maximum number of maternal cycles)"),
        dcc.Input(id='input-ncyclemax', type='number', value=1000, className="mb-3"),
      ]),
    ], md=3),
    dbc.Col([
      html.Div([
        html.Label("Lamb (0=Het is een foetus; 1=PAS OP: lammetje)"),
        dcc.Input(id='input-lamb', type='number', value=0, className="mb-3"),
      ]),
    ], md=3),
  ]),

  html.Button('Submit', id='submit-button', n_clicks=0, className="mt-3"),

  dcc.Graph(id='live-update-graph', className="mt-4")
], className="p-4")


# Callback to update graph
@app.callback(Output('live-update-graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('input-mother', 'value'),
               State('input-uterus', 'value'),
               State('input-foetus', 'value'),
               State('input-umbilical', 'value'),
               State('input-brain', 'value'),
               State('input-CAVmodel', 'value'),
               State('input-scen', 'value'),
               State('input-HES', 'value'),
               State('input-persen', 'value'),
               State('input-duty', 'value'),
               State('input-ncyclemax', 'value'),
               State('input-lamb', 'value')])
def update_graph(n_clicks, mother, uterus, foetus, umbilical, brain, CAVmodel, scen, HES, persen, duty, ncyclemax, lamb):
    if n_clicks > 0:
        # Perform simulation based on submitted parameters
        t = np.linspace(0, ncyclemax, 100)  # Time array
        mV = np.random.normal(100, 10, 100)  # Maternal volume (random data for demo)
        mp = np.random.normal(80, 5, 100)  # Maternal pressure (random data for demo)
        mq = np.random.normal(50, 3, 100)  # Maternal flow (random data for demo)

        # Create traces
        traces = [
            go.Scatter(
                x=t,
                y=mV,
                mode='lines+markers',
                name='Maternal Volume'
            ),
            go.Scatter(
                x=t,
                y=mp,
                mode='lines+markers',
                name='Maternal Pressure'
            ),
            go.Scatter(
                x=t,
                y=mq,
                mode='lines+markers',
                name='Maternal Flow'
            )
        ]

        # Create layout
        layout = go.Layout(
            title='Maternal-Fetal Simulation',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Value')
        )

        return {'data': traces, 'layout': layout}
    else:
        # Default empty graph
        return {'data': [], 'layout': {}}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
