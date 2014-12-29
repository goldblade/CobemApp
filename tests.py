import os
import unittest
import tempfile
from flask import Flask
from app import db
from app.modules.adm.models.usuario import Usuario
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy


class TestCase(unittest.TestCase):

    def setUp(self):
        #app.config['TESTING'] = True
        #app.config['WTF_CSRF_ENABLED'] = False
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        #self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        '''
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.db = SQLAlchemy(self.app)
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()
            self.db.create_all()
        '''

        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app.config['TESTING'] = True
        #self.db = SQLAlchemy(self.app)
        self.db = SQLAlchemy()
        self.db.init_app(self.app)
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.create_all()

    def tearDown(self):
        pass

        #self.db.session.remove()
        #self.db.drop_all()
        #os.unlink(os.path.join(basedir, 'test.db'))

        '''
        self.app = Flask(__name__)
        self.db = SQLAlchemy(self.app)
        #db.init_app(self.app)
        with self.app.app_context():
            self.db.drop_all()
        '''
        #print 'tearDown'

    def test_user(self):
        u = Usuario()
        u.nome = 'Gold'
        u.login = 'gold'
        u.ativo = True
        u.email = 'ej@eduardojunior.com'
        u.set_senha('gold')
        self.db.session.add(u)
        self.db.session.commit()
        gold = Usuario.query.filter_by(login='gold').first()
        #assert gold is not None
        #assert nick != 'Teste'

if __name__ == '__main__':
    unittest.main()