from server.create_app import database, flask_bcrypt

class User(database.Model):
    """
    User Model for storing user related details
    
    GitLab RS uses the your GitLab instance's API
    to retrieve your privileges information.

    The user saved in the database are just for
    internal reference.
    """
    __tablename__ = "user"

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    gitlab_id = database.Column(database.String(128), unique=True)
    username = database.Column(database.String(255), unique=True, nullable=False)
    password_hash = database.Column(database.String(128))
    created_at = database.Column(database.DateTime, nullable=False)
    updated_at = database.Column(database.DateTime, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)