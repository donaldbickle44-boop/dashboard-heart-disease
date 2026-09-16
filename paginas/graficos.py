from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import dcc, html
import dash_bootstrap_components as dbc


# Carrega o dataset UCI Heart Disease
heart_disease = fetch_ucirepo(id=45)

dados = heart_disease.data.features.copy()

# Cria a variável de diagnóstico
dados["doenca"] = (
    heart_disease.data.targets.iloc[:, 0] > 0
).astype(int)


# Histograma da distribuição de idade
fig_hist = px.histogram(
    dados,
    x="age",
    nbins=30,
    title="Distribuição Etária",
    color="doenca"
)

fig_hist.update_layout(
    xaxis_title="Idade",
    yaxis_title="Frequência",
    legend_title="Diagnóstico"
)


# Boxplot da idade por diagnóstico
fig_box = px.box(
    dados,
    x="doenca",
    y="age",
    title="Distribuição Etária por Doença",
    color="doenca"
)

fig_box.update_layout(
    xaxis_title="Diagnóstico (0 = não | 1 = sim)",
    yaxis_title="Idade",
    legend_title="Diagnóstico"
)


layout = dbc.Container(
    [
        html.H1(
            "Análise dos Dados",
            className="text-center mt-4"
        ),

        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=fig_hist),
                    md=6
                ),

                dbc.Col(
                    dcc.Graph(figure=fig_box),
                    md=6
                ),
            ]
        )
    ],
    fluid=True
)