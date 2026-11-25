# StudyBot — Evaluador Web de Espacios de Estudio

Aplicación web desarrollada con **Flask** que utiliza un modelo de clasificación entrenado (`GradientBoostingClassifier`) para predecir si un espacio dentro del campus universitario es **APTO** o **NO APTO** para estudiar, a partir de 11 características binarias (`0` o `1`).

## Estructura del proyecto

```text
studybot-web/
├── app.py                  # Servidor Flask y lógica de inferencia
├── studybot_model.joblib   # Modelo/Pipeline entrenado y serializado
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Instrucciones de instalación y ejecución
└── templates/
    └── index.html          # Formulario web para captura de variables