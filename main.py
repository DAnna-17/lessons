from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('\\templates\\base.html', title='Миссия на Марс')

if __name__ == '__main__':
    app.run(port=8080, host='localhost')