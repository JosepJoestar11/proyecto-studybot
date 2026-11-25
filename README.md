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
    └── index.html          # Formulario web para captura de variables```

## Requisitos previos

* Python 3.10 o superior (Anaconda / Miniconda o instalación estándar de Python)
* `git` y `pip`

## Instalación y ejecución local

1. **Clonar el repositorio y entrar a la carpeta del proyecto:**
   ```bash
   git clone [https://github.com/JosepJoestar11/proyecto-studybot.git](https://github.com/JosepJoestar11/proyecto-studybot.git)
   cd proyecto-studybot
   ```

2. **Crear y activar un entorno virtual:**
   * **Con Anaconda / Conda:**
     ```bash
     conda create -n studybot-env python=3.11 -y
     conda activate studybot-env
     ```
   * **Alternativa con Python estándar (`venv`):**
     ```bash
     python -m venv venv
     # En Windows:
     venv\Scripts\activate
     # En Linux / macOS:
     source venv/bin/activate
     ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar la aplicación:**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador:**
   Ingresa a `http://127.0.0.1:5000`, captura los valores (`1` para presente/sí, `0` para ausente/no) en cada característica y presiona **Evaluar lugar**.