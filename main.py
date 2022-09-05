from flask import Flask, render_template, Markup, redirect, current_app
from utils import getTable, bels
from objects import Links, Otdel


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
links = Links()
otdels = Otdel()


@app.route('/')
def index():
    links.getAll()
    return render_template('index.html',
        otdel=otdels.li[otdels.otdel],
        dates=links.li[otdels.otdel]
    )

@app.route('/refresh')
def refresh():
    links.getAll()
    return redirect("/")

@app.route('/table/<string:foo>')
def tableStr(foo):
    return redirect("/")

@app.route('/table/<int:id>')
def tableId(id):
    return render_template('tableId.html',
        title=links.li[otdels.otdel][id][1],
        table=Markup(getTable(links.li[otdels.otdel][id][2]))
    )

@app.route('/otdel/<int:id>')
def func_name(id):
    if id == 2:
        return render_template('index.html',
            otdel="Расписание звонков",
            dates=bels
        )
    otdels.set(id)
    return redirect("/")

# @app.errorhandler(Exception)
# def handle_bad_request(e):
#     return render_template('Error.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
