from app import create_app,db,app
from app.models import Manager,User


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User )
if __name__ == '__main__':
    manager.run()
