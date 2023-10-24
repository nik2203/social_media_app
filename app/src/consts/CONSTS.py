DBMS='mysql'
DB_HOST='localhost'
DB_NAME='test_proj'
DB_USER='root'
DB_PASSWORD='#Nikki2203'
"""
:pattern <dbms>://<username>:<password>@host/<database name>
"""
SQLALCHEMY_DATABASE_URI=f"{DBMS}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SECRET_KEY = '3PVj9PQaadsffasdfm6'
