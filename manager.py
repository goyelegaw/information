import logging
from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import create_app, db

app = create_app("development")
manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "itheima"
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")
    return 'index'


if __name__ == '__main__':
    manager.run()
