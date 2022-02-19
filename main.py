from flask import Flask, render_template, Markup, redirect, current_app
from flask_socketio import SocketIO, emit
from utils import getTable, bels
from objects import Links, Otdel


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, engineio_logger=False, cors_allowed_origins='*')
# app = Flask(__name__)
links = Links()
otdels = Otdel()


@app.route('/')
def index():
    return render_template('index.html',
        otdel=otdels.li[otdels.otdel],
        dates=links.li[otdels.otdel]
        )

def thr(app):
    with app.app_context():
        if links.li[0][0][1] == "Загрузка...":
            # socketio.sleep(60)
            try:
                links.getAll()
                socketio.emit('show-msg', [1,2])
            except:
                socketio.emit('netErr', [1,2])
                print("AAAAAAA"*100)

@socketio.on('request-all-msgs')
def handle_sync():

    socketio.start_background_task(thr, current_app._get_current_object())

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

@app.errorhandler(Exception)
def handle_bad_request(e):
    return render_template('Error.html')

if __name__ == '__main__':
    # app.run(host='localhost', port=8080, debug=False)
    socketio.run(app, debug=True, host='0.0.0.0')
