import inspect

def gen1():
	a=range(2,10)
	for x in a:
		yield x
	return 'aa'

def gen(iter):
	a=yield from iter
	print(a)

def gen3():
	a=[]
	while True:
		x=yield
		if not x:
			break
		a.append(x)
	return a

def gen4():
	while True:
		a=gen3()
		print(inspect.getgeneratorstate(a))
		x=yield from a
		print(inspect.getgeneratorstate(a))
		print(x)

# g=gen(range(10))
# g.send(None)
# g.send(None)
# for x in g:
# 	print(x)

# a1=gen1()
# a2=gen(a1)
# for x in a2:
# 	print(x)

a=range(2,10)
g=gen4()
g.send(None)
for x in a:
	g.send(x)
g.send(None)