from flask import Flask, render_template

from controllers.client_controller import clients_blueprint
from controllers.classes_controller import classes_blueprint

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
    
app.register_blueprint(clients_blueprint)
app.register_blueprint(classes_blueprint)


if __name__ == '__main__':
    app.run()