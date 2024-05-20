from flask import Config

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'