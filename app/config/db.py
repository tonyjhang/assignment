__all__ = ['config']

driver = 'mysql+pymysql'
host = '127.0.0.1'
port = 3306
db_name = 'assignment'
user = 'user'
password = 'test1234'
config = f'{driver}://{user}:{password}@{host}:{port}/{db_name}'