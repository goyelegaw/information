from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import create_app, db, models

app = create_app("development")
manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
