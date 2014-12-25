import doctest


class Temp(object):
	'''
	may serve as document
	can left out self.assertEqual shit and assertRaises shit

	>>> t = Temp()
	>>> t.hello()
	hello,world
	>>> 1+2
	3
	>>> "this is far more easy"
	'this is far more easy'

	'''
	def __init__(self,**kw):
		super(Temp,self).__init__(**kw)

	def hello(self):
		print "hello,world"



doctest.testmod()