import os


class Config:
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:///" + os.path.join(project_dir) + "\database.db"
    os.environ['SQLALCHEMY_DATABASE_URI'] = database_file
    os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    os.environ['SECRET_KEY'] = 'thisissupposed'
    os.environ['RECAPTCHA_USE_SSL'] = "False"
    os.environ['RECAPTCHA_PUBLIC_KEY'] = 'public'
    os.environ['RECAPTCHA_PRIVATE_KEY'] = 'private'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    RECAPTCHA_USE_SSL = os.environ.get('RECAPTCHA_USE_SSL')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_OPTIONS = os.environ.get('RECAPTCHA_OPTIONS')
