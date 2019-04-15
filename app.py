import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


def app_deploy(plopper_df):

    src_port_df = plopper_df.groupby(['Source Port']).size().reset_index(name='Count').nlargest(10, 'Count')
    src_port_df['Source Port'].apply(str)

    event_df = plopper_df.groupby(['Event']).size().reset_index(name='Count').nlargest(10, 'Count')

    classification_df = plopper_df.groupby(['Classification']).size().reset_index(name='Count').nlargest(10, 'Count')

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Link", href="#"))
        ],
        brand="Plopper",
        brand_href="#",
        sticky="top"
    )

    body = dbc.Container([
        dbc.Col([
            html.H2("Dashboard"),
            dt.DataTable(
                id="Plopper Data",
                columns=[{"name": i, "id": i} for i in plopper_df.columns],
                n_fixed_rows=1,
                style_cell={'width': '100%'},
                data=plopper_df.to_dict("rows"),

            )
        ]),
        dcc.Graph(
            id='src_port',
            figure={
                'data': [go.Bar(
                    x=src_port_df['Source Port'],
                    y=src_port_df['Count'],
                )
                ],
                'layout': go.Layout(
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='event',
            figure={
                'data': [go.Bar(
                    x=event_df['Event'],
                    y=event_df['Count'],
                )
                ],
                'layout': go.Layout(
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='classification',
            figure={
                'data': [go.Bar(
                    x=classification_df['Classification'],
                    y=classification_df['Count'],
                )
                ],
                'layout': go.Layout(
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])

    app.layout = html.Div([navbar, body])

    app.run_server(debug=True)
