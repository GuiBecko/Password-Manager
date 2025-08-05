from flask import Blueprint, render_template, redirect, url_for, flash, session
from db import Usuario
from db import session as db_session
from security import criptografarsenha, verificarsenha
from forms import RegistrationForm, LoginForm
from functools import wraps

auth_bp = Blueprint('auth', __name__, template_folder = 'templates')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Por favor, faça o login para acessar a a pagina.", 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/')
@login_required
def usuario():
    return render_template('Paginadeusuario.html')









@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() 

    # validate_on_submit() checa se é um POST e se os dados são válidos
    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        usuario_existente = db_session.query(Usuario).filter_by(email=email).first()
        if usuario_existente:
            flash('Este email já está registrado. Por favor, faça login.', 'info')
            return redirect(url_for('auth.login'))
        
        # Dados são válidos e usuário não existe, então crie
        usuario = Usuario()
        usuario.email = email
        usuario.senhacript = criptografarsenha(senha)
        db_session.add(usuario)
        db_session.commit()

        flash('Registro realizado com sucesso! Faça o login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('Paginaderegistro.html', form=form)



@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm() 

    if form.validate_on_submit():
        email = form.email.data
        senha_digitada = form.senha.data

        usuario_existente = db_session.query(Usuario).filter_by(email=email).first()

        if usuario_existente and verificarsenha(usuario_existente.senhacript, senha_digitada):
            #adiciona o usuario logado na sessao
            session['user_id'] = usuario_existente.id
            session['user_email'] = usuario_existente.email

            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('auth.usuario'))
        else:
            flash('Email ou senha incorretos. Por favor, tente novamente.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('Paginadelogin.html', form=form)
        

