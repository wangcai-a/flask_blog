#!/usr/bin/env python
import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
# from app.models import User, Userlog, Admin, Adminlog, Auth, Tag, Comment, Moviecol, Movie, Oplog, Role, Preview


app = create_app(os.getenv('Flask_config') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    """ make_shell_context() 注册了程序, 数据库实例, 以及模型."""
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()