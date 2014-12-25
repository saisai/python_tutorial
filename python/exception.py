try:
	f = open("../resource/temp.txt","w")
except IOError as e:
	print "IOError"
except: # all captured
	print "all captured"
else: # no exception raised
	print "everything is fine"
finally:
	print "this will be called after all"


class NetworkError(Exception):
	pass
# raise NetworkError("network error")