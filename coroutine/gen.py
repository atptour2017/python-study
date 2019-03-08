#yield from的使用

#从外部获取迭代对象，直接yield from
def g1(gen):
    yield from gen

#内部生成迭代对象，直接yield from
def g2():
	a=range(5)
	yield from a

if __name__=='__main__':
	g=g1(range(10))
	g.send(None)
	for x in g:
		print(x)

	s=g2()
	s.send(None)
	for x in s:
		print(x)