import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


def app_deploy(plopper_df):

    # DataFrames Splits and Groups

    src_port_df = plopper_df.groupby(['Source Port']).size().reset_index(name='Count').nlargest(10, 'Count')
    src_port_df['Source Port'].apply(str)

    src_ip_df = plopper_df.groupby(['Source IP']).size().reset_index(name='Count').nlargest(10, 'Count')

    dest_port_df = plopper_df.groupby(['Destination Port']).size().reset_index(name='Count').nlargest(10, 'Count')
    dest_port_df['Destination Port'].apply(str)

    dest_ip_df = plopper_df.groupby(['Destination IP']).size().reset_index(name='Count').nlargest(10, 'Count')

    event_df = plopper_df.groupby(['Event']).size().reset_index(name='Count').nlargest(10, 'Count')

    classification_df = plopper_df.groupby(['Classification']).size().reset_index(name='Count').nlargest(10, 'Count')

    event_by_time = plopper_df[['time', 'Event']]

    unique_ips = plopper_df.groupby(['Destination IP']).size().count()

    count_of_events = plopper_df.groupby(['Event']).size().count()

    count_of_classes = plopper_df.groupby(['Classification']).size().count()

    # Web Application

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Navbar setup
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Link", href="#"))
        ],
        brand="Plopper",
        brand_href="#",
        sticky="top"
    )

    # body setup
    body = dbc.Container([
        dbc.Row([
            html.H2("Dashboard")
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("Unique IPs"),
                html.H3(unique_ips)
            ], width=4, style={'background-color': 'ff0000'}),
            dbc.Col([
                html.H3("Types of Events"),
                html.H3(count_of_events)
            ], width=4),
            dbc.Col([
                html.H3("Total Classifications"),
                html.H3(count_of_classes)
            ], width=4),
        ]),
        dbc.Row([
            html.H3("Timeline of Events"),
            dbc.Col([
                dcc.Graph(
                    id='Event-by-time',
                    figure={
                        'data': [go.Histogram(
                            x=event_by_time['time'],
                            y=event_by_time['Event'],
                        )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                )
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("Source IP"),
                dcc.Graph(
                    id='src_ip',
                    figure={
                        'data': [go.Bar(
                            x=src_ip_df['Source IP'],
                            y=src_ip_df['Count'],
                        )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                ),
                dbc.Table.from_dataframe(src_ip_df, striped=True, bordered=True, hover=True)
            ], width=6),
            dbc.Col([
                html.H3("Source Port"),
                dcc.Graph(
                    id='src_port',
                    figure={
                        'data': [go.Pie(
                            labels=src_port_df['Source Port'],
                            values=src_port_df['Count'],
                        )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                ),
                dbc.Table.from_dataframe(src_port_df, striped=True, bordered=True, hover=True)
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("Destination IP"),
                dcc.Graph(
                    id='dest_ip',
                    figure={
                        'data': [go.Bar(
                            x=dest_ip_df['Destination IP'],
                            y=dest_ip_df['Count'],
                        )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                ),
                dbc.Table.from_dataframe(dest_ip_df, striped=True, bordered=True, hover=True)
            ], width=6),
            dbc.Col([
                html.H3("Destination Port"),
                dcc.Graph(
                    id='dest_port',
                    figure={
                        'data': [go.Pie(
                            labels=dest_port_df['Destination Port'],
                            values=dest_port_df['Count'],
                        )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                ),
                dbc.Table.from_dataframe(dest_port_df, striped=True, bordered=True, hover=True)
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("Top 10 Events"),
                dbc.Table.from_dataframe(event_df, striped=True, bordered=True, hover=True)
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("Top 10 Classifications"),
                dbc.Table.from_dataframe(classification_df, striped=True, bordered=True, hover=True)
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H2("Event Table"),
                dbc.Table.from_dataframe(plopper_df.head(), striped=True, bordered=True, hover=True),
                html.H2("Event Table"),
                dt.DataTable(
                    id="Plopper Data",
                    columns=[{"name": i, "id": i} for i in plopper_df.columns],
                    n_fixed_rows=1,
                    style_cell={'width': '100%'},
                    data=plopper_df.to_dict("rows"),
                )
            ], width=12)
        ]),
    ])

    # Web App build
    app.layout = html.Div([navbar, body])

    app.run_server(debug=True)
