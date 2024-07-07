import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Initialiseer de Dash-app met Bootstrap stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definieer de layout van de app
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Naam Combinator", className="text-center mt-4 mb-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                [
                    dcc.Input(
                        id='first-name',
                        type='text',
                        placeholder='Voornaam',
                        className='form-control mb-3',
                        style={'width': '80%', 'margin': '0 auto'}
                    ),
                    dcc.Input(
                        id='last-name',
                        type='text',
                        placeholder='Achternaam',
                        className='form-control mb-3',
                        style={'width': '80%', 'margin': '0 auto'}
                    ),
                    html.Button(
                        'Combineren',
                        id='combine-button',
                        className='btn btn-primary',
                        style={'width': '80%', 'margin': '0 auto', 'display': 'block'}
                    ),
                ],
                width=6,
                className="mx-auto text-center"
            ),
            className="mb-4"
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Gecombineerde Naam")),
                dbc.ModalBody(id='modal-body'),
                dbc.ModalFooter(
                    dbc.Button("Sluiten", id="close", className="ms-auto", n_clicks=0)
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ],
    className="p-4"
)

# Definieer de callback om de modal bij te werken
@app.callback(
    Output('modal', 'is_open'),
    Output('modal-body', 'children'),
    Input('combine-button', 'n_clicks'),
    Input('close', 'n_clicks'),
    State('first-name', 'value'),
    State('last-name', 'value'),
    State('modal', 'is_open'),
)
def combine_names(n_clicks_combine, n_clicks_close, first_name, last_name, is_open):
    if n_clicks_combine or n_clicks_close:
        if n_clicks_combine > 0 and first_name and last_name:
            combined_name = f"{first_name} {last_name}"
            return not is_open, combined_name
        return not is_open, ''
    return is_open, ''

# Start de app
if __name__ == '__main__':
    app.run_server(debug=True)
