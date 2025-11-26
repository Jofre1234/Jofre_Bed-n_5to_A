from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    
    return "¡Hola! Esta es la app de DevOps de finalquintoa."


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
