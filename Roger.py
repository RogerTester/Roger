from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run()
