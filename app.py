from flask import Flask, render_template
from routes.auth import auth_bp
from routes.credentials import cred_bp


app = Flask("__main__")



#define a rota homepage
@app.route('/')
def root():
    return render_template('homepage.html')

#define a blueprint auth, que contém auth/login e auth/register
app.register_blueprint(auth_bp, url_prefix='/auth')

app.register_blueprint(cred_bp, url_prefix='/credentials')
if __name__ == "__main__":
    app.run(debug=True)