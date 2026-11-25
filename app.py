from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Cargamos el modelo una sola vez al iniciar la aplicación
modelo = joblib.load('studybot_model.joblib')

# Lista exacta y ordenada de columnas que espera el modelo
COLUMNAS = [
    'silencio', 'sombra', 'aire_acondicionado', 'soporte_para_trabajar',
    'asientos', 'asientos_comodos', 'enchufes', 'flujo_personas',
    'banos_cerca', 'cafeteria_cerca', 'internet_wifi'
]

def predecir_lugar(datos_entrada: dict) -> str:
    """
    Recibe un diccionario con las 11 características (valores 0 o 1),
    arma un DataFrame con el orden exacto de columnas y devuelve 'APTO' o 'NO APTO'.
    """
    df_entrada = pd.DataFrame([datos_entrada], columns=COLUMNAS)
    prediccion = modelo.predict(df_entrada)[0]
    return "APTO" if prediccion == 1 else "NO APTO"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None
    valores_form = {}

    if request.method == 'POST':
        try:
            datos_usuario = {}
            for col in COLUMNAS:
                valor_raw = request.form.get(col)
                if valor_raw is None or valor_raw.strip() == '':
                    raise ValueError(f"El campo '{col}' es obligatorio.")
                
                # Validación estricta de valor numérico (0 o 1)
                valor_num = float(valor_raw)
                if valor_num not in (0.0, 1.0):
                    raise ValueError(f"El campo '{col}' debe ser 0 o 1.")
                
                datos_usuario[col] = int(valor_num)
                valores_form[col] = int(valor_num)

            resultado = predecir_lugar(datos_usuario)

        except ValueError as e:
            error = f"Entrada inválida: {e}"

    return render_template('index.html', resultado=resultado, error=error, valores=valores_form)

# Bloque para probar la función aislada (Paso 2 de la guía) al ejecutar directamente si se desea
if __name__ == '__main__':
    app.run(debug=True)