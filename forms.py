from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    nome = StringField('Nome',
                       validators=[DataRequired(message="Este campo é obrigatório")])
    email = StringField('Email',
                        validators=[DataRequired(message="Este campo é obrigatório"),
                                    Email(message="Por favor, insira um email válido")])
    
    senha = PasswordField('Senha',
                          validators=[DataRequired(message="Este campo é obrigatorio"),
                                      Length(min=5, message="A senha deve ter mais que 5 caracteres")])
    
    confirmar_senha = PasswordField('Confirmar Senha', 
                                    validators=[DataRequired(message="Este campo é obrigatório."), 
                                                EqualTo('senha', message="As senhas não coincidem.")])
    
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField("Email",
                         validators=[DataRequired(message="Campo Obrigatório"),
                                      Email(message="Por favor, insira um email válido")])
    senha = PasswordField('Senha',
                           validators=[DataRequired(message="Campo Obrigatório")])
    submit = SubmitField('Login')

class NewCredentialForm(FlaskForm):
    site = StringField("Site",
                        validators=[DataRequired(message="Campo Obrigatório")])
    usuario = StringField('Usuario',
                           validators=[DataRequired(message="Campo Obrigatório")])
    senha = PasswordField('Senha',
                           validators=[DataRequired(message="Campo Obrigatório")])
    submit = SubmitField('Salvar')