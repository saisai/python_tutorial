import shelve
# Manage shelves of pickled objects.

class a(object):
	def __init__(self):
		self.name = "laozhikun"

obj = a()
db = shelve.open("../resource/temp.txt",protocol=2)
db["key"] = obj
db.close()