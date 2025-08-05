from werkzeug.security import generate_password_hash, check_password_hash

def criptografarsenha(senha_texto_plano):
    """Gera um hash seguro para a senha usando o padrão da indústria."""
    # Gera um hash com um método forte e um "salt" aleatório.
    return generate_password_hash(senha_texto_plano, method='pbkdf2:sha256')

def verificarsenha(hash_salvo_no_banco, senha_fornecida_no_login):
    """Verifica se a senha fornecida corresponde ao hash salvo."""
    # Compara a senha com o hash. Retorna True ou False.
    return check_password_hash(hash_salvo_no_banco, senha_fornecida_no_login)

    