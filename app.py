from dotenv import load_dotenv

load_dotenv() ## carrega variaveis secretas
from flask import Flask, render_template
from routes.auth import auth_bp, login_required
from routes.credentials import cred_bp
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#define a rota homepage
@app.route('/')
def root():
    return render_template('homepage.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


#define a blueprint auth, que contém auth/login e auth/register
app.register_blueprint(auth_bp, url_prefix='/auth')

app.register_blueprint(cred_bp, url_prefix='/cred')
if __name__ == "__main__":
    app.run(debug=True)



#fazer aparecer as credenciais na dashboard