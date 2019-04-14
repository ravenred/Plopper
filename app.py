import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt


def app_deploy(plopper_df):

    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H2('My Dash App'),
        dt.DataTable(
            id='Plopper Data',
            rows=plopper_df,
            editable=False,
            row_selectable=True,
            filterable=True,
            sortable=True,
            selected_row_indices=[]
        ),
        html.Div(id='selected-indexes'),
        dcc.Graph(
            id='datatable-subplots'
        )
    ], style={'width': '60%'})

    app.run_server(debug=True)
