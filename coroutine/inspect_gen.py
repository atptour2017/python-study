import inspect

def gen():
	x=1
	y=1
	while x:
		x=yield y
		print(x)
		y=x
		if not x:
			break
	#return x

if __name__=='__main__':
	g=gen()
	print(inspect.getgeneratorstate(g))
	g.send(None)
	print(inspect.getgeneratorstate(g))
	for x in range(2,5):
		print(g.send(x))
		print(inspect.getgeneratorstate(g))
	g.send(None)
	print(inspect.getgeneratorstate(g))
	#g.close()
	print(inspect.getgeneratorstate(g))