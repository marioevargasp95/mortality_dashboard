import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os
import unicodedata
from dash import html, dcc

# 🔧 Función para limpiar nombres
def quitar_tildes(texto):
    if not isinstance(texto, str):
        return texto
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', errors='ignore').decode('utf-8')
    return texto.replace(".", "").replace(",", "").upper().strip()

# 📊 Conexión a la base de datos
conn = sqlite3.connect("data/mortality_dw.db")

# 1️⃣ Mapa coroplético
df_mapa = pd.read_sql_query("""
    SELECT du.DEPARTAMENTO, COUNT(hm.AÑO) AS total_muertes
    FROM hechos_mortalidad hm
    JOIN dim_ubicacion du ON hm.cod_dane = du.COD_DANE
    GROUP BY du.DEPARTAMENTO
""", conn)

df_mapa.rename(columns={"DEPARTAMENTO": "departamento"}, inplace=True)
df_mapa["departamento"] = df_mapa["departamento"].apply(quitar_tildes)
df_mapa.replace({"departamento": {
    'SAN ANDRES': 'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA',
    'BOGOTA DC': 'SANTAFE DE BOGOTA DC'}}, inplace=True)

geo_path = "data/colombia.geo.json"  # Asegúrate de que el nombre del archivo coincida exactamente
with open(geo_path, encoding='utf-8') as f:
    geojson_data = json.load(f)

for feature in geojson_data["features"]:
    nombre = feature["properties"].get("NOMBRE_DPT") or feature["properties"].get("DPTO_CNMBR")
    feature["properties"]["DPTO_CNMBR_CLEAN"] = quitar_tildes(nombre)

fig_mapa = px.choropleth(
    df_mapa,
    geojson=geojson_data,
    locations="departamento",
    color="total_muertes",
    featureidkey="properties.DPTO_CNMBR_CLEAN",
    color_continuous_scale="YlOrRd",
    range_color=(0, 40000),
    custom_data=["departamento", "total_muertes"]
)

fig_mapa.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br>Muertes: %{customdata[1]:,}<extra></extra>"
)
fig_mapa.update_layout(
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    height=700,
    width=1200,
    coloraxis_colorbar=dict(title="Muertes", tickformat=","),
    geo=dict(
        projection_type="mercator",
        center={"lat": 4.5709, "lon": -74.2973},
        lataxis_range=[-5, 15],
        lonaxis_range=[-85, -65],
        fitbounds="locations"
    )
)

# 2️⃣ Gráfico de líneas por mes
df_linea = pd.read_sql_query("""
    SELECT AÑO, MES, printf('%04d-%02d', AÑO, MES) AS MES_FORMATO, COUNT(*) AS TOTAL_MUERTES
    FROM hechos_mortalidad
    GROUP BY AÑO, MES
    ORDER BY AÑO, MES
""", conn)
fig_linea = px.line(df_linea, x="MES_FORMATO", y="TOTAL_MUERTES", markers=True)
fig_linea.update_layout(height=400, xaxis_title="Mes", yaxis_title="Total de muertes", yaxis_tickformat=",")
fig_linea.update_traces(hovertemplate="Mes: %{x}<br>Muertes: %{y:,}<extra></extra>")

# 3️⃣ Barras: 5 municipios con más homicidios
df_homicidios = pd.read_sql_query("""
    SELECT du.MUNICIPIO, COUNT(*) AS homicidios
    FROM hechos_mortalidad hm 
    JOIN dim_ubicacion du ON hm.cod_dane = du.COD_DANE
    WHERE CODIGO_CIE10_3C = 'X95'
    GROUP BY du.MUNICIPIO 
    ORDER BY homicidios DESC 
    LIMIT 5
""", conn)
fig_barras = px.bar(df_homicidios, x="MUNICIPIO", y="homicidios")
fig_barras.update_layout(xaxis_title="Municipio", yaxis_title="Homicidios", yaxis_tickformat=",")
fig_barras.update_traces(hovertemplate="Municipio: %{x}<br>Homicidios: %{y:,}<extra></extra>")

# 4️⃣ Pie chart: 10 municipios con menor mortalidad
df_pie = pd.read_sql_query("""
    SELECT du.MUNICIPIO, COUNT(*) AS total
    FROM hechos_mortalidad hm 
    JOIN dim_ubicacion du ON hm.cod_dane = du.COD_DANE
    GROUP BY du.MUNICIPIO 
    ORDER BY total ASC 
    LIMIT 10
""", conn)
fig_pie = px.pie(df_pie, values="total", names="MUNICIPIO")
fig_pie.update_traces(textinfo='label+percent+value', hovertemplate="%{label}<br>Muertes: %{value:,}<extra></extra>")

# 5️⃣ Tabla: principales causas de muerte
df_causas = pd.read_sql_query("""
    SELECT CODIGO_CIE10 AS codigo, DESCRIPCION_CIE10 AS causa_muerte, COUNT(*) AS total
    FROM hechos_mortalidad
    GROUP BY CODIGO_CIE10, DESCRIPCION_CIE10
    ORDER BY total DESC
    LIMIT 10
""", conn)
fig_tabla = go.Figure(data=[go.Table(
    header=dict(values=["Código", "Causa", "Total"], fill_color='paleturquoise', align='left'),
    cells=dict(values=[df_causas[col] for col in df_causas.columns], fill_color='lavender', align='left'))
])

# 6️⃣ Histograma de edades
df_edades = pd.read_sql_query("SELECT EDAD FROM hechos_mortalidad WHERE EDAD IS NOT NULL", conn)
df_edades["EDAD"] = pd.to_numeric(df_edades["EDAD"], errors='coerce')
fig_hist = px.histogram(df_edades, x="EDAD", nbins=18)
fig_hist.update_layout(xaxis_title="Edad", yaxis_title="Número de muertes", yaxis_tickformat=",")
fig_hist.update_traces(hovertemplate="Edad: %{x}<br>Muertes: %{y:,}<extra></extra>")

# 7️⃣ Barras apiladas por sexo
df_sexo = pd.read_sql_query("""
    SELECT du.DEPARTAMENTO, hm.SEXO, COUNT(*) AS total
    FROM hechos_mortalidad hm 
    JOIN dim_ubicacion du ON hm.cod_dane = du.COD_DANE
    GROUP BY du.DEPARTAMENTO, hm.SEXO
""", conn)
conn.close()
df_pivot = df_sexo.pivot(index="DEPARTAMENTO", columns="SEXO", values="total").fillna(0)
fig_apiladas = go.Figure()
for sexo in df_pivot.columns:
    fig_apiladas.add_bar(name=f"Sexo {sexo}", x=df_pivot.index, y=df_pivot[sexo])
fig_apiladas.update_layout(barmode='stack', xaxis_title="Departamento", yaxis_title="Total de muertes", yaxis_tickformat=",")
fig_apiladas.update_traces(hovertemplate="Departamento: %{x}<br>Muertes: %{y:,}<extra></extra>")

# 📦 Función final para layout
def create_layout():
    return html.Div([
        html.H1("📊 Dashboard Mortalidad en Colombia", style={"textAlign": "center", "marginBottom": "2rem"}),
        dcc.Graph(figure=fig_mapa),
        dcc.Graph(figure=fig_linea),
        dcc.Graph(figure=fig_barras),
        dcc.Graph(figure=fig_pie),
        dcc.Graph(figure=fig_tabla),
        dcc.Graph(figure=fig_hist),
        dcc.Graph(figure=fig_apiladas)
    ])