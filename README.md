<<<<<<< HEAD
# Proyectos_GitHub
Varios_proyectos
=======
# 🔐 <<<<<<< HEAD
# Proyectos_GitHub
Varios_proyectos
=======
# Dashboard de Mortalidad en Colombia

**Nombre del estudiante:** Mario Esteban Vargas Pisco  
**Asignatura:** Aplicaciones I - Maestría en Inteligencia Artificial - Profundización
**Fecha:** Mayo 10, 2025
**Universidad**  La Salle

---

## 📘 Introducción

Este dashboard interactivo presenta visualizaciones detalladas sobre la mortalidad en Colombia, permitiendo el análisis geográfico, demográfico y por causas de muerte. Está construido con `Dash`, `Plotly`, y `SQLite`, y desplegado mediante **Render.com**.

---

## 📁 Estructura del Proyecto

mortality_dashboard/
│
├── app.py # Punto de entrada de la aplicación
├── requirements.txt # Dependencias necesarias para Render
├── Procfile # Configuración para despliegue
│
├── assets/ # Estilos personalizados e imágenes
│ ├── custom.css
│ └── logo_ministerio.png
│
├── data/ # Datos fuente (GeoJSON, SQLite, Excel)
│ ├── mortality_dw.db
│ ├── colombia.geo.json
│ ├── Divipola_CE_.xlsx
│ └── CodigosDeMuerte.xlsx
│
├── scripts/ # ETLs y construcción del DW
│ └── mortality_dw_creation.py
│
└── src/ # Componentes funcionales
├── layout.py # Diseño del dashboard y visualizaciones
└── utils.py # Funciones auxiliares (limpieza, conexión, etc.)

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

1. Asegúrate de que `requirements.txt` y `Procfile` están en la raíz del repositorio.
2. El `Procfile` debe contener:


## 🧠 Conclusión

A través de esta actividad se logró comprender la estructura básica de una interfaz gráfica usando Python y Tkinter. Se aplicaron principios de lógica y diseño modular, además de integrarse con herramientas como PyInstaller y GitHub. Este proyecto fortaleció la autonomía técnica en el desarrollo de soluciones sencillas, prácticas y presentables.
>>>>>>> 1a1a94dcccef31045840ce66187a27426641ac2b


**Nombre del estudiante:** Mario Esteban Vargas Pisco  
**Asignatura:** Aplicaciones I - Maestría en Inteligencia Artificial - Profundización
**Fecha:** Mayo 18, 2025
**Universidad**  La Salle

---

## 📘 Introducción

Esta aplicación fue desarrollada como parte del curso de Aplicaciones I con el propósito de implementar una interfaz gráfica en Python que permita al usuario cifrar y descifrar números de seis dígitos aplicando una lógica algorítmica.  
El objetivo principal es familiarizarse con el desarrollo de interfaces usando `Tkinter` u otras, aplicar lógica de programación y generar un entregable funcional empaquetado como ejecutable.

---

## ⚙️ Desarrollo

El programa consta de una ventana principal desde la cual el usuario puede:
- **Cifrar un número**: se abre una ventana para ingresar un número de 6 dígitos y aplicar el algoritmo de cifrado.
- **Descifrar un número**: se abre una ventana para revertir el cifrado y obtener el número original.
- **Nota**: se generó una función para limitar el número de dígitos a 6 y solo sean números enteros.

### Algoritmo de cifrado:
1. Se suma 7 a cada dígito y se aplica módulo 10.
2. Se intercambian las posiciones:
   - 1º ↔ 3º
   - 2º ↔ 4º
   - 5º ↔ 6º

### Ventanas de la aplicación:

| Ventana principal                      | Ventana de cifrado                    | Ventana de descifrado                 |
|----------------------------------------|---------------------------------------|---------------------------------------|
| ![Main](screenshots/main.PNG) | ![Cifrado](screenshots/cifrado.PNG) | ![Descifrado](screenshots/descifrado.PNG) |

---

## 🧪 Pruebas de funcionalidad

| Entrada original | Número cifrado | Descifrado (resultado) |
|------------------|----------------|-------------------------|
| 123456           | 098723         | 123456                  |
| 987654           | 432109         | 987654                  |
| 222222           | 999999         | 222222                  |

---

## 🧠 Conclusión

A través de esta actividad se logró comprender la estructura básica de una interfaz gráfica usando Python y Tkinter. Se aplicaron principios de lógica y diseño modular, además de integrarse con herramientas como PyInstaller y GitHub. Este proyecto fortaleció la autonomía técnica en el desarrollo de soluciones sencillas, prácticas y presentables.
>>>>>>> 1a1a94dcccef31045840ce66187a27426641ac2b
