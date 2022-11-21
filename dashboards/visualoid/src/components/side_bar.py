"""
This app creates a simple sidebar layout using inline style 
arguments and the dbc.Nav component.

dcc.Location is used to track the current location, and a 
callback uses the current location to render the appropriate 
page content. The active prop of each NavLink is set automatically 
according to the current pathname. 
"""

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc # for themes

# the style arguments for the sidebar. 
# We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position 
# it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
def render(dashboard: Dash, title: str) -> html.Div:
    """
    The main application side menubar
    """
    sidebar = html.Div([
        html.H2(title, className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", 
            className="lead"
        ),
        dbc.Nav([
            dbc.NavLink("Home", href="/", active="exact"),
            dbc.NavLink("Page 1", href="/page-1", active="exact"),
            dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )
    @dashboard.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname:str): 
        """
        reads pathname and loads the corresponding layout
        """
        if pathname == "/":
            return html.P("This is the content of the home page!")
        elif pathname == "/page-1":
            return html.P("This is the content of page 1. Yay!")
        elif pathname == "/page-2":
            return html.P("Oh cool, this is page 2!")
        # return a 404 message
        return layout.error_404(dashboard)

    content = html.Div(id="page-content", style=CONTENT_STYLE)
    mylayout = html.Div([dcc.Location(id="url"), sidebar, content])

    return mylayout
