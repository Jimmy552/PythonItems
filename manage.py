from flask_sqlalchemy import SQLAlchemy
from app.models import Good, DetailedStore, Store
from app import create_app, db

import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# default:DevelopmentConfig
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Store=Store, DetailedStore=DetailedStore, Good=Good, roll=db.session.rollback())


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
