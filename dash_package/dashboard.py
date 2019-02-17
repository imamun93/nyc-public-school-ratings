from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash_package.query import *


import dash
import plotly.graph_objs as go
import plotly.plotly as py
import pandas as pd

from dash_package.mega_data import mega_list_2012, mega_list_2013, mega_list_2014, mega_list_2015, mega_list_2016, mega_list_2017


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('Schools2013.csv', sep='\t')


app.layout = html.Div(children=[
html.H1('NYC Public School Attendance, Rating and Student Performance'),
dcc.Tabs(id="tabs", children=[
	dcc.Tab(id='satmath', label='Math AVG SAT',
		children=[
    dcc.Graph(
        id='math-sat-avg',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Rating'] == i]['Math_Avg'],
                    y=df[df['Rating'] == i]['Attendance_Ratio'],
                    text=df[df['Rating'] == i]['Name'],
                    mode='markers',
                    # showlegend= False,
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'black'}
                    },
                    name=str(i)
                ) for i in df.Rating.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Math Average'},
                yaxis={'title': 'Absence Ratio'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
]),
    dcc.Tab(id='satread', label='Reading AVG SAT',
		children=[
        dcc.Graph(
            id='read-sat-avg',
            figure={
                'data': [
                    go.Scatter(
                        x=df[df['Rating'] == i]['Reading_Avg'],
                        y=df[df['Rating'] == i]['Attendance_Ratio'],
                        text=df[df['Rating'] == i]['Name'],
                        mode='markers',
                        # showlegend= False,
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=str(i)
                    ) for i in df.Rating.unique()
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Reading Average'},
                    yaxis={'title': 'Absence_Ratio'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])
])])
