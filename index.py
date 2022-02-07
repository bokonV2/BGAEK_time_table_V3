from flask import Flask, render_template, Markup, redirect
from utils import getTable

from objects import Links, Otdel


app = Flask(__name__)
links = Links()
otdels = Otdel()

@app.route('/')
def index():
    return render_template('index.html',
        otdel=otdels.li[otdels.otdel],
        dates=links.li[otdels.otdel]
        )

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/table/<int:id>')
def tableId(id):
    return render_template('tableId.html',
        title=links.li[otdels.otdel][id][1],
        table=Markup(getTable(links.li[otdels.otdel][id][2]))
        )

@app.route('/otdel/<int:id>')
def func_name(id):
    otdels.set(id)
    return redirect("/")

@app.errorhandler(Exception)
def handle_bad_request(e):
    return render_template('Error.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=False)
