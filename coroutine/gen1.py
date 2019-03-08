
def gen(iter):
	yield from iter

g=gen(range(10))
g.send(None)
g.send(None)
for x in g:
	print(x)
