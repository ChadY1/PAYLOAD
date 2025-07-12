from flask import Flask, render_template, request, redirect, session, url_for, send_file
from cryptography.fernet import Fernet
import pandas as pd
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Changez ceci en production

FERNET_KEY = b'SJ0pY0f3Tiqq5pNXQZsiwS6c1CWrxRocORau8IOj9Ic='
LOG_PATH = 'log.csv'

USERS = {
    'admin': 'admin123'
}

# Initialise le fichier de log si nécessaire
if not os.path.exists(LOG_PATH):
    pd.DataFrame(columns=['uid', 'timestamp', 'scan_time', 'ip', 'terminal']).to_csv(LOG_PATH, index=False)

def decrypt_token(token):
    f = Fernet(FERNET_KEY)
    data = json.loads(f.decrypt(token.encode()).decode())
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        token = request.form['token'].strip()
        terminal = request.user_agent.string
        ip = request.remote_addr
        try:
            data = decrypt_token(token)
            now = datetime.utcnow().replace(microsecond=0).isoformat()
            new_entry = {
                "uid": data.get("uid"),
                "timestamp": data.get("timestamp"),
                "scan_time": now,
                "ip": ip,
                "terminal": terminal
            }
            df = pd.read_csv(LOG_PATH)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            df.to_csv(LOG_PATH, index=False)
            return redirect('/dashboard')
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html", error=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if USERS.get(username) == password:
            session['user'] = username
            return redirect('/dashboard')
        return render_template("login.html", error="Identifiants incorrects.")
    return render_template("login.html", error=None)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    df = pd.read_csv(LOG_PATH)
    df = df.sort_values(by='scan_time', ascending=False)
    return render_template("dashboard.html", table=df.to_dict(orient='records'))

@app.route('/export')
def export():
    if 'user' not in session:
        return redirect(url_for('login'))
    return send_file(LOG_PATH, as_attachment=True)

if __name__ == "__main__":
    print("🚀 Application Flask démarrée sur http://localhost:5000")
    app.run(debug=True)
