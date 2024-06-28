# 引入sqlalchemy依赖
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
 
# 申明基类对象
Base = declarative_base()
 
 
# 定义user表实体对象
class User(Base):
    # 定义表名
    __tablename__ = 'user'
    # 定义字段
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
 
    def __repr__(self):
        return "User(id:{},name:{},age:{})".format(self.id, self.name, self.age)
 
 
class SqliteSqlalchemy(object):
    def __init__(self):
        # 创建Sqlite连接引擎
        engine = create_engine('sqlite:///./sqlalchemy.db', echo=True)
        # 创建表
        Base.metadata.create_all(engine, checkfirst=True)
        # 创建Sqlite的session连接对象
        self.session = sessionmaker(bind=engine)()
 
 
if __name__ == '__main__':
    # 初始化Sqlite数据库连接，获取数据库session连接
    session = SqliteSqlalchemy().session
 
    # 新增一条用户信息数据
    user = User(name='xiaoming', age=23)
    session.add(user)
    session.commit()
 
    # 关闭数据库session连接
    session.close()