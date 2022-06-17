# Database Connection
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'projetoxp'
    )