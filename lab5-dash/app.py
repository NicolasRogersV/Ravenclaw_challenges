import dash_bootstrap_components as dbc
import utils as ut
import os
import pandas as pd
import plotly.graph_objs as go
from dash import dash, dcc, html, Output, Input
from plotly.subplots import make_subplots

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons .
                                                BOOTSTRAP, "/ assets / custom .css "])

SIDEBAR_STYLE = {
    " position ": " fixed ",
    "top": 0,
    " left ": 0,
    " bottom ": 50,
    " width ": "17 rem",
    " padding ": "2rem 1rem",
    " background - color ": "# FFFFFF ",
    " color ": " #24245 c"
}

SIDEBAR_FILTER_STYLE = {

    " position ": " fixed ",
    "top": 200,
    " left ": 0,
    " bottom ": 50,
    " width ": "17 rem",
    " padding ": "2rem 1rem",
    " background - color ": "# FFFFFF ",
    " color ": " #24245 c"
}

CONTENT_STYLE = {
    "margin - left ": "19 rem",
    "margin - right ": "2rem",
    " padding ": "2rem 1rem",
    " color ": " #24245 c"
}

image_path = "assets/lorenz_attractor_rainbow.png "

df_mds = pd.read_csv("./exercise_to_bq.csv")
df_mds = ut.raw_processor(df_mds)
df_mds.rename(columns={"Training Start_date ": " Training_Start_date ",
                       "Offers Accepted ": " Offers_Accepted "}, inplace=True)

req_count_card = dbc.Card(
    dbc.CardBody([
        html.I(id="requisition -count - card ",
                 className="bi text - success h1"),
        html.H5([html.I(className="bi bi - person me -2"), " Number of requisitions "],
                className="text - nowrap "),
        html.P(" Total ", className="text - muted ",
               style={"font - size ": "10 px"}),
    ], className="border - start border - success border -5"
    ), className="text - center m -4"
)
req_avg_size_card = dbc.Card(
    dbc.CardBody([
        html.I(id="avg - requisition -size - card ",
                 className="bi text - success h1"),
        html.H5([html.I(className="bi bi - rulers me -3"), "Requisition average size "],
                className="text - nowrap "),
        html.P(" Openings per requisition ",
               className="text - muted ", style={"font - size ": "10 px"}),
    ], className="border - start border - success border -5"
    ), className="text - center m -4"
)

top_language = dbc.Card(
    dbc.CardBody([
        html.I(id="requisition - language - card ",
                 className="bi text - success h1"),
        html.H5([html.I(className="bi bi -chat -dots - fill me -2"),
                 html.I(id="requisition - language -name - card ")],
                className="text - nowrap "),
        html.P("By number of openings ", className="text - muted ",
               style={"font - size ": "10 px"}),
    ], className="border - start border - success border -5"
    ), className="text - center m -4"
)

top_vertical = dbc.Card(
    dbc.CardBody([
        html.I(id="requisition - vertical - card ",
                 className="bi text - success h1"),
        html.H5([html.I(className="bi bi - building -up me -2"),
                 html.I(id="requisition - vertical -name - card ")],
                className="text - nowrap "),
        html.P("By number of openings ", className="text - muted ",
               style={"font - size ": "10 px"}),
    ], className="border - start border - success border -5"
    ), className="text - center m -4"
)

top_country = dbc.Card(
    dbc.CardBody([
        html.I(id="requisition - country - card ",
                 className="bi text - success h1"),
        html.H5([html.I(className="bi bi - globe me -2"),
                 html.I(id="requisition - country -name - card ")],
                className="text - nowrap "),
        html.P("By number of openings ", className="text - muted ",
               style={"font - size ": "10 px"}),
    ], className="border - start border - success border -5"

    ), className="text - center m -4"
)

filters_side_bar = html.Div([
    html.Div(

        children=[
            html.Img(src=image_path, alt="Logo Dynamical Systems ",
                     className="header - image ", style=SIDEBAR_STYLE),
            html.Div([
                html.H4("Filters ", style={
                        " color ": " #24245 c", "padding -top ": "40 px "}),
                html.Div([
                    html.Label("Start Date ", style={"marginRight ": "5px "}),
                    dcc.DatePickerSingle(
                        id="start -date - picker ",
                        date=df_mds[" Training_Start_date "]. min(),
                        display_format="MMM Do, YY ",
                        with_portal=True,
                        style={"marginRight ": "10 px "}
                    ),
                    html.Label("End date ", style={"marginRight ": "12 px "}),
                    dcc.DatePickerSingle(
                        id="end -date - picker ",
                        date=df_mds[" Training_Start_date "]. max(),
                        display_format="MMM Do, YY ",
                        with_portal=True
                    ),
                ], style={"display ": "block ", "alignItems ": "center ", " marginBottom ": "10 px "}),
                dcc.Dropdown(
                    id="country - dropdown ",
                    options=[{"label ": country, "value ": country} for country in df_mds["Country "].
                             unique()],
                    multi=True,
                    value=None,
                    style={" marginBottom ": "10 px "},
                    placeholder="Country "
                ),
                dcc.Dropdown(
                    id="vertical - dropdown ",
                    options=[{"label ": vertical, "value ": vertical}
                             for vertical in df_mds["Vertical"].unique()],
                    multi=True,
                    value=None,
                    style={" marginBottom ": "10 px "},
                    placeholder="Vertical "
                ),
                dcc.Dropdown(
                    id="language - dropdown ",
                    options=[{"label ": language, "value ": language} for language in df_mds["Language"].
                             unique()],
                    multi=True,
                    value=None,
                    style={" marginBottom ": "10 px "},
                    placeholder="Language "
                ),
                dcc.Dropdown(
                    id="status - dropdown ",
                    options=[{"label ": pos_status, "value ": pos_status}
                             for pos_status in df_mds["tus "]. unique()],
                    multi=True,
                    value=None,
                    style={" marginBottom ": "10 px "},
                    placeholder="Status "
                )])],

    )], className="filters ", style=SIDEBAR_FILTER_STYLE),
