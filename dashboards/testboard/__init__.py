"""
__init__.py

Author: Jose Guzman
Created: Mon Aug 15 21:38:23 EDT 2022

Strongly based on this video:
https://www.youtube.com/watch?v=7m0Bq1EGPPg
"""
from flask import Flask

from dash import Dash, html, dcc
from dash import Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

# custom layouts

def test_layout(flask_app:Flask) -> Dash:
    """
    Layout to test Dash
    """
    # main Dash application
    mydashboard = Dash(server = flask_app,
        name = 'TestBoard',
        url_base_pathname = '/testboard/',
        external_stylesheets=[dbc.themes.SOLAR]
        )

    # define components  
    mytext = dcc.Markdown(children='# Hello World in TestBoard')
    myinput = dbc.Input(value='Insert your message here')

    # callback decorator and callback function
    @mydashboard.callback(
        Output(mytext, component_property='children'),
        Input(myinput, component_property='value')
    )

    def update_title(mytext):
        """
        Function argument comes from component_property of input
        """
        # returns componenent_property of the output:w
        return mytext

    # finish layout
    mydashboard.title = "testboard"
    mydashboard.layout = dbc.Container([mytext, myinput])

    return mydashboard

def create_dashboard(flask_app:Flask) -> Dash:
    """
    Creates a dashboard inside a Flask application
    """

    # dash applicaton
    mydash = Dash( server = flask_app, 
        name = 'configurator', 
        url_base_pathname = '/testboard/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
        )

    mydash.title = "Configurator"

    # dash layout
    #mydash.layout = layout.basic(dashboard = mydash) 
    #mydash.layout = layout.test_layout(dashboard = mydash) 
    mydash.layout = html.Div(children=[
        html.H1(children='Customize page'),

        html.Div(children='''
            Dash: A web application framework for your data.
        ''')
        ])

    return mydash 
