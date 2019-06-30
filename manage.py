from app import create_app, db
from app.models import User
from flask_script import Manager,Server

#Creating app instance
app = create_app('development')
manager = Manager(app)


@manager.shell
def make_shell_sontext():
    return dict(app = app,db = db,User = User)

if __name__=='__main__':
    app.secret_key = 'kadweka'
    manager.run()