# 📊 Dashboard de Mortalidad en Colombia

**Autor:** Mario Esteban Vargas Pisco  
**Proyecto:** Visualización de datos de mortalidad (Aplicaciones I - Maestría en Inteligencia Artificial)  
**Fecha:** Mayo 18, 2025  
**Universidad:** Universidad de La Salle

---

## 🧩 Descripción

Este dashboard interactivo presenta visualizaciones detalladas sobre la mortalidad en Colombia, permitiendo el análisis geográfico, demográfico y por causas de muerte. Está construido con `Dash`, `Plotly`, y `SQLite`, y desplegado mediante **Render.com**.

---

## 📁 Estructura del Proyecto

```
mortality_dashboard/
│
├── app.py                  # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias necesarias para Render
├── Procfile                # Configuración para despliegue
│
├── assets/                 # Estilos personalizados e imágenes
│   ├── custom.css
│   └── logo_ministerio.png
│
├── data/                   # Datos fuente (GeoJSON, SQLite, Excel)
│   ├── mortality_dw.db
│   ├── colombia.geo.json
│   ├── Divipola_CE_.xlsx
│   └── CodigosDeMuerte.xlsx
│
├── scripts/                # ETLs y construcción del DW
│   └── mortality_dw_creation.py
│
└── src/                    # Componentes funcionales
    ├── layout.py           # Diseño del dashboard y visualizaciones
    └── utils.py            # Funciones auxiliares (limpieza, conexión, etc.)
```

---

## 📌 Visualizaciones Incluidas

- 🗺️ Mapa coroplético de muertes por departamento
- 📈 Línea temporal de muertes por mes
- 📊 Barras con los 5 municipios con más homicidios
- 🥧 Gráfico circular: 10 ciudades con menor mortalidad
- 🧾 Tabla: principales causas de muerte
- 📉 Histograma de muertes por edad
- 🚻 Gráfico de barras apiladas por sexo y departamento

---

## ⚙️ Tecnologías Usadas

- Python 3.11+
- Dash
- Plotly
- Pandas
- SQLite
- GeoJSON
- Gunicorn (para despliegue)

---

## 🚀 Despliegue en Render

Para desplegar el proyecto en [Render.com](https://render.com):

1. Se aseguro de que `requirements.txt` y `Procfile` están en la raíz del repositorio.
2. El `Procfile` debe contener:
   ```
   web: python app.py
   ```
3. El comando de construcción (`Build Command`) en Render:
   ```
   pip install -r requirements.txt
   ```
---

## 🧠 Conclusión

Este proyecto integra múltiples habilidades en desarrollo de dashboards, bases de datos y despliegue web. Facilita la exploración de patrones de mortalidad de forma visual y accesible para la toma de decisiones.

---

---
## 🖼️ Evidencia del Dashboard en Dash y Render

| 🖥️ Evidencia del Dashboard en Dash y Render                | 🌐 Dashboard desplegado en Render                 | 
|----------------------------------------|---------------------------------------|---------------------------------------|
| ![Dash 1 ](screenshots/Evidencia%20Dash.PNG) | ![Dash 2 ](screenshots/Evidencia%Dash%2.PNG) | ![Render 1](screenshots/Evidencia$del%Dashboard%en%Render.PNG) |[Render 2](screenshots/Evidencia$del$Dashboard%en%Render%2.PNG) |
---

## 📬 Contacto

**Correo:** mevargasp@unisalle.edu.co  
**GitHub:** [@marioevargasp95](https://github.com/marioevargasp95)
