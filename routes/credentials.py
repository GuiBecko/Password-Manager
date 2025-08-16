
from flask import Blueprint, render_template, session, flash, redirect, url_for
from forms import NewCredentialForm
from db import Credential, session as db_session
import os
from security import generate_encryption_key, encrypt_data, decrypt_data
from routes.auth import login_required

cred_bp = Blueprint("cred", __name__, template_folder='templates')

@cred_bp.route('/new', methods=['POST', 'GET'])
@login_required
def novaSenha():
    form = NewCredentialForm()
    senha_mestra = session.get('master_key')
    user_id = session.get('user_id')

    if not user_id:
        flash("Sessão expirada. Faça login novamente.", "warning")
        return redirect(url_for('auth.login'))
    
    if form.validate_on_submit(): #se é POST
        site = form.site.data
        usuario = form.usuario.data
        senha_para_encriptar = form.senha.data

        form.site.data = ''
        form.usuario.data = ''
        form.senha.data = ''

        salt = os.urandom(16)
        encryption_key = generate_encryption_key(senha_mestra, salt)
        encrypted_password = encrypt_data(senha_para_encriptar, encryption_key)

        credencial = Credential(
            site = site,
            usuario = usuario,
            senhacript = encrypted_password,
            salt = salt,
            user_id = user_id
        )

        db_session.add(credencial)
        db_session.commit()

        flash('Credencial salva com segurança!', 'success')
        return redirect(url_for('auth.usuario'))
    return render_template('Novasenha.html', form = form)

@cred_bp.route("/dashboard")
@login_required
def dashboard():
    user_id = session.get('user_id')
    senha_mestra = session.get('master_key')

    if not user_id or not senha_mestra:
        flash("Sessão inválida. Faça login novamente.", "warning")
        return redirect(url_for('auth.login'))
    
    credenciais_do_usuario = db_session.query(Credential).filter_by(user_id=user_id).all()

    lista_decifrada=[]

    for cred in credenciais_do_usuario:
        encryption_key = generate_encryption_key(senha_mestra, cred.salt)
        senha_decifrada = decrypt_data(cred.senhacript, encryption_key)

        lista_decifrada.append({
            'site': cred.site,
            'usuario': cred.usuario,
            'senha': senha_decifrada
        })
    return render_template("dashboard.html", credenciais = lista_decifrada)