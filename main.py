from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from paginas import home, graficos, formulario


navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Gráficos",
                href="/graficos"
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Formulário",
                href="/formulario"
            )
        ),
    ],
    brand="Dashboard - Heart Disease",
    brand_href="/",
    color="primary",
    dark=True
)


app.layout = html.Div(
    [
        dcc.Location(
            id="url",
            refresh=False
        ),

        navegacao,

        html.Div(
            id="conteudo",
            className="container-fluid"
        )
    ]
)


@app.callback(
    Output("conteudo", "children"),
    Input("url", "pathname")
)
def mostrar_pagina(pathname):

    if pathname == "/graficos":
        return graficos.layout

    elif pathname == "/formulario":
        return formulario.layout

    else:
        return home.layout


if __name__ == "__main__":
    app.run(
        debug=True
    )