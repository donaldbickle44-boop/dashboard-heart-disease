from dash import html
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        html.H1(
            "Dashboard Interativo de Machine Learning",
            className="text-center mt-5"
        ),

        html.H3(
            "Previsão de Doença Cardíaca",
            className="text-center mt-3"
        ),

        html.Hr(),

        html.P(
            "Este dashboard apresenta uma análise dos dados "
            "de doenças cardíacas e utiliza Machine Learning "
            "para realizar previsões."
        ),

        html.P(
            "Utilize o menu superior para visualizar os gráficos "
            "ou realizar uma previsão."
        ),
    ],
    fluid=True
)