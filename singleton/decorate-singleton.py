def singleton(cls, *args, **kw):    
	instances = {}    
	def _singleton():    
		if cls not in instances:    
			instances[cls] = cls(*args, **kw)    
		return instances[cls]    
	return _singleton

@singleton    
class MyClass(object):    
	a = 1    
	def __init__(self, x=0):    
		self.x = x 
