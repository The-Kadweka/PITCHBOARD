from app import create_app, db
from app.models import User,Role
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand


#Creating app instance
app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_sontext():
    return dict(app = app,db = db,User = User, Role = Role )
if __name__=='__main__':
    app.secret_key = 'kadweka'
    manager.run()