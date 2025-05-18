# 📊 Dashboard de Mortalidad en Colombia

**Autor:** Mario Esteban Vargas Pisco  
**Proyecto:** Visualización de datos de mortalidad (Aplicaciones I - Maestría en Inteligencia Artificial)  
**Fecha:** Mayo 18, 2025  
**Universidad:** Universidad de La Salle

---

## 🧩 Descripción

Este proyecto tiene como propósito desarrollar una aplicación web interactiva para visualizar patrones de mortalidad en Colombia, haciendo uso de Python, Dash y un modelo de Data Warehouse. La solución combina herramientas de desarrollo web con principios de ingeniería de datos para facilitar la toma de decisiones en salud pública.

El uso de Dash y Plotly permite la creación de dashboards con componentes visuales ricos e interactivos, sin necesidad de programación web avanzada. Por otro lado, el modelado Data Warehouse garantiza una estructura de datos optimizada, confiable y preparada para análisis multidimensional.

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

---
## 📦 Data Warehouse
Se construyó un modelo de Data Warehouse para la mortalidad en Colombia con las siguientes características: 

- Hechos: hechos_mortalidad (fecha, edad, sexo, causa de muerte, código DANE)

Dimensiones:

- dim_ubicacion: datos geográficos normalizados (departamento, municipio)

- dim_tiempo (si aplica): año, mes

- dim_causa: código CIE10 y descripción

El modelo garantiza consistencia, velocidad de consulta y facilidad para construir indicadores agregados por múltiples niveles.
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

Pasos realizados:

Estructura modular del código

requirements.txt y Procfile para despliegue

app.run() actualizado para compatibilidad

Publicación en https://mortality-dashboard.onrender.com

🔐 Se validó que el enlace esté activo, accesible públicamente y cargue todos los recursos necesarios (GeoJSON, DB).

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

El proyecto permitió integrar y aplicar conocimientos clave en Python, Dash y análisis de datos. La experiencia de construir un dashboard desde cero, organizarlo de forma modular, conectarlo con bases SQLite apoyandose  y publicarlo en la web demuestra la versatilidad de estas herramientas.

Dash y Plotly ofrecieron una alternativa ágil para crear visualizaciones potentes, mientras que Render facilitó un despliegue accesible.
Se identificaron oportunidades de mejora como:

Incluir filtros por año o región.

Permitir exportar los gráficos como PDF.

Habilitar autenticación de usuarios para diferentes roles.

---

---
## 🖼️ Evidencia del Dashboard en Dash y Render

| 🖥️ Evidencia en Dash | 🌐 Render (Vista 1) | 🌐 Render (Vista 2) |
|----------------------|--------------------|---------------------|
| ![Dash 1](assets/Evidencia%20Dash.png) | ![Render 1](assets/Evidencia%20del%20Dashboard%20en%20Render.png) | ![Render 2](assets/Evidencia%20del%20Dashboard%20en%20Render%202.png) |

---

## 📬 Contacto

**Correo:** mevargasp@unisalle.edu.co  
**GitHub:** [@marioevargasp95](https://github.com/marioevargasp95)

---
