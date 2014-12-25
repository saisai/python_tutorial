# -*- coding:utf-8  -*-

# 1、要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

# *****************************************
# 使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# *****************************************

# 2、编写底层模块的第一步，就是先把调用接口写出来

# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')

# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()


# __new__()方法接收到的参数依次是：

# 当前准备创建的类的对象；

# 类的名字；

# 类继承的父类集合；

# 类的方法集合。


# 3、
class Field(object):
	def __init__(self,name,column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return "<%s:%s>"%(self.__class__.__name__,self.name)

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,"varchar(100)")

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,"bigint")

# # metaclass是创建类，所以必须从`type`类型派生：
class ModelMetaclass(type):
	# 如果是Model()，直接让他调用
	def __new__(cls,name,bases,attrs):
		if name == "Model":
			return type.__new__(cls, name, bases, attrs)
		# 如果不是Model的话，就说明是自定义的model了，此时调用的name是自定义model的名字
		# 此时Model可能被修改过，加入了不是Field的东西，要过滤掉
		mappings = dict()
		for k,v in attrs.iteritems():
			if isinstance(v, Field):
				print "Found mappings %s => %s"%(k,v)
				mappings[k] = v
		for k in mappings.iterkeys():
			attrs.pop(k)
			
		# 加入额外的信息
		attrs['__table__'] = name # 假设表名和类名一致
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		return type.__new__(cls, name, bases, attrs)


# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找__metaclass__，
# 如果没有找到，就继续在父类Model中查找__metaclass__，找到了，就使用Model中定义的__metaclass__的ModelMetaclass来创建User类
class Model(dict):
	__metaclass__ = ModelMetaclass

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		# __mappings__是已经被筛选过之后的
		for k, v in self.__mappings__.iteritems():
			fields.append(v.name)
			params.append(self[k])
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))


# 这样：
# 如果没有metaclass：
# 用户在class User里面定义了这些属性，并且User继承了Model的属性
# 关键问题是，从Model继承过来的save()方法，无法获取到它自己的其他属性（各种stringField和
# integerField，因为这些都是由用户动态输入的，无法确定会有多少个，具体叫什么名字?
# 所以要用metaclass，因为metaclass的__new__会收到调用的参数

# 相当于先到metaclass做一下过滤，然后再真正创建类
# 而用户并不知情

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

class temp(object):
	def __init__(self):
		pass

	def a(self):
		print "hello"

	def getDict(self):
		pass

t = temp()
print t.getDict()


class User(Model):
	username = StringField("username")
	password = StringField("password")

# 6666666
u = User(username="laozhikun",password="123456")
u.save()

# 和静态语言很大不同！
# *****************************************
# metaclass动态添加行为->type()动态生成类
# *****************************************
