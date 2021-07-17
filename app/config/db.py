__all__ = ['config']

driver = 'mysql+pymysql'
host = '10.3.0.2'
port = 3306
db_name = 'assignment'
user = 'user'
password = 'test1234'
config = f'{driver}://{user}:{password}@{host}:{port}/{db_name}'