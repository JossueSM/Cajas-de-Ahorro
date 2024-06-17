class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
