# -*- coding:utf-8 -*-
# 把关系数据库的表结构映射到对象上

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# sqlalchemy不会像django那样帮你创建，要你自己创建好，然后用sqlalchemy来操作

# 定义User对象:
class User(Base):
	# 表的名字:
	__tablename__ = 'user'

	# 表的结构:
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

	def __unicode__(self):
		return self.name

class Book(Base):
	__tablename__ = "book"

	id = Column(String(20), primary_key=True)
	name = Column(String(20))

	borrower_id = Column(String(20), ForeignKey('user.id'))

	def __unicode__(self):
		return self.name

class Age(Base):
	__tablename__ = "age"

	age = Column(String(20), primary_key=True)

	user_id = Column(String(20), ForeignKey('user.id'))

	def __unicode__(self):
		return self.age

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:scut8711@localhost:3306/alchemy')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
# new_user = User(id='5', name='Bob')
# new_book = Book(id="1", name="shelock holmes",borrower_id="5")
# new_age = Age(age="15",user_id="5")
# # 添加到session:
# session.add(new_user)
# session.add(new_book)
# session.add(new_age)
# # 提交即保存到数据库:
# session.commit()


print(session.query(User, Book, Age).filter(User.id == Book.borrower_id ,User.id == Age.user_id).all())



# 关闭session:
session.close()





