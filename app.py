# app.py
from flask import Flask

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define una ruta (URL)
@app.route('/')
def hello_world():
    # Retorna un mensaje simple
    return "¡Hola! Esta es la app de DevOps de finalquintoa."

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000
    app.run(debug=True, host='0.0.0.0', port=5000)