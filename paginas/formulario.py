import joblib
import pandas as pd

from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app


# Carrega o modelo e as medianas
modelo = joblib.load("modelo_xgboost.pkl")
medianas = joblib.load("medianas.pkl")


layout = dbc.Container(
    [
        html.H1(
            "Previsão de Doença Cardíaca",
            className="text-center mt-4"
        ),

        html.P(
            "Informe os dados do paciente para realizar a previsão.",
            className="text-center"
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Idade"),
                        dbc.Input(
                            id="age",
                            type="number",
                            placeholder="Ex.: 55"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Sexo"),
                        dcc.Dropdown(
                            id="sex",
                            options=[
                                {"label": "Masculino", "value": 1},
                                {"label": "Feminino", "value": 0},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Tipo de dor no peito (cp)"),
                        dcc.Dropdown(
                            id="cp",
                            options=[
                                {"label": "1", "value": 1},
                                {"label": "2", "value": 2},
                                {"label": "3", "value": 3},
                                {"label": "4", "value": 4},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),
            ],
            className="mb-3"
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Pressão arterial em repouso"),
                        dbc.Input(
                            id="trestbps",
                            type="number",
                            placeholder="Ex.: 130"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Colesterol"),
                        dbc.Input(
                            id="chol",
                            type="number",
                            placeholder="Ex.: 250"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Açúcar em jejum (fbs)"),
                        dcc.Dropdown(
                            id="fbs",
                            options=[
                                {"label": "0", "value": 0},
                                {"label": "1", "value": 1},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),
            ],
            className="mb-3"
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Eletrocardiograma (restecg)"),
                        dcc.Dropdown(
                            id="restecg",
                            options=[
                                {"label": "0", "value": 0},
                                {"label": "1", "value": 1},
                                {"label": "2", "value": 2},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Frequência cardíaca máxima"),
                        dbc.Input(
                            id="thalach",
                            type="number",
                            placeholder="Ex.: 150"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Angina induzida por exercício (exang)"),
                        dcc.Dropdown(
                            id="exang",
                            options=[
                                {"label": "0", "value": 0},
                                {"label": "1", "value": 1},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),
            ],
            className="mb-3"
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Oldpeak"),
                        dbc.Input(
                            id="oldpeak",
                            type="number",
                            step=0.1,
                            placeholder="Ex.: 1.5"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("Slope"),
                        dcc.Dropdown(
                            id="slope",
                            options=[
                                {"label": "1", "value": 1},
                                {"label": "2", "value": 2},
                                {"label": "3", "value": 3},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),

                dbc.Col(
                    [
                        dbc.Label("CA"),
                        dcc.Dropdown(
                            id="ca",
                            options=[
                                {"label": "0", "value": 0},
                                {"label": "1", "value": 1},
                                {"label": "2", "value": 2},
                                {"label": "3", "value": 3},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),
            ],
            className="mb-3"
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Thal"),
                        dcc.Dropdown(
                            id="thal",
                            options=[
                                {"label": "3", "value": 3},
                                {"label": "6", "value": 6},
                                {"label": "7", "value": 7},
                            ],
                            placeholder="Selecione"
                        ),
                    ],
                    md=4
                ),
            ],
            className="mb-3"
        ),

        dbc.Button(
            "Realizar Previsão",
            id="botao-prever",
            color="primary",
            className="mt-3"
        ),

        html.Div(
            id="resultado",
            className="mt-4"
        )
    ],
    fluid=True
)


@app.callback(
    Output("resultado", "children"),
    Input("botao-prever", "n_clicks"),
    [
        Input("age", "value"),
        Input("sex", "value"),
        Input("cp", "value"),
        Input("trestbps", "value"),
        Input("chol", "value"),
        Input("fbs", "value"),
        Input("restecg", "value"),
        Input("thalach", "value"),
        Input("exang", "value"),
        Input("oldpeak", "value"),
        Input("slope", "value"),
        Input("ca", "value"),
        Input("thal", "value"),
    ],
    prevent_initial_call=True
)
def realizar_previsao(
    n_clicks,
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal
):

    dados = pd.DataFrame(
        {
            "age": [age],
            "sex": [sex],
            "cp": [cp],
            "trestbps": [trestbps],
            "chol": [chol],
            "fbs": [fbs],
            "restecg": [restecg],
            "thalach": [thalach],
            "exang": [exang],
            "oldpeak": [oldpeak],
            "slope": [slope],
            "ca": [ca],
            "thal": [thal],
        }
    )

    # Preenche valores ausentes utilizando as medianas
    dados = dados.fillna(medianas)

    # Mantém oldpeak como float
    dados["oldpeak"] = dados["oldpeak"].astype("float64")

    # Converte as demais variáveis para inteiro
    colunas_inteiras = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "slope",
        "ca",
        "thal",
    ]

    for coluna in colunas_inteiras:
        dados[coluna] = dados[coluna].astype(int)

    previsao = modelo.predict(dados)[0]

    if previsao == 1:
        return dbc.Alert(
            "Resultado: possível presença de doença cardíaca.",
            color="danger"
        )

    return dbc.Alert(
        "Resultado: ausência de doença cardíaca identificada pelo modelo.",
        color="success"
    )