from flask import Blueprint, render_template
from forms import NewPasswordForm
cred_bp = Blueprint("cred", __name__, template_folder='templates')

@cred_bp.route('/new', methods=['POST', 'GET'])
def novaSenha():
    site = None
    usuario = None
    senha = None
    form = NewPasswordForm()

    if form.validate_on_submit():
        site = form.site.data
        usuario = form.usuario.data
        senha = form.senha.data
        form.site.data = ''
        form.usuario.data = ''
        form.senha.data = ''
    return render_template('Novasenha.html', 
                site = site,
                usuario = usuario,
                senha = senha,
                form = form)