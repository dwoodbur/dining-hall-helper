from gluon.tools import Auth
from gluon.contrib.login_methods.email_auth import email_auth

db = DAL('sqlite://storage.sqlite')

auth = Auth(db)
auth.define_tables()
auth.settings.login_methods.append(email_auth('smtp.gmail.com:465', '@ucsc.com'))
