import inspect

def gen(iter):
	for x in iter:
		yield x


if __name__=='__main__':
	g=gen(range(2,10))
	print(inspect.getgeneratorstate(g))
	for x in g:
		print(x)
		print(inspect.getgeneratorstate(g))
	print(inspect.getgeneratorstate(g))
